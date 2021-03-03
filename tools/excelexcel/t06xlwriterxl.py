# # xlwt向老版本的office兼容，最大index不能超过256
# 但是呢，这个py文件中所说的xlswriter和openpyxl不太稳定，可能会出问题
# import xlsxwriter as xw
# workbook = xw.Workbook('./data/xwrite.xlsx')
# sheet0 = workbook.add_worksheet('sheet0')
# for i in range(300):
#     sheet0.write(0, i, i)
# workbook.close()

#
import openpyxl
workbook = openpyxl.load_workbook('./data/xwrite.xlsx') # 先get这个xlsx
sheet = workbook['sheet0']  # get到想要的sheet
sheet['B3'] = '5'   # 在上面做修改 # ‘5’会把对应的单元格属性设置为“文本”
sheet['B5'] = 7
workbook.save('./data/openpyxldata.xlsx')   # 保存到另一个表