import xlwt

workbook=xlwt.Workbook()

sheet=workbook.add_sheet("My Sheet")
style=xlwt.easyxf("font:bold 1,color red;")
sheet.write(0,0,'Test Case Name',style)
workbook.save(r"C:\Users\tm\Desktop\Exceldata.xls")