from xlutils.copy import copy
import xlrd
import xlwt


xlsx = xlrd.open_workbook('./data/e03.xlsx')
# xls是97-03的版本；xlsx是03之后的版本；utils对xlsx支持不到位，可能会出问题，无法复制
table = xlsx.sheet_by_index(0)

all_data = []
for n in range(1, table.nrows):
    province = table.cell(n, 5)
    I_value = table.cell(n, 8)

    #
    data = {'province': province, 'I': I_value}
    all_data.append(data)


# 通过省份提取具体对应省份下的所有数据    # 可以用pandas的groupby轻易实现
# 对该省份下的数据进行统计
# 统计完了写入新表
list_province = []
