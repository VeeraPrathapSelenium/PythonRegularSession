import xlrd

workbook=xlrd.open_workbook(r"C:\Users\tm\Desktop\Apr_30.xlsx")

print(workbook.sheet_names())

sheetdata=workbook.sheet_by_name("Testdata")

print(sheetdata.cell_value(0,0))

print(sheetdata.nrows)
print(sheetdata.ncols)