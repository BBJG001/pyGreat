import xlrd
import pandas as pd
import xlwt
from xlutils.copy import copy
import xlsxwriter

sheet_np = pd.read_excel('../data/name_position.xlsx', sheet_name='2号楼8F', engine='openpyxl')
talbe_p = xlrd.open_workbook('../data/position.xls')
sheet_p = talbe_p.sheet_by_name('2号楼8F')
res_table_p = copy(talbe_p)
# res_table_p = xlsxwriter.Workbook('../data/position2.xls')
# res_sheet_p = res_table_p.add_sheet('2号楼8F&name')
res_sheet_p = res_table_p.add_sheet('2号楼8F&name')


dd_np = {}
for i in range(50):
    dd_np[sheet_np.iloc[i,2]]=sheet_np.iloc[i,1]
i = 0
for row in sheet_p.get_rows():
    j=0
    for pi in row:
        name = dd_np.get(pi.value, None)
        if name:
            print(name)
            res_sheet_p.write(i,j,name)
            print(i,j,name)
        else:
            res_sheet_p.write(i,j,pi.value)
        j+=1
    i+=1

res_table_p.save('../data/position2.xls')
