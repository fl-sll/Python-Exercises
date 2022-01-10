import csv
import pandas as pd
import matplotlib.pyplot as plt
import statistics as st

weekend = {}
weekday = {}
filename = 'activity.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)

    w = open("newActivity.csv","w")
    w.write(str (header[0]) + "," + str (header[1]) + ","+ str (header[2]))
    w.write("\n")

    n = 0 
    for row in reader :
        interval = int(row[2])
        if row[0] == "NA":
            row[0] = 0
            n += 1
        steps = row[0]
        time = pd.Timestamp(row[1])
        if time.dayofweek <5:
            row.append("weekday")
            weekday.setdefault(interval,[])
            weekday[interval].append(int(steps))
        else:
            row.append("weekend")
            weekend.setdefault(interval,[])
            weekend[interval].append(int(steps))

        w.write(str(row[0]))
        w.write(str (row[0]) + "," + str (row[1]) + ","+ str (row[2]) + "," + str (row[3]))
        w.write("\n")

    w.close()

    weekendlist = []
    for i in weekend.keys():
        weekendlist.append(st.mean(weekend.get(i)))
    
    weekdaylist = []
    for i in weekend.keys():
        weekdaylist.append(st.mean(weekday.get(i)))
        
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.title("5-minute intervals")
    plt.plot(weekendlist, c="blue")
    plt.plot(weekdaylist, c="red")
    plt.xlabel("5-minute Intervals")
    plt.ylabel("Average number of steps")
    plt.show()