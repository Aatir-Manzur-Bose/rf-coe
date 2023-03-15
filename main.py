import pandas as pd
import matplotlib.pyplot as plt
import re
import time
import glob
import os

list_of_files = glob.glob('rf_coe_records*')  # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getmtime)

latency = []
RSSI = []
fading = []
noise = []
time = []
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
    fading.append(fading_intval)
    noise.append(noise_intval)
    seconds.append(seconds_intval)
#   tot_atten.append(fading_intval + noise_intval)

# print(seconds)
text = r'(\d+-\d+-\d+ (\d+):(\d+):(\d+).(\d+))'
pattern = re.compile(text)

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

#
# plt.figure(1)
# plt.plot(time, latency)
# plt.title("Latency vs Time")
# plt.ylabel("Latency (Buffer Size)")
# plt.xlabel("Time (Seconds)")
#
# plt.figure(2)
# plt.plot(time, RSSI)
# plt.title("RSSI vs Time")
# plt.ylabel("RSSI (dB)")
# plt.xlabel("Time (Seconds)")
#
# plt.figure(3)
# plt.plot(time,fading)
# plt.title("Fading vs Time")
# plt.ylabel("Fading (dB)")
# plt.xlabel("Time (Seconds)")
#
# plt.figure(4)
# plt.scatter(RSSI,latency)
# plt.title("Latency vs RSSI")
# plt.ylabel("Latency (Buffer Size)")
# plt.xlabel("RSSI (dB)")
#
# plt.figure(5)
# plt.plot(time, latency)
# plt.plot(time, RSSI)
#
# # plt.figure(5)
# # plt.plot(time, latency)
# # plt.plot(time, fading)
#
# fig = plt.figure(figsize=(12,12))
# ax = fig.add_subplot(projection='3d')
# ax.scatter(time,fading,latency)
# ax.set_zlabel("Latency (Buffer Size)")
# ax.set_xlabel("Time (seconds)")
# ax.set_ylabel("Fading (dB)")
#

dropouts = []
seconds1 = []
time1 = []

df1 = pd.read_csv(r'C:\WearableTestUtils\WearableTestUtils\AttenuationUtils\rf_coe_dropout20230313-165835.csv')
print(df1)
df1 = df1.dropna()
data1 = pd.DataFrame(df1, columns=['dropout', "TIMESTAMP"])
data_list1 = data1.values.tolist()

for i1 in data_list1:
    dropouts_intval = (i1[0])
    seconds1_intval = (i1[1])
    dropouts.append(dropouts_intval)
    seconds1.append(seconds1_intval)

text = r'(\d+-\d+-\d+ (\d+):(\d+):(\d+).(\d+))'
pattern = re.compile(text)
first = 0
for s in seconds1:
    match = pattern.match(s)
    hours = 3600 * (int(match.group(2)))
    minutes = 60 * (int(match.group(3)))
    seconds = int(match.group(4))
    frax = float((int(match.group(5))) / 1000000)
    if (first == 0):
        first = hours + minutes + seconds + frax
    time1.append(hours + minutes + seconds + frax - first)

print(time1)
print(dropouts)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(time1, dropouts, label="dropouts")
ax.plot(time, RSSI, label="RSSI")
ax.plot(time, latency, label="Latency")
ax.plot(time, fading, label="fading")
ax.set_xlabel("Time (seconds")
ax.legend(loc='best')
plt.show()
