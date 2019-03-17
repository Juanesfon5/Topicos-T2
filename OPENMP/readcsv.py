import csv
from csv import field_size_limit
from os import listdir
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
    for i in range(len(arrID)):
        string +=  arrID[i]+'\''+arrTitle[i]+'\''+arrContent[i]+'\''
    file.write(string)
while decrement:
    decrement = False
    try:
        field_size_limit(maxInt)
    except OverflowError:
        maxInt = int(maxInt/10)
        decrement = True

    read()
