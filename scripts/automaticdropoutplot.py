import pandas as pd
import matplotlib.pyplot as plt
import re
import time
import glob
import os
import numpy as np
import csv
import datetime
import argparse
from datetime import datetime


def main():
    list_of_files = glob.glob('autodetecteddrops_rf_coe_records*')  # * means all if need specific format then *.csv
    latest_auto_detected_dropouts_file = max(list_of_files, key=os.path.getmtime)
    print(latest_auto_detected_dropouts_file)
    parser = argparse.ArgumentParser(description=" RF CoE Data")
    parser.add_argument("--autodetectedrecords")
    args, leftovers = parser.parse_known_args()
    if args.autodetectedrecords is not None:
        latest_merged_file = args.autodetectedrecords
        print("records file has been set file: %s" % args.mergedrecords)
    autoRecordedDropouts(latest_auto_detected_dropouts_file)

def autoRecordedDropouts(latest_auto_detected_dropouts_file: str):
    #func starts here
    df1 = pd.read_csv(r'' + latest_auto_detected_dropouts_file)
    data1 = pd.DataFrame(df1, columns=['latency', 'RSSI', "TIMESTAMP", 'Drop?'])
    print(data1)
    data_list = data1.values.tolist()
    latency=[]
    RSSI=[]
    time=[]
    drop=[]

    for count, elm in enumerate(data_list):
        latency.append(elm[0])
        RSSI.append(elm[1])
        time.append(elm[2]/1e9)
        drop.append(elm[3])

    print(drop)
    fig = plt.figure()
    last_state = 0
    ax = fig.add_subplot(1, 2, 1)
    ax.plot(time, RSSI, label="RSSI",color='green')
    ax.plot(time, latency, label="Latency",color='black')
    for q in range(0,len(time)):
        #assuming dropouts and returns have the same length
        if (drop[q] == 1):
             print("drop marked")

             ax.axvspan(time[q], time[q+1], color='red', alpha=0.7)

    ax.set_xlabel("Time (seconds)")
    ax.legend(loc='best')
    plt.title("Latency and RSSI Plot with auto Marked Regions of Dropouts")
    plt.show()


if __name__ == '__main__':
    main()

