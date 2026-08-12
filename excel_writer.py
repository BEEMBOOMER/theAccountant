from openpyxl import load_workbook
from config import PATH_BANK_STATEMENT,PATH_OUTPUT_FILE

def addToExcel(debitList):
    wb = load_workbook(filename = PATH_OUTPUT_FILE)
    sheet=wb["Expenses"]
    startRow=7
    startCol=5 #Translates to C
    for row in debitList:
        print(row)
        for column,value in enumerate(row,start=startCol):
            sheet.cell(row=startRow,column=column).value=value
        startRow+=1
    wb.save(PATH_OUTPUT_FILE)

