import csv
from csv import field_size_limit
from os import listdir
from pandas import read_csv
from sys import maxsize


maxInt = maxsize
decrement = True
arrID = []
arrContent = []
arrTitle = []
path='./output.txt'

def read():
    listDir = listdir('/opt/datasets')
    for dirs in listDir:
        with open ('/opt/datasets/' + dirs) as csvf:
            read = csv.DictReader(csvf)
            for row in read:
                arrID.append(row['id'])
                arrContent.append(row['content'])
                arrTitle.append(row['title'])
            print('fucking done', ' size id:',len(arrID),' size content: ',len(arrContent),' size title:',len(arrTitle))
            csvf.close()
            writefile()

def writefile():
    file = open(path,'w')
    string = ""
    #print(string)
    for i in range(len(arrID)):
        #print(i)
        string +=  arrID[i]+'\\'+arrTitle[i]+'\\'+arrContent[i]+'\\'
        #aux = string.join( arrID[i]+'/'+arrTitle[i]+'/'+arrContent[i]+'/')
        #file.write(string)
        #if(i == 200):
            #file.write(string);
            #print(string)
            #break
    file.write(string)
while decrement:
    decrement = False
    try:
        field_size_limit(maxInt)
    except OverflowError:
        maxInt = int(maxInt/10)
        decrement = True

    read()
