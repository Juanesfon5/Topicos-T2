#-*-coding:utf-8-*-
from mpi4py import MPI
from csv import DictReader, field_size_limit
from os import listdir
from sys import maxsize
import numpy as np

maxInt = maxsize
decrement = True
arr = []
arr3 = []
comm = MPI.COMM_WORLD
count = 0
def test():
    if comm.rank == 0:
        try:
                    a = input('Ingrese la palabra que desea buscar: ')
        except ValueError:
                    print ("Not a string")
        
    with open ('/home/jfonsec1/tests/Tests/dc-wikia-data.csv') as csvf:
        readCSV = DictReader(csvf)
        for row in readCSV:
            arr.append(row)
        arr2 = np.array(arr)
        out = np.array_split(arr2,comm.size)
        if comm.rank == 0:
            data = out
        else:
            data = None
        data = comm.scatter(data, root=0)
        #print ('rank',comm.rank,'has data:',data)
        cont = 0
        #arr3 = []
        for row in data:
           # print(row['name'],cont)
            tempCont = row['name'].lower()
            #tempTitle = row['title'].lower()
            count = tempCont.count(a.lower())
            if(count > 0):
                tempArr = [count, row['ID'],row['name']
               # arr3.append(tempArr)

          # print("------------------------------------------------------------------------------------")
        print("------------------------------------------------------------------------------------")
        newData = comm.gather(arr3, root=0)
        if(comm.rank == 0):
            print (len(newData))
        csvf.close()

while decrement:

    decrement = False
    try:
        field_size_limit(maxInt)
    except OverflowError:
        maxInt = int(maxInt/10)
        decrement = True

    test()
