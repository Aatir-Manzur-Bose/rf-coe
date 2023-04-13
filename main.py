import pandas as pd
import matplotlib.pyplot as plt
import re
import time
import glob
import os
import numpy as np
import csv
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
from sklearn.model_selection import train_test_split
from sklearn import metrics
import seaborn as sns
from sklearn.metrics import classification_report
import argparse

latest_file = ''
parser = argparse.ArgumentParser(description=" RF CoE Data")
parser.add_argument("--records")
parser.add_argument("--drops")
args, leftovers = parser.parse_known_args()
if args.records is not None:
    print( "records file has been set (value is %s)" % args.records)
    latest_file = args.records
    print(latest_file)
else: 
    list_of_files = glob.glob('rf_coe_records*')  # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getmtime)
    print(latest_file)
latency = []
filt_latency = []
RSSI = []
fading = []
noise = []
tot_atten = []
seconds = []
time = []

df = pd.read_csv(r'' + latest_file)
# print(df)
df = df.dropna()
data = pd.DataFrame(df, columns=['latency', 'RSSI', 'filtered latency', 'attn1', 'attn2', "TIMESTAMP"])
# print(data)
data_list = data.values.tolist()

for i in data_list:
    latency_intval = (i[0])
    filt_latency_intval = (i[2])
    RSSI_intval = (i[1])
    fading_intval = (i[4])
    noise_intval = (i[3])
    seconds_intval = (i[5])
    latency.append(latency_intval)
    RSSI.append(RSSI_intval)
    fading.append(-1 * fading_intval)
    noise.append(noise_intval)
    seconds.append(seconds_intval)
    filt_latency.append(filt_latency_intval)


text = r'(\d+-\d+-\d+ (\d+):(\d+):(\d+).(\d+))'
pattern = re.compile(text)

def timeLine(seconds, time, pattern):
    first = 0
    for s in seconds:
        match = pattern.match(s)
        hours = 3600 * (int(match.group(2)))
        minutes = 60 * (int(match.group(3)))
        secondsq = int(match.group(4))
        frax = float((int(match.group(5))) / 1000000)
        if (first == 0):
            first = hours + minutes + secondsq + frax
        time.append(hours + minutes + secondsq + frax - first)
    return(first)

def derivative(x,t):
    derv = []
    for d in range(1,len(x)):
        dx = x[d] - x[d-1]
        dt = t[d] - t[d-1]
        derv.append(dx / dt)
    return derv
#no more index searching -- implement for loop in here, have it go by steps of 1

firstTime = timeLine(seconds,time,pattern)

dropouts = []
dropout_list = []
returns = []
seconds1 = []
seconds2 = []
time1 = [] #timestamps corresponding to dropouts
time2 = [] #timestamps corresponding to returns

if args.drops is not None:
    print("file has been set (value is %s)" % args.drops)
    latest_file = args.drops
else: 
    list_of_files = glob.glob('rf_coe_dropout*')  # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getmtime)

df1 = pd.read_csv(r'' + latest_file)
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

firstTime1 = timeLine(seconds1,time1,pattern)
firstTime2 = timeLine(seconds2,time2,pattern)


offset1 = firstTime1 - firstTime #calculates the offset in time between dropout.py and RFLatency.py
offset2 = firstTime2 - firstTime #calculates the offset between the first dropout and first return
for i in range(0,len(time1)):
    time1[i] = time1[i] + offset1
for i in range(0,len(time2)):
    time2[i] = time2[i] + offset2

tarr = np.asarray(time)
rssiarr = np.asarray(RSSI)
fadarr = np.asarray(fading)

for ct in range(0, len(time1)):
    for q in range(0,len(time)): #assuming dropouts and returns have the same length
        if (time[q] >= time1[ct] and time[q] < time2[ct]):
            dropout_list.append(1)
        else:
            dropout_list.append(0)
    if (ct == 0):
        master = dropout_list
    else:
        for i in range(0,len(time)):
            master[i] = master[i] + dropout_list[i]
    dropout_list = []

fields = ['latency', 'RSSI', 'filtered latency', "TIMESTAMP", "Drop?"]
filename = "masterfile" + latest_file
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    for a in range(0,len(time)):
        row = [latency[a],RSSI[a],filt_latency[a],time[a],master[a]]
        csvwriter.writerow(row)


derivlist = derivative(latency,time)
filtderivlist = derivative(filt_latency,time)

tot_list = []
auto_dropouts = []
auto_dropouts_time = []
rssi_drops = []
autdrop = []
autdroptime = []
derivcheck = []
rssiauto = []

last = 0
for r in range(1,len(latency)-1):
    if (abs(derivlist[r]) > 200):
        rssi_drops.append(RSSI[r])
        auto_dropouts.append(derivlist[r])
        auto_dropouts_time.append(time[r])
    if (abs(filtderivlist[r] > 910)):
        # print("At t = {}, Lat_Der = {} and Filt_Late_Der = {}".format(time[r],derivlist[r],filtderivlist[r]))
        autdrop.append(filtderivlist[r])
        autdroptime.append(time[r])
        derivcheck.append(derivlist[r])
        rssiauto.append(RSSI[r])

fig = plt.figure()
last_state = 0
ax = fig.add_subplot(1, 2, 1)
ax.plot(time, RSSI, label="RSSI",color='green')
ax.plot(time, latency, label="Latency",color='black')
ax.plot(time,filt_latency,label='Filtered Latency',color='blue')
for q in range(0,len(time)): #assuming dropouts and returns have the same length
    if (master[q] == 1):
        ax.axvspan(time[q], time[q+1], color='red', alpha=0.7)

ax.set_xlabel("Time (seconds)")
ax.legend(loc='best')
plt.title("Latency and RSSI Plot with Manually Marked Regions of Dropouts")


