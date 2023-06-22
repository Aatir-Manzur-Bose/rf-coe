#!/usr/bin/env python
"""
    Python based USB CLI Application interface control for vaunix LDA devices on windows-64bit machine
    JA 05/05/2021   Initial Version of USB CLI control Interface
    NB 07/28/2022   Updates
    RD 08/01/2022   Updates
    NB 08/04/2022   Updates
    RD 8/4 - 8/18   Re-design and updates, error handlers, enhanced functionality
    (c) 2021-2022 by Vaunix Technology Corporation, all rights reserved

    This class provides an example layer above the DLL API which provide some additional functionality * Devices can
    be selected by serial number, or for simple applications by their device number * Device numbers are a simplified
    index to the devices. If you only have one device, then the device number is 1 * The class allows the application
    software to open and close LDA devices by the serial number of the device * Opening a device by serial number
    also provides the corresponding device number * Using the class is very simple, Call find_devices,
    open the device or devices you want to work with, set of get parameters and then close the devices when your
    program is done.


"""

from __future__ import annotations
import ctypes
import getopt
import math
import os
import sys
from ctypes import *
from time import sleep
import threading
import time
import numpy as np

# DLL error codes and constants
INVALID_DEVID = 0x80000000
BAD_PARAMETER = 0x80010000
BAD_HID_IO = 0x80020000
DEVICE_NOT_READY = 0x80030000
FEATURE_NOT_SUPPORTED = 0x80040000
MAXDEVICES = 64


class LDAError(Exception):
    pass


def square_wave(increment: int, attn: CLIVaunixAttn):
    i = 0
    while 1:
        i += 1
        if i % 5 == 0:
            attn.find_error(attn.vnx.fnLDA_SetAttenuationHR(attn.get_devid(1), int(float(60) * 20)))
        else:
            attn.find_error(attn.vnx.fnLDA_SetAttenuationHR(attn.get_devid(1), int(float(10) * 20)))


def sine_wave(attn: CLIVaunixAttn):
    x = []
    y = []
    j = 0
    i = 0
    while True:
        x.append(math.radians(20 * j))
        y.append(int(math.sin(math.radians(20 * j)) * 60))
        print(abs(y[i]))

        # ax.plot(x, y, color='b')

        # fig.canvas.draw()

        # fig.show()
        # plt.pause(0.05)
        attn.find_error(attn.vnx.fnLDA_SetAttenuationHR(attn.get_devid(1), int(float(abs(y[i]*20)))))
        i += 1
        j += 1




