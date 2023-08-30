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


class CodecComparator:
    #class starts here
    def compareFiles(self,list_of_record_files: List[str]):
        #func starts here
        analysis = []
        row = len(list_of_record_files)%2 + len(list_of_record_files)//2
        for count, file in enumerate(list_of_record_files):
            #start parsing files here
            df = pd.read_csv(r'' + file)
            print(df)
            print(df.loc[df['Drop?'] == 1])
            print('come check this')
            print(df.loc[df['Drop?'] == 1].loc[df['latency'] >0])
            #mean_l= df.loc[df['Drop?'] == 1].loc[df['latency'] >0].mean()
            mean_l= df.loc[df['Drop?'] == 1].loc[:, 'latency'].mean()
            mean_RSSI= df.loc[df['Drop?'] == 1].loc[:, 'RSSI'].mean()
            df2 = df.iloc[[0, -1]]
            no_of_dropouts = len(df[df['Drop?'] == 1])
            total_readings = len(df)
            total_duration = ((df2['TIMESTAMP'].iloc[-1] -df2['TIMESTAMP'].iloc[0]) /1000000000)/60
            dropout_per_min = (no_of_dropouts/total_duration)
            analysis.append({'name': file, 'latency_mean': mean_l, 'RSSI_mean': mean_RSSI, 'dropout_per_min': dropout_per_min})
        print(mean_l)
        print(mean_RSSI)
        print(analysis)
        keys = []
        values_latency = []
        values_RSSI = []
        values_dp = []
        for index in range(len(analysis)):
            for key in analysis[index]:
                if key == 'name':
                    keys.append(analysis[index]['name'])
                    values_latency.append(analysis[index]['latency_mean'])
                    values_RSSI.append(analysis[index]['RSSI_mean'])
                    values_dp.append(analysis[index]['dropout_per_min'])
     
        dict_plots = dict(zip(keys, values_latency))
        dict_plots_RSSI = dict(zip(keys, values_RSSI))
        dict_plots_dp = dict(zip(keys, values_dp))
        codecs = list(dict_plots.keys())
        values = list(dict_plots.values())
        values_RSSI = list(dict_plots_RSSI.values())
        values_dp = list(dict_plots_dp.values())
        fig = plt.figure(figsize = (10,5))
        #plt.subplot(row,3,1)
        #plt.bar(codecs, values, color = 'maroon', width = 0.4)
        #plt.xlabel("codecs")
        #plt.ylabel("avg dropout latency")
        #plt.title("avg dropout latency")
        plt.subplot(row,2,1)
        #latency/RSSI got switched fix this
        plt.bar(codecs, values_latency, color = 'orange', width = 0.4)
        plt.xlabel("codecs")
        plt.ylabel("avg dropout RSSI")
        plt.title("avg dropout RSSI")
        plt.subplot(row,2,2)
        plt.bar(codecs, values_dp, color = 'green', width = 0.4)
        plt.xlabel("codecs")
        plt.ylabel("dropout per min")
        plt.title("dropout per min  Comparison")
        return plt,fig







