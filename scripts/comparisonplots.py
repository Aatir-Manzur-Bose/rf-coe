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
from rfcoe.classes import codecomparator 

def main():
    parser = argparse.ArgumentParser(description=" RF CoE Data")
    parser.add_argument("-l", "--list", help="list of data file to use for comparison. list delimited by ,", type=str)
    args, leftovers = parser.parse_known_args()
    file_list = [str(item) for item in args.list.split(',')]
    cc = codecomparator.CodecComparator() 
    plt,fig=cc.compareFiles(file_list)
    fig.savefig('my_plot.png')
    plt.show()

if __name__ == '__main__':
    main()



