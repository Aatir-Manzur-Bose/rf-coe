from pypolycomm.core import *
from pypolycomm.devicemanager import DeviceManager, ExpectTimeout
import csv
from datetime import datetime
import time
import asyncio
import time as t
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import re
from rfcoe.classes.attenuator import Attenuator
import logging
import multiprocessing
import keyboard  # using module keyboard
import csv
from datetime import datetime
import time


def plot_cont(fun, xmax, dev_list, active_attn_devices, filename, fields, attobj):
    #
    x = []
    y = []
    y2 = []
    a1 = []
    a2 = []
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    with open(filename, 'a') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)

    def update(i):
        yi, y2i, attn1 = fun(dev_list, active_attn_devices, attobj)
        y.append(yi)
        y2.append(y2i)
        a1.append(attn1)
        # a2.append(attn2)
        # row = [yi, y2i, datetime.now()]
        # csvwriter.writerow(row)
        # x = range(len(y))
        x.append(i)
        ax.clear()
        ax.set_xlabel('Samples')
        ax.set_ylabel('Latency and RSSI')
        ax.set_title("Latency and RSSI plot")
        ax.plot(x, y, label='Latency')
        ax.plot(x, y2, label='RSSI')
        ax.legend(loc='best')
        # ax.plot(x, a1)
        # ax.plot(x, a2)
        print(i, ': ', yi)
        with open(filename, 'a') as csvfile:
            # creating a csv writer object
            print(time.time_ns())
            row = [yi, y2i, attn1, str(time.time_ns())]
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(row)

    a = anim.FuncAnimation(fig, update, interval=50)
    plt.show()


def getLatencyAndAttenuation_bad(dev_list, active_attn_devices, attobj):
    vals = []
    for dev in dev_list:
        try:
            result = dev.send_expect(DeviceMessageType.TAP, "aud.latency", ".*current:.*\d+")
            result2 = str(dev.send_expect(DeviceMessageType.TAP, "cor.bt rssi", ".*RSSI:.*\d+"))
            print(result2)
            latency = [int(s) for s in result.data.split() if s.isdigit()]
            regex = re.compile(r'[\+\-]?[0-9]+')
            rssi = [int(k) for k in regex.findall(result2)]
            print("Found response: {}".format(latency[0]))
            print("Found response: {}".format(rssi[0]))
            vals.append(latency[0])
            vals.append(rssi[0])
            # print("Filtered LAT: {}".format(lat[1]))

        except ExpectTimeout:
            print("Expect timed out")
    # TODO: get this dictionary iterator working
    # for attn, chnl in active_attn_devices.items():
    #    vals.append(attobj.get_currentattenuation(attn, chnl))
    attobj.open_device(2)
    # vals.append((int(attobj.get_currentattenuation(2, 1))))
    attobj.open_device(1)
    vals.append((int(attobj.get_currentattenuation(1, 1))))
    return tuple(vals)


def getLatencyAndAttenuation(dev_list, active_attn_devices, attobj):
    vals = []
    for dev in dev_list:
        try:
            print(
                "***************************************************************************dev found****************************************************")
            result = dev.send_expect(DeviceMessageType.TAP, "aud.stats 0", "[0-9]+(,[0-9]+)+")
            print("stat list {} *************************************".format(result))
            stat_list = str(result).split(",")
            print("stat list {} *************************************".format(stat_list))
            # vals.append(int(stat_list[1]))
            # vals.append(int(stat_list[2]))
            print("lat/rssi: {}".format(stat_list[1]))
            result = dev.send_expect(DeviceMessageType.TAP, "aud.latency", ".*current:.*\d+")
            result2 = str(dev.send_expect(DeviceMessageType.TAP, "cor.bt rssi", ".*RSSI:.*\d+"))
            print(result2)
            latency = [int(s) for s in result.data.split() if s.isdigit()]
            regex = re.compile(r'[\+\-]?[0-9]+')
            rssi = [int(k) for k in regex.findall(result2)]
            print("Found response: {}".format(latency[0]))
            print("Found response: {}".format(rssi[0]))
            vals.append(int(stat_list[1]))
            vals.append((int(stat_list[2])))
            # vals.append(latency[0])
            # vals.append(rssi[0])
            # print("Filtered LAT: {}".format(lat[1]))

        except ExpectTimeout:
            print("Expect timed out")
    # TODO: get this dictionary iterator working
    # for attn, chnl in active_attn_devices.items():
    #    vals.append(attobj.get_currentattenuation(attn, chnl))
    attobj.open_device(2)
    # vals.append((int(attobj.get_currentattenuation(2, 1))))
    attobj.open_device(1)
    vals.append((int(attobj.get_currentattenuation(1, 1))))
    return tuple(vals)


def telemetry():
    logging.getLogger().addHandler(logging.StreamHandler())
    logging.getLogger().setLevel(logging.DEBUG)
    currtime = time.strftime("%Y%m%d-%H%M%S")
    filename = "rf_coe_records" + currtime + ".csv"
    fields = ['latency', 'RSSI', 'attn1', 'TIMESTAMP']
    dev_manager = DeviceManager()
    dev_list = dev_manager.available_devices(count=1, timeout=20.0)
    attobj = Attenuator()
    num_devices = attobj.find_devices()
    if num_devices == 0:
        print("No Attenuation Devices Connected...")
    active_attn_devices = {}  # a dictionary where each integer key is a device number (in the user numbering space,
    # not a DLL handle)

    # the associated string value specifies the channels associated with the device, or is null if no channel selection
    # has occurred yet
    current_channels = []
    opened_devices = []  # a list of devices we opened, each entry is a device number
    # get all Open attenuation devices
    devs = range(num_devices)
    for tmp_id in devs:
        devnum = tmp_id
        if tmp_id not in active_attn_devices.keys():
            active_attn_devices[devnum] = ''
            # add the channel list to the device if we only have 1 channel in this device
            if attobj.get_num_channels(devnum) == 1:
                active_attn_devices[devnum] = '1'
            else:
                active_attn_devices[devnum] = ''
                # add this device to the list of selected devices

    plot_cont(getLatencyAndAttenuation, 10, dev_list, active_attn_devices, filename, fields, attobj)


def recordDropout():
    # func starts here
    last = 0

    fields = ['dropout', 'return', 'DROPOUT TIMESTAMP', 'RETURN TIMESTAMP']
    currtime = time.strftime("%Y%m%d-%H%M%S")
    filename = "rf_coe_dropout" + currtime + ".csv"
    with open(filename, 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
    counter = 0
    returns = 0
    while True:  # making a loop
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('d'):  # if key 'd' is pressed
                print('Recording Dropout!', flush=True)
                with open(filename, 'a') as csvfile:
                    # creating a csv writer object
                    counter += 1
                    row = [counter, " ", time.time_ns(), " "]
                    csvwriter = csv.writer(csvfile)
                    csvwriter.writerow(row)
                while keyboard.is_pressed('d'):
                    pass
            elif keyboard.is_pressed('r'):
                print("Audio Returned!", flush=True)
                with open(filename, 'a') as csvfile:
                    # creating a csv writer object
                    returns += 1
                    row = [" ", returns, " ", time.time_ns()]
                    csvwriter = csv.writer(csvfile)
                    csvwriter.writerow(row)
                while keyboard.is_pressed('r'):
                    pass
        except:
            break  # if user pressed a key other than the given key the loop will break


if __name__ == '__main__':
    p = multiprocessing.Process(target=telemetry, args=())
    p.start()
    p = multiprocessing.Process(target=recordDropout, args=())
    p.start()
