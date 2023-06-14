from __future__ import annotations
import ctypes
import os
from ctypes import *
import threading
import time

from rfcoe.constants.attenuator import *
from .ldaerror import LDAError


class Attenuator:

    def __init__(self, name="ldaApi", port=''):
        os.add_dll_directory(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'ddls')))
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
        def __init__(self, increment: int, attn: Attenuator):
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
