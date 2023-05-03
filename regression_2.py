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
from main_2 import fig


df = pd.read_csv(r'masterfilerf_coe_dropout20230413-145948.csv')
df = df.dropna()
data = pd.DataFrame(df, columns=['latency', 'RSSI', 'filtered latency', "TIMESTAMP", "Drop?"])

features = ['RSSI']
result = ["Drop?"]
X = data[features]
Y = data[result]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=16)
logreg = LogisticRegression(random_state=16)
logreg.fit(X_train, Y_train)
predicted_drops = logreg.predict(X_test)

# coefficients = logreg.coef_[0]
# print(coefficients)
# Y_pred = logreg.predict(X_test)
#
# confusion_matrix = metrics.confusion_matrix(Y_test,Y_pred)
# print(confusion_matrix)
#
# class_names=[0,1] # name  of classes
# fig1, ax = plt.subplots()
# tick_marks = np.arange(len(class_names))
# plt.xticks(tick_marks, class_names)
# plt.yticks(tick_marks, class_names)
# # create heatmap
# sns.heatmap(pd.DataFrame(confusion_matrix), annot=True, cmap="YlGnBu" ,fmt='g')
# ax.xaxis.set_label_position("top")
# plt.tight_layout()
# plt.title('Confusion matrix', y=1.1)
# plt.ylabel('Actual label')
# plt.xlabel('Predicted label')
#
# target_names = ['Non-Dropout Samples', 'Dropout Samples']
# print(classification_report(Y_test, Y_pred, target_names=target_names))

list_of_files = glob.glob('masterfile*')  # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getmtime)
# print(latest_file)
df = pd.read_csv(r'' + latest_file)
df = df.dropna()
data = pd.DataFrame(df, columns=['latency', 'RSSI', 'filtered latency', "TIMESTAMP", "Drop?"])
# print(data)
data_list = data.values.tolist()

features = ['RSSI']
new_X = data[features]
# print(new_X)
new_Y = logreg.predict(new_X)

dropout_number = 0

for r in range(1,len(new_Y)):
    if (new_Y[r] - new_Y[r-1]):
        dropout_number += 1

RSSI = []
dropouts = []
seconds = []

for i in data_list:
    RSSI_intval = (i[1])
    seconds_intval = (i[3])
    dropouts_intval = i[4]
    RSSI.append(RSSI_intval)
    seconds.append(seconds_intval)
    dropouts.append(dropouts_intval)

# fig = plt.figure()
ax = fig.add_subplot(1,2,2)
ax.plot(seconds, RSSI, label="RSSI",color='green')
ax.legend(loc='best')
for i in range(0,len(seconds) - 1):
    if (new_Y[i] == 1):
        ax.axvspan(seconds[i], seconds[i+1], color='red', alpha=0.7)
ax.set_xlabel("Time (seconds)")
ax.legend(loc='best')
plt.title("Latency and RSSI Plot with Automatically Marked Regions of Dropouts")

plt.show()

dropout_number = 0
drop_len = 0
add = 0
dropouts_list = []

for r in range(1,len(new_Y)):
    if (new_Y[r] - new_Y[r-1] == 1):
        dropout_number += 1
    elif (new_Y[r] - new_Y[r-1] == 0):
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
plt.figure()
plt.hist(drop_dist)
plt.xlabel('Dropout Length (Samples)')
plt.ylabel('Frequency')
plt.title('Histogram of Dropout Lengths')

plt.show()
