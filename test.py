import os
import filecmp
import csv
from dateutil.relativedelta import *
from datetime import date

def getData(file):
    inFile = open(file, 'r')
    list = []
    readlines = inFile.readlines()
    header = readlines[0].split(',')
    for i in range(len(header)):
        word = header[i].rstrip('\n')
        header[i] = word
    
    for object in readlines[1:]:
        i = 0
        dict_obj = {}
        split_obj = object.split(',')
        for x in split_obj:
            dict_obj[header[i]] = x
            i += 1
        list.append(dict_obj)	
    
    for dict in list:
        for item in dict.items():
            dict[item[0]] = item[1].rstrip('\n')
    
    inFile.close()
    return list

afile = "P1DataA.csv"
data = getData(afile)

def findMonth(a):
    months = {}
    for dic in a:
        birthday = dic["DOB"]
        month = birthday[:2].rstrip('/')
        if month in months:
            months[month] += 1
        else:
            months[month] = 1
    data = sorted(months.items(), key=lambda x: x[1], reverse=True)
    winner = int(data[0])
    return winner[0]

print(findMonth(data))