import xlrd # 交心版本不再对xls提供支持

xlsx = xlrd.open_workbook('data/e03.xlsx')  # 打开表格
table = xlsx.sheet_by_index(0)  # 通过sheet索引获取
# table = xlsx.sheet_by_name('全部付款方式')  # 通过sheet名称获取

# 获得单元格值的三种方式
print(table.cell_value(5, 3))
print(table.cell(1, 2).value)
print(table.row(1)[2].value)
