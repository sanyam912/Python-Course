import xlrd
wb = xlrd.open_workbook('example.xls')
ws = wb.sheet_by_name('test')
print(ws.col_values(0))
print(ws.cell(2,1).value)


