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
    with open ('/home/msanch60/Tests/dc-wikia-data.csv') as csvf:
        readCSV = DictReader(csvf)
        for row in readCSV:
            arr.append(row)
        arr2 = np.array(arr)
        out = np.array_split(arr2,comm.size)
        if comm.rank == 0:
            try:
                a = input('Ingrese la palabra que desea buscar: ')
            except ValueError:
                print ("Not a string")
            data = out
        else:
            data = None
            a = None
                        
        a = comm.bcast(a, root=0)
        data = comm.scatter(data, root=0)
                
        #print ('rank',comm.rank,'has data:',a)
        #print(len(data))
        for row in data:
            tempCont = row['name'].lower()
            #tempTitle = row['title'].lower()
            count = tempCont.count(a.lower())
            if(count > 0):
                tempArr = [count, row['ID'], row['name']]
                arr3.append(tempArr)
            
        print("en el rango", comm.rank, "el arreglo tiene", len(arr3))
        newData = comm.gather(arr3, root=0)
        if(comm.rank == 0):
            newData = [x for x in newData if x != []] 
            #print (len(newData))
            print (newData)
        csvf.close()

while decrement:

    decrement = False
    try:
        field_size_limit(maxInt)
    except OverflowError:
        maxInt = int(maxInt/10)
        decrement = True

    test()
