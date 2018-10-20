import os
import csv
import filecmp
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

def mySort(data,col):
    data_sorted = sorted(data, key=lambda dict: dict[col])
    return(str((data_sorted)[0]["First"]) + " " +str((data_sorted)[0]["Last"]))

def classSizes(data):
    sizes = {"Freshman": 0, "Sophomore": 0, "Junior": 0, "Senior": 0}
    for dic in data:
        class_stand = dic["Class"]
        sizes[class_stand] += 1
    return sorted(sizes.items(), key=lambda x: x[1], reverse=True)

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
    winner = data[0]
    return int(winner[0])

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

def findAge(a):
    birthdays = []
    for dic in a:
        birthdays.append(dic['DOB'])
    ages = []
    for date in birthdays:
        age = int(2018) - int(date[-4:])
        ages.append(age)
    sum = 0
    for age in ages:
        sum += int(age)
    average = sum / len(ages)
    return round(average)


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS ##
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
