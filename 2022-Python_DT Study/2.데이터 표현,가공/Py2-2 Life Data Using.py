import pandas as pd
#import csv
a=[[],[],[],[],[],[],[]]

def LoadCsvFile(file_name):
    data=pd.read_csv(file_name,header=None)
    
    data[0]=data[0].str.replace('','')
    datasize=range(len(data))
    for i in range(len(data)):
        for j in data.iloc[i]:
            if isinstance(j,str):
                j=j.replace('','')
    return data

print('file1 읽기 결과')
data1=LoadCsvFile("passby_data.csv")
print(data1)

#    i=j=0
#    for row in data:
#        a[i].append(row)
#        j=j+1
#        if(j%24==0):
#            i=i+1

#x_title=['MON','TUE','WED','THR','FRI','SAT','SUN']

#for i in range(0,7):
#    for j in range(0, len(a[i])):
#        print(x_title[i],'[',j,']=',a[i][j])