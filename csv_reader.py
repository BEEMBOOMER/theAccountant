import csv


def readFile(fileName):
    with open(fileName,mode='r',newline="",encoding="utf-8") as file:
        reader=csv.reader(file)
        transactions=list(reader)
        #Reversing of the List so as to get ascending date wise
        transactions=transactions[::-1]
        #Do not need the last row as it is CSV headers of WestPac File
        transactions=transactions[:-1]
        return transactions
 
   