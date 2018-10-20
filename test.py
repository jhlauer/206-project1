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

afile = "P1DataB.csv"
data = getData(afile)

def mySort(data,col):
    data_sorted = sorted(data, key=lambda dict: dict[col])
    return(str((data_sorted)[0]["First"]) + " " +str((data_sorted)[0]["Last"]))

def mySortPrint(a,col,fileName):
    outfile = open(fileName, "w", newline="")
    sort_data = sorted(a, key=lambda dict: dict[col])
    just_data = []
    for dic in sort_data:
        new_dic = {}
        new_dic["First"] = dic["First"]
        new_dic["Last"] = dic["Last"]
        new_dic["Email"] = dic["Email"]
        just_data.append(new_dic)
    fieldnames = ["First", 'Last', "Email"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    for dic in just_data:
        writer.writerow(dic)
    outfile.close()
    return outfile

mySortPrint(data, "Last", "outfile.csv")