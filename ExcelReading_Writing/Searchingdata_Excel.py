import xlrd

workbook=xlrd.open_workbook(r"C:\Users\tm\Desktop\Apr_30.xlsx")

#load Testdata

sheet=workbook.sheet_by_name("Testdata")

rows=sheet.nrows
cols=sheet.ncols
#iterate over rows
for r in range(1,rows):
    celldata=str(sheet.cell_value(r,2))

    if celldata.upper()=="YES":
        print(str(sheet.cell_value(r,0)))












