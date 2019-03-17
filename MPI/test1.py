from mpi4py import MPI
from csv import DictReader, field_size_limit
from os import listdir
from sys import maxsize
import numpy as np
from pandas import read_csv
from re import findall

maxInt = maxsize
decrement = True
arr = []
arr3 = []
arr4 = []
comm = MPI.COMM_WORLD
count = 0

def countT(texto, palabra):
    nlist = findall(r"[\w']+", texto)
    return nlist.count(palabra)

def test():
    
    if comm.rank == 0:
        try:
            a = input('Ingrese la palabra que desea buscar: ')
        except ValueError:
            print ("Not a string")
        listDir = listdir('/opt/datasets')
        for dirs in listDir:
            with open ('/opt/datasets/'+dirs) as csvf:
                readCSV = DictReader(csvf)
                for row in readCSV:
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

    for row in data:
        tempCont = row['content'].lower()
        tempTitle = row['title'].lower()
        count = countT(tempCont, a.lower()) + countT(tempTitle, a.lower())
        if(count > 0):
            tempArr = [count, row['id'], row['title']]
            arr3.append(tempArr)
            
    newData = comm.gather(arr3, root=0)
    if(comm.rank == 0):
        arr4 = []
        newData = [x for x in newData if x != []] 
        for row2 in newData:
            row2 = sorted(row2, key=lambda x: x[0])
            row2.reverse()
            count2 = 0
            for aux in row2:
                if count2 == 10:
                    break
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
    

while decrement:

    decrement = False
    try:
        field_size_limit(maxInt)
    except OverflowError:
        maxInt = int(maxInt/10)
        decrement = True

    test()
