from openpyxl import load_workbook
import csv
from cateogrizer import categorizer

print("WestPac Exclusive Banker")


debitList=[]
creditList=[]

with open('test.csv',mode='r',newline="",encoding="utf-8") as file:
    paymentMethod='WestPac'
    reader=csv.reader(file)
    transactions=list(reader)
    transactions=transactions[::-1]
    transactions=transactions[:-1]
    for row in transactions:
        #The Row without the bank number as I do not need that
        cleanedRow=row[1:]
        date=cleanedRow[0]
        if cleanedRow[2]!="":
                category,merchant=categorizer(cleanedRow)
                description=cleanedRow[1]
                grossAmount=float(cleanedRow[2])
                myshares=grossAmount
                notes=""
                if category=="misc":
                    notes="Requires Review"
                debitList.append([date,category.title(),'',description,merchant.title(),grossAmount,'N',grossAmount,paymentMethod,notes])
        else:
            type='Bank Transfer'
            source='me'
            amount=float(cleanedRow[3])
            notes=''
            creditList.append([date,source,type,amount,paymentMethod,notes])
   

wb = load_workbook(filename = "book2.xlsx")
sheet=wb["Sheet1"]

startRow=6
startCol=3 #Translates to C
for row in debitList:
    print(row)
    for column,value in enumerate(row,start=startCol):
        sheet.cell(row=startRow,column=column).value=value
    startRow+=1
wb.save('Book2.xlsx')


#Modular, Description, Add Underneath
#Will it work with existing formulas
# print(cell.value)