class CLIVaunixAttn:

    def __init__(self, name="ldaApi", port=''):
        os.add_dll_directory(os.getcwd())
        self.vnx = cdll.VNX_atten64
        self.vnx.fnLDA_SetTestMode(False)
        self.num_devices = 0
        device_id_array = c_int * MAXDEVICES
        self.devices_buffer = device_id_array()
        # RD testing
        # self.raise_errors = False
        self.raise_errors = True
        self.devices_list = [0]

    # New Functions

    class Counter:
        def __init__(self, increment: int, attn: CLIVaunixAttn):
            self.next_t = time.time()
            self.i = 0
            self.done = False
            self.increment = increment
            self._run()
            self.attn = attn

        def _run(self):
            print("hello ", self.i)
            if self.i % 5 == 0:
                self.attn.find_error(self.attn.vnx.fnLDA_SetAttenuationHR(self.attn.get_devid(1), int(float(50) * 20)))
            else:
                self.attn.find_error(self.attn.vnx.fnLDA_SetAttenuationHR(self.attn.get_devid(1), int(float(10) * 20)))

            self.next_t += self.increment
            self.i += 1
            if not self.done:
                threading.Timer(self.next_t - time.time(), self._run).start()

        def stop(self):
            self.done = True

    # validate a device number and return its devid handle this function also handles type conversions if the devnum
    # passed is not an integer if raise_errors is true it will raise an exception for invalid device numbers.
    # Otherwise, it will return INVALID_DEVID
    def get_devid(self, devnum):
        if type(devnum) != int:
            tmp_devnum = int(devnum)
        else:
            tmp_devnum = devnum
        # print("in get_devid ", tmp_devnum)
        if tmp_devnum > 0 and tmp_devnum <= self.num_devices:
            return self.devices_list[tmp_devnum - 1]
        else:
            return self.find_error(INVALID_DEVID)

    # Fills local array devices_list with device IDs, returns number of connected devices.
    def find_devices(self):
        # The DLL will search for devices and return zero or the number of connected LDA devices
        self.num_devices = self.vnx.fnLDA_GetNumDevices()
        # The DLL will return zero or the number of connected LDA devices and fill in the list of device ID handles
        self.num_devices = self.vnx.fnLDA_GetDevInfo(self.devices_buffer)
        self.devices_list = [0]
        self.devices_list = self.devices_buffer[:self.num_devices]

        # print("the new device_list")
        # print(self.devices_list)
        # print("device_list length= ", len(self.devices_list))

        return self.num_devices

    # Initializes device using device number, returns device number or error code if the DLL exceptions are disabled
    # by setting raise_errors = False
    # calling programs should test if the return value is equal to the device number, if it is not an error occurred
    # note that devid handles may be equal to devnum values but that relationship is not guaranteed
    def open_device(self, devnum):
        devid = self.get_devid(devnum)
        temp = self.find_error(self.vnx.fnLDA_InitDevice(devid))
        if temp == 0:
            return devnum
        else:
            return temp

    # Initializes device using SN, returns device number
    def open_device_sn(self, devsn):
        for devid in self.devices_list:
            sn = self.get_serial_number(devid)
            if sn == devsn:
                temp = self.find_error(self.vnx.fnLDA_InitDevice(devid))
                if temp == 0:
                    devnum = 1
                    # look through the list of device ids to find which entry's location corresponds to the matched serial number
                    # that's our devnum for this devid minus 1 (which is why our counter starts at 1 instead of 0)
                    for itmp in self.devices_list:
                        if itmp == devid:
                            return devnum
                        else:
                            devnum += 1
                else:
                    # the open returned an error
                    return temp

        # we did not find a device with the serial number       
        self.find_error(INVALID_DEVID)
        return 0

    # Closes device using ID, returns device ID or error code if the DLL exceptions are disabled
    # by setting raise_errors = False
    # calling programs should test if the return value is equal to the devid, if it is not an error occurred
    def close_device(self, devnum):
        devid = self.get_devid(devnum)
        temp = self.find_error((self.vnx.fnLDA_CloseDevice(devid)))
        if (temp == 0):
            return devnum
        else:
            return temp

    # Closes device using SN, returns device ID
    def close_device_sn(self, devsn):
        for devid in self.devices_list:
            sn = self.get_serial_number(devid)
            if sn == devsn:
                temp = self.find_error(self.vnx.fnLDA_CloseDevice(devid))
                if temp == 0:
                    devnum = 1
                    # look through the list of device ids to find which entry's location corresponds to the matched serial number
                    # that's our devnum for this devid minus 1 (which is why our counter starts at 1 instead of 0)
                    for itmp in self.devices_list:
                        if itmp == devid:
                            return devnum
                        else:
                            devnum += 1
                else:
                    # the close returned an error
                    return temp

        # we did not find a device with the serial number
        self.find_error(INVALID_DEVID)
        return 0

    # Returns number of channels
    def get_num_channels(self, devnum):
        devid = self.get_devid(devnum)
        return self.find_error(self.vnx.fnLDA_GetNumChannels(devid))

    # Gets the device number for a specified serial number
    def get_device_num(self, devsn):
        for devid in self.devices_list:
            sn = self.get_serial_number(devid)
            if sn == devsn:
                devnum = 1
                # look through the list of device ids to find which entry's location corresponds to the matched serial number
                # that's our devnum for this devid minus 1 (which is why our counter starts at 1 instead of 0)
                for itmp in self.devices_list:
                    if itmp == devid:
                        return devnum
                    else:
                        devnum += 1

        self.find_error(INVALID_DEVID)
        return 0

    # Gets the device ID for a specified serial number
    def get_device_id(self, devsn):
        for devid in self.devices_list:
            sn = self.get_serial_number(devid)
            if sn == devsn:
                return devid

        self.find_error(INVALID_DEVID)
        return 0

    # Start and stop attenuation ramp (True - begin sweep, False - stop sweep)
    def activate_ramp(self, devnum, channel, go):
        devid = self.get_devid(devnum)
        self.set_channel(devid, channel)
        self.find_error(self.vnx.fnLDA_StartRamp(devid, go))

    # Set the step size for the frist phase of an attenuation ramp
    def set_attenuation_step(self, devnum, channel, step):
        devid = self.get_devid(devnum)
        self.set_channel(devid, channel)
        self.find_error(self.vnx.fnLDA_SetAttenuationStepHR(devid, int(float(step) * 20)))

    # Sets the step size for the second phase of an attenuation ramp
    def set_attenuation_step_two(self, devnum, channel, step):
        devid = self.get_devid(devnum)
        self.set_channel(devid, channel)
        self.find_error(self.vnx.fnLDA_SetAttenuationStepTwoHR(devid, int(float(step) * 20)))

    # Changes if error codes are returned or errors are raised by functions (False - raise errors, True - error codes)
    def ignore_errors(self, ignore):
        self.raise_errors = ignore

    # Get device status
    def get_status(self, devnum):
        devid = self.get_devid(devnum)
        return self.find_error(self.vnx.fnLDA_GetDeviceStatus(devid))

    # Checks values returned by functions for error codes
    def find_error(self, returned_value):
        if not self.raise_errors:
            if (returned_value & 0x80000000):
                err_test = returned_value & 0xFFFFFFFF
                print(err_test)
                if err_test == INVALID_DEVID:
                    raise LDAError("Invalid Device ID")
                elif err_test == BAD_PARAMETER:
                    raise LDAError("Parameter Out of Range")
                elif err_test == BAD_HID_IO:
                    raise LDAError("Communication Failure")
                elif err_test == DEVICE_NOT_READY:
                    raise LDAError("Device Not Ready")
                elif err_test == FEATURE_NOT_SUPPORTED:
                    raise LDAError("Feature Not Supported")
                else:
                    raise LDAError("Unknown DLL Error")
        return returned_value

    # Previous functions
    # Get local list of devices
    def get_devices_list(self):
        return self.devices_list

    # Get serial number
    def get_serial_number(self, devnum):
        devid = self.get_devid(devnum)
        return self.find_error(self.vnx.fnLDA_GetSerialNumber(devid))

    # Returns True if device is connected, False if device is not connected
    def check_deviceexists(self, devnum):
        devid = self.get_devid(devnum)
        try:
            tmp = self.get_status(devid) & 0x00000001  # isolate the lsb which is 1 for a connected device
            if tmp == 0:
                return False
        except:
            return False
        else:
            return True

            # Get Model Name

    def get_modelname(self, devnum):
        devid = self.get_devid(devnum)
        self.data = ctypes.create_string_buffer(32)
        self.find_error(self.vnx.fnLDA_GetModelNameA(devid, ctypes.byref(self.data)))
        return self.data.value

    # Get LDA DLL Version
    def get_dllversion(self):
        self.data = self.find_error(self.vnx.fnLDA_GetDLLVersion())
        return self.data

    # Get Min. Frequency
    def get_minfrequency(self, devnum):
        devid = self.get_devid(devnum)
        result = self.find_error(self.vnx.fnLDA_GetMinWorkingFrequency(devid))
        return (result / 10)

    # Get Max. Frequency
    def get_maxfrequency(self, devnum):
        devid = self.get_devid(devnum)
        result = self.find_error(self.vnx.fnLDA_GetMaxWorkingFrequency(devid))
        # print(f"devnum is: {self.vnx.fnLDA_GetWorkingFrequency(devid)}")

        print(f"result is {result}*********")
        return (result / 10)

    # Get Min. Attenuation
    def get_minattenuation(self, devnum):
        devid = self.get_devid(devnum)
        result = self.find_error(self.vnx.fnLDA_GetMinAttenuationHR(devid))
        return (result / 20.0)

    # Get Max. Attenuation
    def get_maxattenuation(self, devnum):
        devid = self.get_devid(devnum)
        result = self.find_error((self.vnx.fnLDA_GetMaxAttenuationHR(devid)))
        return (result / 20.0)

    # Get Current Frequency
    def get_currentfrequency(self, devnum, channel):
        devid = self.get_devid(devnum)
        self.set_channel(devid, channel)
        result = self.find_error(self.vnx.fnLDA_GetWorkingFrequency(devid))
        return (result / 10)

    # Get Current Attenuation
    def get_currentattenuation(self, devnum, channel):
        devid = self.get_devid(devnum)
        self.set_channel(devid, channel)
        result = self.find_error(self.vnx.fnLDA_GetAttenuationHR(devid))
        return (result / 20.0)

    # Get Ramp Start
    def get_rampstart(self, devid, channel):
        self.set_channel(devid, channel)
        self.data = self.find_error(self.vnx.fnLDA_GetRampStartHR(devid))
        return (self.data / 20.0)

    # Get Ramp End
    def get_rampend(self, devnum, channel):
        devid = self.get_devid(devnum)
        self.set_channel(devid, channel)
        result = self.find_error(self.vnx.fnLDA_GetRampEndHR(devid))
        return (result / 20.0)

    # Get Dwell time
    def get_dwelltime(self, devnum, channel):
        devid = self.get_devid(devnum)
        self.set_channel(devid, channel)
        result = self.find_error(self.vnx.fnLDA_GetDwellTime(devid))
        return result

    # Get bi-directional ramp dwelltime
    def get_bidirectional_dwelltime(self, devnum, channel):
        devid = self.get_devid(devnum)
        self.set_channel(devid, channel)
        self.data = self.find_error(self.vnx.fnLDA_GetDwellTimeTwo(devid))
        return self.data

    # Get Idle time
    def get_idletime(self, devnum, channel):
        devid = self.get_devid(devnum)
        self.set_channel(devid, channel)
        result = self.find_error(self.vnx.fnLDA_GetIdleTime(devid))
        return result

    # Get hold time
    def get_holdtime(self, devnum, channel):
        devid = self.get_devid(devnum)
        self.set_channel(devid, channel)
        result = self.find_error(self.vnx.fnLDA_GetHoldTime(devid))
        return result

    # Get profile count
    def get_profilecount(self, devnum, channel):
        devid = self.get_devid(devnum)
        self.set_channel(devid, channel)
        self.data = self.find_error(self.vnx.fnLDA_GetProfileCount(devid))
        return self.data

    # Get Profile Max length
    def get_profilemaxlength(self, devnum, channel):
        devid = self.get_devid(devnum)
        self.set_channel(devid, channel)
        result = self.find_error(self.vnx.fnLDA_GetProfileMaxLength(devid))
        return result

    # Get Profile Dwell time
    def get_profiledwelltime(self, devnum, channel):
        devid = self.get_devid(devnum)
        self.set_channel(devid, channel)
        result = self.find_error(self.vnx.fnLDA_GetProfileDwellTime(devid))
        return result

    # Get Profile Idle time
    def get_profileidletime(self, devnum, channel):
        devid = self.get_devid(devnum)
        self.set_channel(devid, channel)
        result = self.find_error(self.vnx.fnLDA_GetProfileIdleTime(devid))
        return result

    # Get Profile Index
    def get_profileindex(self, devnum, channel):
        devid = self.get_devid(devnum)
        self.set_channel(devid, channel)
        result = self.find_error(self.vnx.fnLDA_GetProfileIndex(devid))
        return result

    # Set Attenuation
    def set_attenuation(self, devnum, channel, attenuation):
        devid = self.get_devid(devnum)
        self.set_channel(devid, channel)
        self.find_error(self.vnx.fnLDA_SetAttenuationHR(devid, int(float(attenuation) * 20)))

    # Set Frequency
    def set_frequency(self, devnum, channel, frequency):
        devid = self.get_devid(devnum)
        self.set_channel(devid, channel)
        self.find_error(self.vnx.fnLDA_SetWorkingFrequency(devid, int(float(frequency) * 10)))

    # Set Channel
    def set_channel(self, devnum, channel):
        devid = self.get_devid(devnum)
        if self.find_error(self.vnx.fnLDA_GetNumChannels(devid)) > 1:
            self.find_error(self.vnx.fnLDA_SetChannel(devid, int(channel)))

    # Set Ramp Start
    def set_rampstartattenuation(self, devnum, channel, attenuation):
        devid = self.get_devid(devnum)
        self.set_channel(devid, channel)
        self.find_error(self.vnx.fnLDA_SetRampStartHR(devid, int(float(attenuation) * 20)))

    # Set Ramp End
    def set_rampendattenuation(self, devnum, channel, attenuation):
        devid = self.get_devid(devnum)
        self.set_channel(devid, channel)
        self.find_error(self.vnx.fnLDA_SetRampEndHR(devid, int(float(attenuation) * 20)))

    # Set dwell time
    def set_dwelltime(self, devnum, channel, dwelltime):
        devid = self.get_devid(devnum)
        self.set_channel(devid, channel)
        self.find_error(self.vnx.fnLDA_SetDwellTime(devid, int(dwelltime)))

    # Set idle time
    def set_idletime(self, devnum, channel, idletime):
        devid = self.get_devid(devnum)
        self.set_channel(devid, channel)
        self.find_error(self.vnx.fnLDA_SetIdleTime(devid, int(idletime)))

    # Set bidirectional dwell time
    def set_bidirectionaldwelltime(self, devnum, channel, dwelltime):
        devid = self.get_devid(devnum)
        self.set_channel(devid, channel)
        self.find_error(self.vnx.fnLDA_SetDwellTimeTwo(devid, int(dwelltime)))

    # Set hold time
    def set_holdtime(self, devnum, channel, holdtime):
        devid = self.get_devid(devnum)
        self.set_channel(devid, channel)
        self.find_error(self.vnx.fnLDA_SetHoldTime(devid, int(holdtime)))

    # Set Ramp direction  -- True: Upwards, False: Downwards
    def set_rampdirection(self, devnum, channel, rampdirection):
        devid = self.get_devid(devnum)
        self.set_channel(devid, channel)
        self.find_error(self.vnx.fnLDA_SetRampDirection(devid, int(rampdirection)))

    # Set bidirectional Ramp direction (True - Bi-directional, False - Uni-directional)
    def set_rampbidirectional(self, devnum, channel, rampdirection):
        devid = self.get_devid(devnum)
        self.set_channel(devid, channel)
        self.find_error(self.vnx.fnLDA_SetRampBidirectional(devid, int(rampdirection)))

    # Set Rampmode (False - Once, True - Continuous)
    def set_rampmode(self, devnum, channel, rampmode):
        devid = self.get_devid(devnum)
        self.set_channel(devid, channel)
        self.find_error(self.vnx.fnLDA_SetRampMode(devid, rampmode))

    # Set profile element data
    def set_profileelements(self, devnum, channel, profileindex, profiledata):
        #        print('profiledata:%r', int(profiledata)*10)
        devid = self.get_devid(devnum)
        self.set_channel(devid, channel)
        self.find_error(self.vnx.fnLDA_SetProfileElementHR(devid, int(profileindex), int(float(profiledata) * 20)))

    # Set profile count
    def set_profilecount(self, devnum, channel, profilelen):
        devid = self.get_devid(devnum)
        self.set_channel(devid, channel)
        self.find_error(self.vnx.fnLDA_SetProfileCount(devid, int(profilelen)))

    # Set profile Idletime
    def set_profileidletime(self, devnum, channel, idletime):
        devid = self.get_devid(devnum)
        self.set_channel(devid, channel)
        self.find_error(self.vnx.fnLDA_SetProfileIdleTime(devid, int(idletime)))

    # Set profile Dwell time
    def set_profiledwelltime(self, devnum, channel, dwelltime):
        devid = self.get_devid(devnum)
        self.set_channel(devid, channel)
        self.find_error(self.vnx.fnLDA_SetProfileDwellTime(devid, int(dwelltime)))

    # Set profile mode (0 - Off, 1 - Once, 2 - Repeat)
    def set_profilemode(self, devnum, channel, profilemode):
        devid = self.get_devid(devnum)
        self.set_channel(devid, channel)
        self.find_error(self.vnx.fnLDA_StartProfile(devid, int(profilemode)))

    # Save settings
    def set_savesettings(self, devnum, channel):
        devid = self.get_devid(devnum)
        self.set_channel(devid, channel)
        self.find_error(self.vnx.fnLDA_SaveSettings(devid))

    # Print the help message
    def show_helpmessage(self):
        print(
            'ldausbcli.py -i <deviceid[id:id:...,a-all]> -c <channel[chnl:chnl:...,a-all]> -a <attenuation> -f '
            '<frequency> -s <rampstart> -e <rampend> -w <dwelltime> -d <idletime> -o <holdtime> -b '
            '<bidirectional-dwelltime> -D <rampdirection[0-Down,1-Up]> -B <rampbidirectional[0-Unidirectional,'
            '1-Bidirectional]> -M <rampmode[0-Once,1-Continuous,2-Off]> -C <profilecount> -I <profileidletime> -W '
            '-k <ramp up attenuation[]> -p <ramp down attenuation>',
            '<profiledwelltime> -F <profilefile> -O <profilemode[0-Off,1-Once,2-Repeat]> -S <savesetting> -r <read> '
            '-Z <indefinite Square wave>' '-H <infinite Sine wave>')

    # Main Function call
    def main(self, argv):
        active_devices = {}  # a dictionary where each integer key is a device number (in the user numbering space, not a DLL handle)
        # the associated string value specifies the channels associated with the device, or is null if no channel selection
        # has occurred yet
        selected_devices = []  # a list where each entry is a device number from 1 to N that the user has selected
        current_channels = []
        opened_devices = []  # a list of devices we opened, each entry is a device number
        num_devices = 0  # the number of LDA devices we have
        result = 0  # temporary variable used to hold results of method calls
        print("LDA Demo Program")
        attobj = CLIVaunixAttn()

        # Verify that valid options are used in the command line
        try:
            opts, args = getopt.getopt(argv, 'hi:a:f:c:s:e:w:d:o:b:D:B:M:C:I:W:F:O:S:r:ZXk:p:',
                                       ['idevid=', 'aattn=', 'ffreq=', 'cchnl=', 'srmst=', 'ermed=', 'wdwtm=', 'didtm=',
                                        'ohdtm=', 'bdwtm=', 'Drmdi=', 'Bbimd=', 'Mrmmd=', 'Cprct=', 'Iprit=', 'Wprdt=',
                                        'Fprel=', 'Oprmd=', 'Svst=', 'Square=', "Sine=", "step=", "step2="
                                        ])
        except getopt.GetoptError as err:
            print(err)
            print("ldausbcli.py argument error")
            sys.exit(2)

        # Display the help message if no other options are selected
        if len(opts) == 0:
            attobj.show_helpmessage()
            sys.exit(0)

        # find how many LDA devices are available to use
        num_devices = attobj.find_devices()

        # let the user know if there are no LDA devices attached
        if num_devices == 0:
            print("No Devices Connected...")
            sys.exit(2)

        # Automatically select the device if only one device is connected
        if num_devices == 1:
            # we only have one device, so it must be device number 1
            devnum = 1
            # open the device
            try:
                result = attobj.open_device(devnum)
                # print(f"devnum is: {devnum}")
                # print(f"open call says: {result}")
                if result != devnum:
                    # some kind of error occurred, but error trapping was disabled
                    print("Error opening the LDA device")
                    sys.exit(2)
            except:
                print("Exception error opening the LDA device")
                sys.exit(2)
            else:
                # the LDA device opened successfully, add it's handle to the list of opened devices
                opened_devices.append(devnum)

            # set the channel selection tokens into the active_devices dictionary structure
            if attobj.get_num_channels(devnum) == 1:
                active_devices[devnum] = '1'
            else:
                active_devices[devnum] = ''
            channel = active_devices[devnum]
            selected_devices.append(devnum)

            # Loop through each command option in the command line
        for opt, arg in opts:
            # Display command options help message
            if opt == '-h':
                attobj.show_helpmessage()
                continue

            # Set Device Number to select devices
            elif opt in ('-i', '--idevid'):
                device_selected = arg

                # if there is only one device we don't need to do device selection here
                # but we check the command line for validity anyway
                if num_devices == 1:
                    if device_selected != "1":
                        print("Only one device is available")
                        if device_selected == 'a':
                            print("All devices option a has no effect")
                        else:
                            print(f"Device {device_selected} is not available")
                    continue

                # at this point we have multiple LDA devices available and device selection options are mandatory the
                # option 'a' selects all attached LDA devices, a number or list of numbers (or serial numbers)
                # separated by ':' selects one or more devices. At least one device must be selected before other
                # commands are valid

                # Opens all devices
                if device_selected == 'a':
                    devs = range(1, num_devices + 1)
                    for tmp_id in devs:
                        if tmp_id not in active_devices.keys():
                            try:
                                devnum = tmp_id
                                result = attobj.open_device(devnum)
                                if result != devnum:
                                    # some kind of error occurred, but error trapping was disabled
                                    print("Error opening the LDA device")
                                    sys.exit(2)
                            except:
                                print("Exception error opening the LDA device")
                                sys.exit(2)
                            else:
                                # the LDA device opened successfully, add its handle to the list of opened devices
                                opened_devices.append(devnum)
                                # add the channel list to the device if we only have 1 channel in this device
                                if attobj.get_num_channels(devnum) == 1:
                                    active_devices[devnum] = '1'
                                else:
                                    active_devices[devnum] = ''

                                # add this device to the list of selected devices
                                selected_devices.append(tmp_id)

                # Opens specified list of devices
                else:
                    device_selected_list = device_selected.split(':')
                    for tmp_id in device_selected_list:
                        # Open device by its id for id numbers smaller than any possible serial number, and
                        # in the range of possible device numbers (the DLL supports only 64 devices)
                        lda_id = int(tmp_id)
                        if 64 > lda_id > 0:
                            devnum = lda_id
                            if attobj.check_deviceexists(devnum):
                                if lda_id not in active_devices.keys():
                                    try:
                                        result = attobj.open_device(devnum)

                                        if result != devnum:
                                            # some kind of error occurred, but error trapping was disabled
                                            print("Error opening the LDA device")
                                            sys.exit(2)
                                    except:
                                        print("Exception error opening the LDA device")
                                        sys.exit(2)
                                    else:
                                        # the LDA device opened successfully, add its device number to the list of
                                        # opened devices
                                        opened_devices.append(devnum)
                                        # add the channel list to the device if we only have 1 channel in this device
                                        if attobj.get_num_channels(devnum) == 1:
                                            active_devices[devnum] = '1'
                                        else:
                                            active_devices[devnum] = ''

                                        # add this device to the list of selected devices
                                        selected_devices.append(devnum)

                        # Open device using serial number
                        else:
                            sn = lda_id
                            devnum = attobj.get_device_num(sn)
                            if devnum != 0:
                                if devnum not in active_devices.keys():
                                    try:
                                        result = attobj.open_device(devnum)
                                        if result != devnum:
                                            # some kind of error occurred, but error trapping was disabled
                                            print("Error opening the LDA device by serial number")
                                            sys.exit(2)
                                    except:
                                        print("Exception error opening the LDA device by serial number")
                                        sys.exit(2)
                                    else:
                                        # the LDA device opened successfully, add its device number to the list of
                                        # opened devices
                                        opened_devices.append(devnum)
                                        # add the channel list to the device if we only have 1 channel in this device
                                        if attobj.get_num_channels(devnum) == 1:
                                            active_devices[devnum] = '1'
                                        else:
                                            active_devices[devnum] = ''

                                        # add this device to the list of selected devices
                                        selected_devices.append(devnum)

                            else:
                                print(f"Could not connect to device with sn: {sn}")
                                sys.exit(2)

                continue

            # Informs user if device selection is required
            if len(opt) > 0 and len(selected_devices) == 0 and opt != '-r':
                if attobj.num_devices >= 1:
                    print(f"Device selection opt '-i' is required before opt '{opt}'...")
                    sys.exit(2)
                else:
                    print("No Devices Connected...")
                    sys.exit(2)
                continue

            # Loops through each device that the user is controlling
            for dev in selected_devices:
                if opt == '-r':
                    break
                if len(selected_devices) > 1:
                    print('Device:', dev)
                # Set Channel
                if opt in ('-c', '--cchnl'):
                    print('Channel #[s]:', arg)
                    channel = arg
                    current_channels = []
                    # Selects all channels
                    if channel == 'a':
                        active_devices[dev] = 'a'
                        for chnl in range(1, attobj.get_num_channels(dev) + 1):
                            current_channels.append(chnl)
                    # Selects specified list of channels
                    else:
                        channel_list = channel.split(':')
                        for chnl in channel_list:
                            try:
                                chnl = int(chnl)
                                if 0 < chnl <= attobj.get_num_channels(dev):
                                    current_channels.append(chnl)
                                else:
                                    print("Channel error")
                                    print(f"Invalid channel {arg}...")
                                    sys.exit(2)
                            except:
                                print("Channel error 2")
                                print(f"Invalid channel {arg}...")
                                sys.exit(2)

                        active_devices[dev] = channel
                    continue

                # Retrieves the channels that the user will control
                else:
                    current_channels = []
                    if active_devices[dev] == 'a':
                        for chnl in range(1, attobj.get_num_channels(dev) + 1):
                            current_channels.append(chnl)
                    else:
                        channel_list = active_devices[dev].split(':')
                        for chnl in channel_list:
                            if chnl != '':
                                current_channels.append(int(chnl))

                # Informs user if channel selection is required
                if len(current_channels) == 0 or '' in current_channels:
                    if opt != '-r':
                        print(f"Channel selection opt '-c' is required before opt '{opt}'...")
                        sys.exit(2)
                    continue

                # Loops through each channel that the user is controlling
                for channel in current_channels:
                    channel = int(channel)
                    # Set Attenuation
                    if opt in ('-a', '--aattn'):
                        attenuation = arg
                        print('Attenuation:', attenuation)
                        if attobj.check_deviceexists(dev):
                            attobj.set_attenuation(dev, channel, attenuation)
                        else:
                            print(f"Could not connect to device {dev}...")
                            sys.exit(2)
                    # Set Frequency
                    elif opt in ('-f', '--ffreq'):
                        frequency = arg
                        print('frequency:', frequency)
                        if attobj.check_deviceexists(dev):
                            attobj.set_frequency(dev, channel, frequency)
                        else:
                            print(f"Could not connect to device {dev}...")
                            sys.exit(2)

                    # Set Rampstart
                    elif opt in ('-s', '--srmst'):
                        rampstart = arg
                        print('rampstart:', rampstart)
                        if attobj.check_deviceexists(dev):
                            attobj.set_rampstartattenuation(dev, channel, rampstart)
                        else:
                            print(f"Could not connect to device {dev}...")
                            sys.exit(2)

                    # Set RampEnd
                    elif opt in ('-e', '--ermed'):
                        rampend = arg
                        print('rampend:', rampend)
                        if attobj.check_deviceexists(dev):
                            attobj.set_rampendattenuation(dev, channel, rampend)
                        else:
                            print(f"Could not connect to device {dev}...")
                            sys.exit(2)


                    # Set Dwell time
                    elif opt in ('-w', '--wdwtm'):
                        dwelltime = arg
                        print('dwelltime:', dwelltime)
                        if attobj.check_deviceexists(dev):
                            attobj.set_dwelltime(dev, channel, dwelltime)
                        else:
                            print(f"Could not connect to device {dev}...")
                            sys.exit(2)

                    # Set Idle time
                    elif opt in ('-d', '--didtm'):
                        idletime = arg
                        print('idletime:', idletime)
                        if attobj.check_deviceexists(dev):
                            attobj.set_idletime(dev, channel, idletime)
                        else:
                            print(f"Could not connect to device {dev}...")
                            sys.exit(2)


                    # Set hold time
                    elif opt in ('-o', '--ohdtm'):
                        holdtime = arg
                        print('holdtime:', holdtime)
                        if attobj.check_deviceexists(dev):
                            attobj.set_holdtime(dev, channel, holdtime)
                        else:
                            print(f"Could not connect to device {dev}...")
                            sys.exit(2)

                    # Set bi-directional dwell time
                    elif opt in ('-b', '--bdwtm'):
                        bddwelltime = arg
                        print('bddwelltime:', bddwelltime)
                        if attobj.check_deviceexists(dev):
                            attobj.set_bidirectionaldwelltime(dev, channel, bddwelltime)
                        else:
                            print(f"Could not connect to device {dev}...")
                            exit(2)

                    # Set step (on way down)
                    elif opt in ('-k', '--step'):
                        step = arg
                        print('step:', step)
                        if attobj.check_deviceexists(dev):
                            attobj.set_attenuation_step(dev, channel, step)
                        else:
                            print(f"Could not connect to device {dev}...")
                            exit(2)

                    # Set step (on way up)
                    elif opt in ('-p', '--step2'):
                        step = arg
                        print('step:', step)
                        if attobj.check_deviceexists(dev):
                            attobj.set_attenuation_step_two(dev, channel, step)
                        else:
                            print(f"Could not connect to device {dev}...")
                            exit(2)

                    # Set ramp direction
                    elif opt in ('-D', '--Drmdi'):
                        rmpdir = arg
                        print('ramp direction:', rmpdir)
                        if attobj.check_deviceexists(dev):
                            attobj.set_rampdirection(dev, channel, rmpdir)
                        else:
                            print(f"Could not connect to device {dev}...")
                            sys.exit(2)
                    # start square wave
                    elif opt in ('-Z', '--Square'):
                        print('generating square wave indefinitely')
                        square_wave(1, attobj)

                    elif opt in ('-X', '--Sine'):
                        print('generating sine wave indefinitely')
                        sine_wave(attobj)

                    # Set ramp bi-direction
                    elif opt in ('-B', '--Bbimd'):
                        rmpdir = arg
                        print('ramp bi-direction:', rmpdir)
                        if attobj.check_deviceexists(dev):
                            attobj.set_rampbidirectional(dev, channel, rmpdir)
                        else:
                            print(f"Could not connect to device {dev}...")
                            sys.exit(2)

                    # Set ramp mode
                    elif opt in ('-M', '--Mrmmd'):
                        rmpmode = int(arg)
                        print('ramp mode:', rmpmode)
                        if attobj.check_deviceexists(dev):
                            if rmpmode == 0 or rmpmode == 1:
                                attobj.set_rampmode(dev, channel, bool(rmpmode))
                                attobj.activate_ramp(dev, channel, True)
                            elif rmpmode == 2:
                                attobj.activate_ramp(dev, channel, False)
                            else:
                                print(f"Invalid ramp mode {rmpmode}...")
                        else:
                            print(f"Could not connect to device {dev}...")
                            sys.exit(2)

                    # Set Profile count
                    elif opt in ('-C', '--Cprct'):
                        profilecount = arg
                        print('profile count:', profilecount)
                        if attobj.check_deviceexists(dev):
                            attobj.set_profilecount(dev, channel, profilecount)
                        else:
                            print(f"Could not connect to device {dev}...")
                            sys.exit(2)

                    # Set Profile idletime
                    elif opt in ('-I', '--Iprit'):
                        profileidletime = arg
                        print('profile idle-time:', profileidletime)
                        if attobj.check_deviceexists(dev):
                            attobj.set_profileidletime(dev, channel, profileidletime)
                        else:
                            print(f"Could not connect to device {dev}...")
                            sys.exit(2)

                    # Set Profile dwelltime
                    elif opt in ('-W', '--Wprdt'):
                        profiledwelltime = arg
                        print('profile dwell-time:', profiledwelltime)
                        if attobj.check_deviceexists(dev):
                            attobj.set_profiledwelltime(dev, channel, profiledwelltime)
                        else:
                            print(f"Could not connect to device {dev}...")
                            sys.exit(2)

                    # Set Profile mode
                    elif opt in ('-O', '--Oprmd'):
                        profilemode = arg
                        print('profile mode:', profilemode)
                        if attobj.check_deviceexists(dev):
                            attobj.set_profilemode(dev, channel, profilemode)
                        else:
                            print(f"Could not connect to device {dev}...")
                            sys.exit(2)

                    # Set savesettings
                    elif opt in ('-S', '--Svst'):
                        print('Save Settings')
                        if attobj.check_deviceexists(dev):
                            attobj.set_savesettings(dev, channel)
                        else:
                            print(f"Could not connect to device {dev}...")
                            sys.exit(2)

                    # Set Profile File
                    elif opt in ('-F', '--Fprel'):
                        profilefilename = arg
                        print('profile Filename:', profilefilename)
                        if attobj.check_deviceexists(dev):
                            try:
                                profilefile = open(profilefilename, 'r')
                                count = 0
                                dwelltime = 0
                                idletime = 0
                                profilelength = 0
                                profileindex = 0
                                for linedata in profilefile.readlines():
                                    linedata = linedata.rstrip()
                                    if "dwell=" in linedata:
                                        dwelltime = linedata.split("dwell=", 1)[1]
                                        attobj.set_profiledwelltime(dev, channel, int(float(dwelltime) * 1000))
                                    elif "idle=" in linedata:
                                        idletime = linedata.split("idle=", 1)[1]
                                        attobj.set_profileidletime(dev, channel, int(float(idletime) * 1000))
                                    elif "length=" in linedata:
                                        profilelength = linedata.split("length=", 1)[1]
                                        attobj.set_profilecount(dev, channel, int(profilelength))
                                    else:
                                        attobj.set_profileelements(dev, channel, profileindex, linedata)
                                        profileindex = profileindex + 1
                                        sleep(0.05)  # delay 50msec
                            except Exception as err:
                                print(f"An error occurred while loading profile for device {dev}...")
                                print(err)
                                sys.exit(2)
                            print("Reading File Done")
                        else:
                            print(f"Could not connect to device {dev}...")
                            sys.exit(2)

            # Displays information about device
            if opt in ('-r', '--rdata'):
                if len(selected_devices) != 0:
                    for dev in selected_devices:
                        if attobj.check_deviceexists(dev):
                            try:
                                current_channels = []
                                if active_devices[dev] == 'a':
                                    for chnl in range(1, attobj.get_num_channels(dev) + 1):
                                        current_channels.append(chnl)
                                else:
                                    channel_list = active_devices[dev].split(':')
                                    for chnl in channel_list:
                                        if chnl != '':
                                            current_channels.append(int(chnl))

                                print("\n*****************Current Information of the device**********")
                                print("Device #:", dev)
                                print("Model Name:", attobj.get_modelname(dev))
                                print("Serial #:", attobj.get_serial_number(dev))
                                print("LDA DLL Version:", attobj.get_dllversion())
                                print("Min Frequency(MHz):", attobj.get_minfrequency(dev))
                                print("Max Frequency(MHz):", attobj.get_maxfrequency(dev))
                                print("Min Attenuation(dB):", attobj.get_minattenuation(dev))
                                print("Max Attenuation(dB):", attobj.get_maxattenuation(dev))
                                print("Num Channels:", attobj.get_num_channels(dev))

                                for chnl in current_channels:
                                    if chnl != '' and chnl != 'a' and 1 <= chnl <= attobj.get_num_channels(
                                            dev):
                                        print("\nChannel ", chnl, ':', sep='')
                                        print("\tFrequency(MHz):", attobj.get_currentfrequency(dev, chnl))
                                        print("\tAttenuation(dB):", attobj.get_currentattenuation(dev, chnl))
                                        print("\tRamp Start Attn(dB):", attobj.get_rampstart(dev, chnl))
                                        print("\tRamp End Attn(dB):", attobj.get_rampend(dev, chnl))
                                        print("\tDwell Time(ms):", attobj.get_dwelltime(dev, chnl))
                                        print("\tIdle Time(ms):", attobj.get_idletime(dev, chnl))
                                        print("\tHold Time:", attobj.get_holdtime(dev, chnl))
                                        print("\tBi-directional Dwell Time:",
                                              attobj.get_bidirectional_dwelltime(dev, chnl))
                                        print("\tProfile Count:", attobj.get_profilecount(dev, chnl))
                                        print("\tProfile Maxlength:", attobj.get_profilemaxlength(dev, chnl))
                                        print("\tProfile dwelltime(ms):", attobj.get_profiledwelltime(dev, chnl))
                                        print("\tProfile idletime(ms):", attobj.get_profileidletime(dev, chnl))
                                        print("\tProfile index:", attobj.get_profileindex(dev, chnl))
                                if len(current_channels) == 0:
                                    for chnl in range(1, attobj.get_num_channels(dev) + 1):
                                        print("\nChannel ", chnl, ':', sep='')
                                        print("\tFrequency(MHz):", attobj.get_currentfrequency(dev, chnl))
                                        print("\tAttenuation(dB):", attobj.get_currentattenuation(dev, chnl))
                                        print("\tRamp Start Attn(dB):", attobj.get_rampstart(dev, chnl))
                                        print("\tRamp End Attn(dB):", attobj.get_rampend(dev, chnl))
                                        print("\tDwell Time(ms):", attobj.get_dwelltime(dev, chnl))
                                        print("\tIdle Time(ms):", attobj.get_idletime(dev, chnl))
                                        print("\tHold Time:", attobj.get_holdtime(dev, chnl))
                                        print("\tBi-directional Dwell Time:",
                                              attobj.get_bidirectional_dwelltime(dev, chnl))
                                        print("\tProfile Count:", attobj.get_profilecount(dev, chnl))
                                        print("\tProfile Maxlength:", attobj.get_profilemaxlength(dev, chnl))
                                        print("\tProfile dwelltime(ms):", attobj.get_profiledwelltime(dev, chnl))
                                        print("\tProfile idletime(ms):", attobj.get_profileidletime(dev, chnl))
                                        print("\tProfile index:", attobj.get_profileindex(dev, chnl))
                            except Exception as err:
                                print(f"Exception raised while obtaining information on device {dev}...")
                                print(err)
                        else:
                            print(f"Could not connect to device {dev}...")
                elif len(attobj.devices_list) > 0:
                    devs = range(1, num_devices + 1)
                    for tmp_id in devs:
                        if tmp_id not in active_devices.keys():
                            try:
                                devnum = tmp_id
                                result = attobj.open_device(devnum)
                                if result != devnum:
                                    # some kind of error occurred, but error trapping was disabled
                                    print("Error opening the LDA device")
                                    sys.exit(2)
                            except:
                                print("Exception error opening the LDA device")
                                sys.exit(2)
                            else:
                                # the LDA device opened successfully, add its handle to the list of opened devices
                                opened_devices.append(devnum)
                                # add the channel list to the device if we only have 1 channel in this device
                                if attobj.get_num_channels(devnum) == 1:
                                    active_devices[devnum] = '1'
                                else:
                                    active_devices[devnum] = ''

                        print("\n*****************Current Information for the devices**********")
                        print("Device #:", tmp_id)
                        print("Model Name:", attobj.get_modelname(tmp_id))
                        print("Serial #:", attobj.get_serial_number(tmp_id))
                        print("LDA DLL Version:", attobj.get_dllversion())
                        print("Min Frequency(MHz):", attobj.get_minfrequency(tmp_id))
                        print("Max Frequency(MHz):", attobj.get_maxfrequency(tmp_id))
                        print("Min Attenuation(dB):", attobj.get_minattenuation(tmp_id))
                        print("Max Attenuation(dB):", attobj.get_maxattenuation(tmp_id))
                        print("Num Channels:", attobj.get_num_channels(tmp_id))
                        for chnl in range(1, attobj.get_num_channels(tmp_id) + 1):
                            print("\nChannel ", chnl, ":", sep='')
                            print("\tFrequency(MHz):", attobj.get_currentfrequency(tmp_id, chnl))
                            print("\tAttenuation(dB):", attobj.get_currentattenuation(tmp_id, chnl))
                            print("\tRamp Start Attn(dB):", attobj.get_rampstart(tmp_id, chnl))
                            print("\tRamp End Attn(dB):", attobj.get_rampend(tmp_id, chnl))
                            print("\tDwell Time(ms):", attobj.get_dwelltime(tmp_id, chnl))
                            print("\tIdle Time(ms):", attobj.get_idletime(tmp_id, chnl))
                            print("\tHold Time:", attobj.get_holdtime(tmp_id, chnl))
                            print("\tBi-directional Dwell Time:",
                                  attobj.get_bidirectional_dwelltime(tmp_id, chnl))
                            print("\tProfile Count:", attobj.get_profilecount(tmp_id, chnl))
                            print("\tProfile Maxlength:", attobj.get_profilemaxlength(tmp_id, chnl))
                            print("\tProfile dwelltime(ms):", attobj.get_profiledwelltime(tmp_id, chnl))
                            print("\tProfile idletime(ms):", attobj.get_profileidletime(tmp_id, chnl))
                            print("\tProfile index:", attobj.get_profileindex(tmp_id, chnl))

                else:
                    print("No Devices Connected...")
                print()

        # the loop over command line options has completed, close any devices we opened
        for devnum in opened_devices:
            try:
                result = attobj.close_device(devnum)
                if result != devnum:
                    print(f"Error closing device {devnum}")
            except:
                print(f"Exception error closing device {devnum}")
                continue
            else:
                print(f"Device {devnum} closed...")

        # we are done, exit successfully
        sys.exit(0)


