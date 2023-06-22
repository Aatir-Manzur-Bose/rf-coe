import keyboard  # using module keyboard
import csv
from datetime import datetime
import time

fields = ['dropout', 'TIMESTAMP']
currtime = time.strftime("%Y%m%d-%H%M%S")
filename = "rf_coe_dropout" + currtime + ".csv"
counter = 0
with open(filename, 'a') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
while True:
    keyboard.wait('space')
    print('space was pressed! Waiting on it again...')
    counter += 1
    with open(filename, 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        row = [counter, datetime.now()]
        csvwriter.writerow(row)
