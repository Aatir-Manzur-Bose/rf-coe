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
from typing import List, Dict

def main():
    parser = argparse.ArgumentParser(description=" RF CoE Data")
    parser.add_argument("-l", "--list", help="list of data file to use for comparison. list delimited by ,", type=str)
    args, leftovers = parser.parse_known_args()
    file_list = [str(item) for item in args.list.split(',')]
    compareFiles(file_list)


def compareFiles(list_of_record_files: List[str]) -> List[Dict]:
    analysis = []
    row = len(list_of_record_files)%2 + len(list_of_record_files)//2
    for count, file in enumerate(list_of_record_files):
        #start parsing files here
        df = pd.read_csv(r'' + file)
        print(df)
        print(df.loc[df['Drop?'] == 1])
        mean_l= df.loc[df['Drop?'] == 1].loc[:, 'latency'].mean()
        mean_RSSI= df.loc[df['Drop?'] == 1].loc[:, 'RSSI'].mean()
        analysis.append({'name': file, 'latency_mean': mean_l, 'RSSI_mean': mean_RSSI})
        print(mean_l)
        print(mean_RSSI)
    print(analysis)
    keys = []
    values_latency = []
    values_RSSI = []
    for index in range(len(analysis)):
        for key in analysis[index]:
            if key == 'name':
                keys.append(analysis[index]['name'])
                values_latency.append(analysis[index]['latency_mean'])
                values_RSSI.append(analysis[index]['RSSI_mean'])
     
    dict_plots = dict(zip(keys, values_latency))
    dict_plots_RSSI = dict(zip(keys, values_RSSI))
    codecs = list(dict_plots.keys())
    values = list(dict_plots.values())
    values_RSSI = list(dict_plots_RSSI.values())
    fig = plt.figure(figsize = (10,5))
    plt.subplot(row,2,1)
    plt.bar(codecs, values, color = 'maroon', width = 0.4)
    plt.xlabel("codecs")
    plt.ylabel("average dropout Latency")
    plt.title("avg Latency at dropout Comparison")
    plt.subplot(row,2,2)
    plt.bar(codecs, values_RSSI, color = 'orange', width = 0.4)
    plt.xlabel("codecs")
    plt.ylabel("average dropout RSSI")
    plt.title("avg RSSI at dropout Comparison")

    plt.show()
    print(dict_plots)


if __name__ == '__main__':
    main()



