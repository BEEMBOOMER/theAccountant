from openpyxl import load_workbook
import csv
from cateogrizer import categorizer
from csv_reader import readFile
from config import PATH_BANK_STATEMENT,PATH_OUTPUT_FILE
from excel_writer import addToExcel
from datetime import datetime

debitList=[]
creditList=[]
transactions=readFile(PATH_BANK_STATEMENT)
paymentMethod='WestPac'

print("WestPac Exclusive Banker")
for transaction in transactions:
    #The Row without the bank number as it's not needed
    cleanedTransaction=transaction[1:]
    #*_ is used to unpack the list and ignore everything after "credit"
    date,description,debit,credit,*_=cleanedTransaction
    notes=""

    #Debit Only 
    if debit!="":
            category,merchant=categorizer(cleanedTransaction)
            grossAmount=float(debit)
            myshares=grossAmount
            if category=="misc":
                notes="Requires Review"
            debitList.append([date,category.title(),'',description,merchant.title(),grossAmount,'N',myshares,paymentMethod,notes])
    #Credit Only
    else:
        type='Bank Transfer'
        source='me'
        amount=float(credit)
        creditList.append([date,source,type,amount,paymentMethod,notes])

addToExcel(debitList)


#Modular, Description, Add Underneath
#Will it work with existing formulas
# print(cell.value)