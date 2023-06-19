from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd
import glob
import os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
import re
import csv
#from main import fig
fig = plt.figure()

df = pd.read_csv(r'masterfilerf_coe_dropout20230618-002613.csv')
df = df.dropna()
data = pd.DataFrame(df, columns=['latency', 'RSSI', "TIMESTAMP", "Drop?"])

features = ['latency', 'RSSI']
result = ["Drop?"]
X = data[features]
Y = data[result]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=16)
logreg = LogisticRegression(random_state=16)
logreg.fit(X, Y)
predicted_drops = logreg.predict(X)
coefficients = logreg.coef_[0]
print(coefficients)
Y_pred = logreg.predict(X_test)

confusion_matrix = metrics.confusion_matrix(Y_test, Y_pred)
print(confusion_matrix)

class_names = [0, 1]  # name  of classes
fig1, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)
# create heatmap
sns.heatmap(pd.DataFrame(confusion_matrix), annot=True, cmap="YlGnBu", fmt='g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion matrix', y=1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')

target_names = ['Non-Dropout Samples', 'Dropout Samples']
print(classification_report(Y_test, Y_pred, target_names=target_names))

# fig = plt.figure()
# ax = fig.add_subplot(1,2,1)
# ax.plot(seconds, RSSI, label="RSSI",color='green')
# ax.plot(seconds, latency, label="Latency",color='black')
# ax.plot(seconds,filt_latency,label='Filtered Latency',color='blue')
# for i in range(0,len(seconds)):
#     if (dropouts[i] == 1):
#         ax.axvspan(seconds[i], seconds[i+1], color='red', alpha=0.7)
#
# ax = fig.add_subplot(1,2,2)
# ax.plot(seconds, RSSI, label="RSSI",color='green')
# ax.plot(seconds, latency, label="Latency",color='black')
# ax.plot(seconds,filt_latency,label='Filtered Latency',color='blue')
# ax.legend(loc='best')
# for i in range(0,len(seconds)):
#     if (predicted_drops[i] == 1):
#         ax.axvspan(seconds[i], seconds[i+1], color='red', alpha=0.7)

# fig = plt.figure()
list_of_files = glob.glob('masterfile*')  # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getmtime)
df = pd.read_csv(r'' + latest_file)
df = df.dropna()
data = pd.DataFrame(df, columns=['latency', 'RSSI', "TIMESTAMP", "Drop?"])
data_list = data.values.tolist()

features = ['latency', 'RSSI']
new_X = data[features]
new_Y = logreg.predict(new_X)

# ax = fig.add_subplot(1,2,1)
# ax.plot(seconds, RSSI, label="RSSI",color='green')
# ax.plot(seconds, latency, label="Latency",color='black')
# ax.plot(seconds,filt_latency,label='Filtered Latency',color='blue')
# for i in range(0,len(seconds)):
#     if (dropouts[i] == 1):
#         ax.axvspan(seconds[i], seconds[i+1], color='red', alpha=0.7)

latency = []
RSSI = []
dropouts = []
# filt_latency = []
seconds = []

for i in data_list:
    latency_intval = (i[0])
    # filt_latency_intval = (i[2])
    RSSI_intval = (i[1])
    seconds_intval = (i[2])
    dropouts_intval = i[3]
    latency.append(latency_intval)
    RSSI.append(RSSI_intval)
    seconds.append(seconds_intval)
    # filt_latency.append(filt_latency_intval)
    dropouts.append(dropouts_intval)

fields = ['latency', 'RSSI', "TIMESTAMP", "Predicted Drops"]
filename = "resultfile_" + latest_file
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    for a in range(0, len(new_Y)):
        row = [latency[a], RSSI[a], seconds[a], new_Y[a]]
        csvwriter.writerow(row)

ax = fig.add_subplot(1, 2, 2)
ax.plot(seconds, RSSI, label="RSSI", color='green')
ax.plot(seconds, latency, label="Latency", color='black')
# ax.plot(seconds,filt_latency,label='Filtered Latency',color='blue')
ax.legend(loc='best')
for i in range(0, len(seconds) - 1):
    if (new_Y[i] == 1):
        ax.axvspan(seconds[i], seconds[i + 1], color='red', alpha=0.7)
ax.set_xlabel("Time (seconds)")
ax.legend(loc='best')
plt.title("Latency and RSSI Plot with Manually Marked Regions of Dropouts")

plt.show()

dropout_number = 0
drop_len = 0
add = 0
dropouts_list = []
drop_RSSI = []

for r in range(1, len(new_Y)):
    if (new_Y[r] - new_Y[r - 1] == 1):
        dropout_number += 1
        drop_RSSI.append(RSSI[r])
    elif (new_Y[r] - new_Y[r - 1] == 0):
        if (new_Y[r] == 1):
            drop_len += 1
    else:
        add += drop_len
        dropouts_list.append(drop_len)
        drop_len = 0

print("# of Dropouts = {}".format(dropout_number))
print("Dropouts/Minute = {}".format(60 * dropout_number / seconds[-1]))
print("Average Dropout Length = {} samples".format(add / dropout_number))

drop_dist = np.asarray(dropouts_list)
median = np.median(drop_dist)
std = np.std(drop_dist)
print("Median = {}, St. Dev. = {}".format(median, std))

plt.figure()
plt.hist(drop_dist)
plt.xlabel('Dropout Length (Samples)')
plt.ylabel('Frequency')
plt.title('Histogram of Dropout Lengths')

drp_RSSI = np.asarray(drop_RSSI)
median_RSSI = np.median(drp_RSSI)
mean_RSSI = np.mean(drp_RSSI)
std_RSSI = np.std(drp_RSSI)
print("Average Dropout RSSI = {}".format(mean_RSSI))
print("Median = {}, St. Dev. = {}".format(median_RSSI, std_RSSI))

# fields = ['Fading Period (ms)', 'Drops/Min', "Avg. Drop Length (sps)", "Median Drop Length (ss)", "Standard Dev. (sps)", "Ag. Drop RSSI (dB)", "Median Drop RSSI (dB)", "Standard Dev. (dB)"]
# filename = "RFCoE_Data.csv"
# with open(filename, 'a') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     # csvwriter.writerow(fields)
#     row = [0,60 * dropout_number / seconds[-1], add / dropout_number, median, std, mean_RSSI, median_RSSI, std_RSSI]
#     csvwriter.writerow(row)

plt.figure()
plt.hist(drp_RSSI)
plt.xlabel('RSSI at Dropout (dB)')
plt.ylabel('Frequency')
plt.title('Histogram of Dropout RSSI Values')

plt.show()
