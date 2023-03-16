import pandas as pd
import matplotlib.pyplot as plt
import re
import time
import glob
import os
import numpy as np

import argparse

latest_file = ''
parser = argparse.ArgumentParser(description=" RF CoE Data")
parser.add_argument("--records")
parser.add_argument("--drops")
args, leftovers = parser.parse_known_args()
if args.records is not None:
    print( "records file has been set (value is %s)" % args.records)
    latest_file = args.records
else: 
    list_of_files = glob.glob('rf_coe_records*')  # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getmtime)

latency = []
RSSI = []
fading = []
noise = []
tot_atten = []
seconds = []
time = []

df = pd.read_csv(r'' + latest_file)
# print(df)
df = df.dropna()
data = pd.DataFrame(df, columns=['latency', 'RSSI', 'attn1', 'attn2', "TIMESTAMP"])
data_list = data.values.tolist()

for i in data_list:
    latency_intval = (i[0])
    RSSI_intval = (i[1])
    fading_intval = (i[3])
    noise_intval = (i[2])
    seconds_intval = (i[4])
    latency.append(latency_intval)
    RSSI.append(RSSI_intval)
    fading.append(-1 * fading_intval)
    noise.append(noise_intval)
    seconds.append(seconds_intval)
#   tot_atten.append(fading_intval + noise_intval)

# print(seconds)
text = r'(\d+-\d+-\d+ (\d+):(\d+):(\d+).(\d+))'
pattern = re.compile(text)

def timeLine(seconds, time, pattern):
    first = 0
    for s in seconds:
        match = pattern.match(s)
        hours = 3600 * (int(match.group(2)))
        minutes = 60 * (int(match.group(3)))
        seconds = int(match.group(4))
        frax = float((int(match.group(5))) / 1000000)
        if (first == 0):
            first = hours + minutes + seconds + frax
        time.append(hours + minutes + seconds + frax - first)
timeLine(seconds,time,pattern)


dropouts = []
returns = []
seconds1 = []
seconds2 = []
time1 = []
time2 = []
if args.drops is not None:
    print("file has been set (value is %s)" % args.drops)
    latest_file = args.drops
else: 
    list_of_files = glob.glob('rf_coe_dropout*')  # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getmtime)

#df1 = pd.read_csv(r'C:\WearableTestUtils\WearableTestUtils\AttenuationUtils\rf_coe_dropout20230313-165835.csv')
df1 = pd.read_csv(r'' + latest_file)
print(df1)
data1 = pd.DataFrame(df1, columns=['dropout', 'return', "DROPOUT TIMESTAMP", 'RETURN TIMESTAMP'])
data_list1 = data1.values.tolist()

for i1 in data_list1:
    if (i1[0] != " "):
        dropouts_intval = (i1[0])
        dropouts.append(dropouts_intval)
    if (i1[1] != " "):
        returns_intval = (i1[1])
        returns.append(returns_intval)
    if (i1[2] != " "):
        seconds1_intval = (i1[2])
        seconds1.append(seconds1_intval)
    if (i1[3] == i1[3] and i1[3] != " "):
        seconds2_intval = (i1[3])
        seconds2.append(seconds2_intval)

text = r'(\d+-\d+-\d+ (\d+):(\d+):(\d+).(\d+))'
pattern = re.compile(text)

timeLine(seconds1,time1,pattern)
timeLine(seconds2,time2,pattern)

tarr = np.asarray(time)
rssiarr = np.asarray(RSSI)
fadarr = np.asarray(fading)
for b in time1:
    i = (np.abs(tarr - b)).argmin()
    print("Time (seconds), RSSI (dB), Fading (dB): " + str((tarr[i],rssiarr[i],fadarr[i])))



fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(time, RSSI, label="RSSI")
ax.plot(time, latency, label="Latency")
ax.plot(time, fading, label="fading")
for q in range(0,min(len(dropouts), len(returns), len(time1), len(time2))): #assuming dropouts and returns have the same length
    ax.axvspan(time1[q],time2[q],color='red',alpha=0.3)
    if (q > 0):
        ax.axvspan(time2[q - 1],time1[q],color='green',alpha=0.3)
    else:
        ax.axvspan(0, time1[q], color='green', alpha=0.3)
ax.axvspan(time2[q], time[-1], color='green', alpha=0.3)
ax.set_xlabel("Time (seconds")
ax.legend(loc='best')
plt.title("")
plt.show()