if __name__ == '__main__':
    # sys.argv = [sys.argv[0], '-i', '1', '-r']
    # sys.argv = [sys.argv[0], '-i', '1', '-c', '2', '-a', '20', '-r']
    # sys.argv = [sys.argv[0], '-i', '1', '-c', '2', '-a', '20', '-r']
    # sys.argv = [sys.argv[0], '-i', '1', '-a', '50']
    # sys.argv = [sys.argv[0], '-i', 'a', '-c', '1', '-a', '20', '-r']
    # sys.argv = [sys.argv[0], '-r']
    # sys.argv = [sys.argv[0], '-a', '60', '-r']
    # sys.argv = [sys.argv[0], '-i', '1:2', '-c', '3:4', '-a', '40', '-i', '1', '-r']
    # sys.argv = [sys.argv[0], '-i', '1', '-c', '3:4:5:6', '-a', '60', '-r']
    # sys.argv = [sys.argv[0], '-i', 'a', '-r']
    # sys.argv = [sys.argv[0], '-i', '1:2', '-r']
    # sys.argv = [sys.argv[0]]
    # RD testing
    # sys.argv = [sys.argv[0], '-i', '2', '-c', '1', '-r']
    # sys.argv = [sys.argv[0], '-i', '1', '-a', '20', '-i', '2', '-a', '40', '-r']
    # sys.argv = [sys.argv[0], '-i', 'a', '-c', 'a', '-a', '30', '-r']
    # sys.argv = [sys.argv[0], '-i', '1', '-c', '1', '-i', '2', '-c', '1', '-a', '40', '-c', 'a', '-i', 'a', '-r']
    # sys.argv = [sys.argv[0], '-i', '1', '-c', 'a', '-a', '20', '-i', '2', '-c', '2', '-a', '40', '-i', 'a', '-r']
    # sys.argv = [sys.argv[0], '-i', '2:3', '-c', 'a', '-a', '20', '-r']
    # sys.argv = [sys.argv[0], '-i', '1', '-c', '1:2:3:4:5:6', '-i', '2', '-c', '4', '-a', '20', '-i', '1', '-a', '40', '-i', 'a', '-c', 'a', '-r']
    # sys.argv = [sys.argv[0], '-i', '20243', '-r']
    # sys.argv = [sys.argv[0], '-i', '29541:29202', '-c', '1:2:3', '-M', '2', '-r']
    # sys.argv = [sys.argv[0], '-i', '29541:29202', '-c', '1:2:3', '-M', '1', '-r']
    # sys.argv = [sys.argv[0], '-i', '29541:29202', '-c', '1:2:3', '-D', '1', '-M', '2', '-r']
    # sys.argv = [sys.argv[0], '-i', '1', '-c', '2', '-a', '200', '-r']
    # sys.argv = [sys.argv[0], '-h']
    # print(sys.argv[0] + ' sysargv[3]= ' + sys.argv[3])
    CLIVaunixAttn().main(sys.argv[1:])
