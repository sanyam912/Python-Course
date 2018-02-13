import xlwt
wb=xlwt.Workbook()
ws=wb.add_sheet('new')

ws.write(2,0,1)
ws.write(2,1,1)
ws.write(2,2,xlwt.Formula("A3+B3"))

wb.save('normal.xls')
