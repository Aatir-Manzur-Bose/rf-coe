import keyboard  # using module keyboard
import csv
from datetime import datetime
import time

last = 0

fields = ['dropout', 'return', 'DROPOUT TIMESTAMP', 'RETURN TIMESTAMP']
currtime = time.strftime("%Y%m%d-%H%M%S")
filename = "rf_coe_dropout" + currtime + ".csv"
with open(filename, 'a') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
counter = 0
returns = 0
while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('d'):  # if key 'd' is pressed
            print('Recording Dropout!')
            with open(filename, 'a') as csvfile:
                # creating a csv writer object
                counter += 1
                row = [counter, " ", datetime.now(), " "]
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(row)
            while keyboard.is_pressed('d'):
                pass
        elif keyboard.is_pressed('r'):
            print("Audio Returned!")
            with open(filename, 'a') as csvfile:
                # creating a csv writer object
                returns += 1
                row = [" ", returns, " ", datetime.now()]
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(row)
            while keyboard.is_pressed('r'):
                pass
    except:
        break  # if user pressed a key other than the given key the loop will break
