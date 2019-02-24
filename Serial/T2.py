import sys
import csv
import os
maxInt = sys.maxsize
decrement = True

def test():
    try:
        a = input('Ingrese la palabra que desea buscar: ')
    except ValueError:
        print ("Not a string")

    arr = []
    count = 0

    listDir = os.listdir('../datasets/all-the-news')
    for dirs in listDir:
        with open ('../datasets/all-the-news/'+dirs) as csvf:
            readCSV = csv.DictReader(csvf)
            for row in readCSV:
                temp = row['content'].lower()
                count = temp.count(a.lower())
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
        print(row2)
        count2 += 1

while decrement:

    decrement = False
    try:
        csv.field_size_limit(maxInt)
    except OverflowError:
        maxInt = int(maxInt/10)
        decrement = True
    
    test()