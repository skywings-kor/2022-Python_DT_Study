import csv
a=[[],[],[],[],[],[],[]]
with open('passby_data.csv','r')as f:
    reader = csv.DictReader(f)
    i=j=0
    for row in reader:
        a[i].append(row)
        j=j+1
        if(j%24==0):
            i=i+1

x_title=['']