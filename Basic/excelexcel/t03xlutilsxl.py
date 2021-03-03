from xlutils.copy import copy
import xlrd
import xlwt

tem_excel = xlrd.open_workbook('./data/newxl.xls')
# xls是97-03的版本；xlsx是03之后的版本；utils对xlsx支持不到位，可能会出问题，无法复制
tem_sheet = tem_excel.sheet_by_index(0)

new_excel = copy(tem_excel)
new_sheet = new_excel.get_sheet(0)

# 设置格式对象
style = xlwt.XFStyle()

# 字体
font = xlwt.Font()
font.name = '微软雅黑'
font.bold = True        # 加粗
font.height = 360       # 字号18号（360=18*20）
style.font = font       # 将font对象作为style对象的属性封装进style

# 边框
borders = xlwt.Borders()
borders.top = xlwt.Borders.THIN     # 单元格的上边框
borders.bottom = xlwt.Borders.THIN  # 下框
borders.left = xlwt.Borders.THIN    # 左框
borders.right = xlwt.Borders.THIN   # 右框
style.borders = borders

# 对齐
alignment = xlwt.Alignment()
alignment.horz = xlwt.Alignment.HORZ_CENTER # 水平对齐
alignment.vert = xlwt.Alignment.HORZ_CENTER # 垂直对齐
style.alignment = alignment

# 写表格并赋予格式
new_sheet.write(2,1,12, style)
new_sheet.write(3,1,13, style)
new_sheet.write(4,1,14, style)
new_sheet.write(5,1,15, style)

new_excel.save('./data/t_xlutils.xls')


