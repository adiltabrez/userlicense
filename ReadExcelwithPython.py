import xlrd
wb = xlrd.open_workbook('C:\Users\Adil\Desktop\ExcelwithPython\roc.xlsx')
sh = wb.sheet_names()
print sh
