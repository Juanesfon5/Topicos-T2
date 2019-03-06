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
    with open ('./all-the-news/articles1.csv') as csvf:
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
    print(string)
    for i in range(len(arrID)):
        string += arrID[i]+'/'+arrTitle[i]+'/'+arrContent[i]+'\n'
        if(i == 2):
            file.write(string);
            #print(string)
            break
while decrement:
    decrement = False
    try:
        field_size_limit(maxInt)
    except OverflowError:
        maxInt = int(maxInt/10)
        decrement = True

    read()
