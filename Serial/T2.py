#!/usr/local/bin/python3

from sys import maxsize
from csv import DictReader, field_size_limit
from os import listdir
maxInt = maxsize
decrement = True

def test():
    try:
        a = input('Ingrese la palabra que desea buscar: ')
    except ValueError:
        print ("Not a string")

    arr = []
    count = 0

    listDir = listdir('/opt/datasets')
    for dirs in listDir:
        with open ('/opt/datasets/'+dirs) as csvf:
            readCSV = DictReader(csvf)
            for row in readCSV:
                tempCont = row['content'].lower()
                tempTitle = row['title'].lower()
                count = tempCont.count(a.lower()) + tempTitle.count(a.lower())
                if(count > 0):
                    tempArr = [count, row['id'], row['title']]
                    arr.append(tempArr)
        csvf.close()

    arr = sorted(arr, key=lambda x: x[0])
    arr.reverse()
    count2 = 0
    for row2 in arr:
        if count2 == 10:
            break
        print(row2[0], row2[1], row2[2])
        count2 += 1

while decrement:

    decrement = False
    try:
        field_size_limit(maxInt)
    except OverflowError:
        maxInt = int(maxInt/10)
        decrement = True
    
    test()
