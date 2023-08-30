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
    parser = argparse.ArgumentParser(description=" RF CoE Data")
    parser.add_argument("--merged")
    args, leftovers = parser.parse_known_args()
    if args.merged is not None:
        print("merged file has been set file: %s" % args.merged)
        latest_merged_file = args.drops
    dropoutRate(latest_merged_file)



def dropoutRate(latest_merged_file: str):
    #func starts here
    df = pd.read_csv(r'' + latest_merged_file)
    df2 = df.iloc[[0, -1]]
    print("number of dropouts: %d" %len(df[df['Drop?'] == 1]))
    no_of_dropouts = len(df[df['Drop?'] == 1])
    total_readings = len(df)
    total_duration = df2['TIMESTAMP'].iloc[-1] - df2['TIMESTAMP'].iloc[0]
    print("total duration: %d" %total_duration)
    print("Dropout percentage: %.2f" %((no_of_dropouts/total_readings)*100))
    print("Dropout rate dropouts per second: %.2f" %((no_of_dropouts/total_duration)))
    
                

if __name__ == '__main__':
    main()




