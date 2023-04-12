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

list_of_files = glob.glob('masterfile*')  # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getmtime)

df = pd.read_csv(r'' + latest_file)
# print(df)
df = df.dropna()
data = pd.DataFrame(df, columns=['latency', 'RSSI', 'filtered latency', "TIMESTAMP", "Drop?"])
data_list = data.values.tolist()

features = ['latency', 'RSSI', 'filtered latency']
result = ["Drop?"]
X = data[features]
Y = data[result]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=16)
logreg = LogisticRegression(random_state=16)
logreg.fit(X_train, Y_train)
coefficients = logreg.coef_[0]
print(coefficients)
Y_pred = logreg.predict(X_test)

confusion_matrix = metrics.confusion_matrix(Y_test,Y_pred)
print(confusion_matrix)

class_names=[0,1] # name  of classes
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)
# create heatmap
sns.heatmap(pd.DataFrame(confusion_matrix), annot=True, cmap="YlGnBu" ,fmt='g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion matrix', y=1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')

target_names = ['Non-Dropout Samples', 'Dropout Samples']
print(classification_report(Y_test, Y_pred, target_names=target_names))

latency = []
RSSI = []
dropouts = []
filt_latency = []
seconds = []

for i in data_list:
    latency_intval = (i[0])
    filt_latency_intval = (i[2])
    RSSI_intval = (i[1])
    seconds_intval = (i[3])
    dropouts_intval = i[4]
    latency.append(latency_intval)
    RSSI.append(RSSI_intval)
    seconds.append(seconds_intval)
    filt_latency.append(filt_latency_intval)
    dropouts.append(dropouts_intval)

plt.figure()
plt.plot(seconds,latency)


plt.show()