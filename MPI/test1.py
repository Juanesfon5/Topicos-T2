from mpi4py import MPI
from csv import DictReader, field_size_limit
from os import listdir
from sys import maxsize
import numpy as np
from pandas import read_csv

maxInt = maxsize
decrement = True
arr = []
arr3 = []
arr4 = []
comm = MPI.COMM_WORLD
count = 0

def test():
    
    #listDir = listdir('/opt/datasets')
    #for dirs in listDir:
        #with open ('/opt/datasets/'+dirs) as csvf:
            #readCSV = DictReader(csvf)
            #for row in readCSV:
                #arr.append(row)
    #arr2 = np.array(arr)
    #out = np.array_split(arr2,comm.size)
    if comm.rank == 0:
        try:
            a = input('Ingrese la palabra que desea buscar: ')
        except ValueError:
            print ("Not a string")
        listDir = listdir('/opt/datasets')
        for dirs in listDir:
            with open ('/opt/datasets/'+dirs) as csvf:
                readCSV = read_csv(csvf, usecols=[1,2,9])
                for row in readCSV.values.tolist():
                    arr.append(row)
            csvf.close()
        arr2 = arr
        out = np.array_split(arr2,comm.size)
        data = out
    else:
        data = None
        a = None
                        
    a = comm.bcast(a, root=0)
    data = comm.scatter(data, root=0)
                
    #print ('rank',comm.rank,'has data:',a)
    #print(len(data))
    for row in data:
        tempCont = row[2].lower()
        tempTitle = row[1].lower()
        count = tempCont.count(a.lower()) + tempTitle.count(a.lower())
        if(count > 0):
            tempArr = [count, row[0], row[1]]
            arr3.append(tempArr)
            
    #print("en el rango", comm.rank, "el arreglo tiene", len(arr3))
    newData = comm.gather(arr3, root=0)
    if(comm.rank == 0):
        arr4 = []
        newData = [x for x in newData if x != []] 
        #print (len(newData))
        #print (newData)
        for row2 in newData:
            row2 = sorted(row2, key=lambda x: x[0])
            row2.reverse()
            count2 = 0
            for aux in row2:
                if count2 == 10:
                    break
                #print(aux[0], aux[1], aux[2])
                superTempArr = [aux[0], aux[1], aux[2]]
                arr4.append(superTempArr)
                count2 += 1
        arr4 = sorted(arr4, key=lambda x: x[0])
        arr4.reverse()
        count3 = 0
        for row3 in arr4:
            if count3 == 10:
                break
            print(row3[0],row3[1],row3[2])
            count3 += 1
    #csvf.close()
    

while decrement:

    decrement = False
    try:
        field_size_limit(maxInt)
    except OverflowError:
        maxInt = int(maxInt/10)
        decrement = True

    test()
