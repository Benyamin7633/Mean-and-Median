import csv
from statistics import median
with open("HeightWeight.csv", newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
newlist = []
for i in range(len(file_data)):
    n_num = file_data[i][1]
    newlist.append(n_num)

n = len(newlist)
newlist.sort()
if n % 2 == 0:
    median1 = float(newlist[n//2])
    median2 = float(newlist[n//2-1])
    median = (median1+median2)/2
else:
    median = newlist[n//2]

print("the median is "+ str(median))