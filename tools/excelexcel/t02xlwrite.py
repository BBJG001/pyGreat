import xlwt

# 获取表格对象
new_workboot = xlwt.Workbook()

# 获取sheet对象
worksheet = new_workboot.add_sheet('new_sheet')

# 写入单元格内容
worksheet.write(0, 0, 'test00')

# 表格保存
new_workboot.save('./data/newxl.xls')