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
import datetime
from calendar import timegm
import argparse
from datetime import datetime

def main():
    list_of_files = glob.glob('mergedrf_coe_records*')  # * means all if need specific format then *.csv
    latest_merged_file = max(list_of_files, key=os.path.getmtime)
    print(latest_merged_file)
    list_of_files = glob.glob('rf_coe_records*')  # * means all if need specific format then *.csv
    latest_records_file = max(list_of_files, key=os.path.getmtime)
    parser = argparse.ArgumentParser(description=" RF CoE Data")
    parser.add_argument("--records")
    parser.add_argument("--merged")
    args, leftovers = parser.parse_known_args()
    if args.merged is not None:
        print("merged file has been set file: %s" % args.merged)
        latest_merged_file = args.drops
    if args.records is not None:
        latest_records_file = args.records
        print("records file has been set file: %s" % args.records)
    autoDetectDropouts(latest_merged_file, latest_records_file)



def autoDetectDropouts(latest_merged_file: str, latest_records_file: str):
    #func starts here
    df = pd.read_csv(r'' + latest_merged_file)
    X = df[['latency', 'RSSI']]
    result = ['Drop?']
    y = df[result]
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.20, random_state=42)
    logreg = LogisticRegression()
    logreg.fit(X_train,y_train)

    y_pred = logreg.predict(X_test)
    df = pd.read_csv(r'' + latest_records_file)
    data1 = pd.DataFrame(df, columns=['latency', 'RSSI', "attn1", 'TIMESTAMP'])
    print(data1)
    data_list1 = data1.values.tolist()
    features = ['latency', 'RSSI']
    new_X = df[features]
    new_Y = logreg.predict(new_X)
    fields = ['latency', 'RSSI', 'TIMESTAMP', 'Drop?']
    filename = 'autodetecteddrops_' + latest_records_file
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        for count, elm in enumerate(data_list1):
            if count < len(new_Y):

                row = [elm[0],elm[1],elm[3], new_Y[count]]
                csvwriter.writerow(row)
                
                

if __name__ == '__main__':
    main()



