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
    list_of_files = glob.glob('rf_coe_dropout*')  # * means all if need specific format then *.csv
    latest_drops_file = max(list_of_files, key=os.path.getmtime)
    print(latest_drops_file)
    list_of_files = glob.glob('rf_coe_records*')  # * means all if need specific format then *.csv
    latest_records_file = max(list_of_files, key=os.path.getmtime)
    parser = argparse.ArgumentParser(description=" RF CoE Data")
    parser.add_argument("--records")
    parser.add_argument("--drops")
    args, leftovers = parser.parse_known_args()
    if args.drops is not None:
        print("droput file has been set file: %s" % args.drops)
        latest_drops_file = args.drops
    if args.records is not None:
        latest_records_file = args.records
        print("records file has been set file: %s" % args.records)
    mergeDropoutsAndRecordsFile(latest_records_file, latest_drops_file)



def dropoutStartAndEndTimes(latest_drops_file: str):
    #func starts here
    dropout_start_time_arr = []
    dropout_end_time_arr = []
    df1 = pd.read_csv(r'' + latest_drops_file)
    data1 = pd.DataFrame(df1, columns=['dropout', 'return', "DROPOUT TIMESTAMP", 'RETURN TIMESTAMP'])
    print(data1)
    data_list1 = data1.values.tolist()
    #print(data_list1)
    print(len(data_list1))
    for i1 in data_list1:
        #for starts here
        if (i1[0] != " "):
            print("found dropout")
            print("value  %s" % (i1[2]))
            dropout_start_time_arr.append((i1[2]))
        if (i1[1] != " "):
            print("found return")
            dropout_end_time_arr.append((i1[3]))
    return dropout_start_time_arr , dropout_end_time_arr

def mergeDropoutsAndRecordsFile(latest_records_file: str, latest_drops_file: str):
    df1 = pd.read_csv(r'' + latest_records_file)
    print(df1)
    data1 = pd.DataFrame(df1, columns=['latency', 'RSSI', 'attn1', "TIMESTAMP"])
    data_list1 = data1.values.tolist()
    drops = []
    dropout_start_time_arr, dropout_end_time_arr = dropoutStartAndEndTimes(latest_drops_file)
    for count, i1 in enumerate(data_list1):
        for i in range (0, max(len(dropout_start_time_arr), len(dropout_end_time_arr))):
            drops.append(0)
            #timestamp: 1687101808292378000, 
            #start:     1687101808071341400, 
            #end        1687101808412351000
            #droput merged!

            if (float(i1[3]) >= float(dropout_start_time_arr[i]) and float(i1[3])<= float(dropout_end_time_arr[i])):
                print("timestamp: %s, start: %s, end %s" % (i1[3], dropout_start_time_arr[i],  dropout_end_time_arr[i]))
                print("droput merged!")
                drops[count]=1
    fields = ['latency', 'RSSI', 'TIMESTAMP', 'Drop?']
    filename = 'merged' + latest_records_file
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        for count, elm in enumerate(data_list1):
            if count < len(drops):

                row = [elm[0],elm[1],elm[3], drops[count]]
                csvwriter.writerow(row)
            else:
                row = [elm[0], elm[1], elm[3], 0]
                csvwriter.writerow(row)
                

if __name__ == '__main__':
    main()


