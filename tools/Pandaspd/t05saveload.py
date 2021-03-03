import pandas as pd #加载模块
import numpy as np

# 生成测试数据2
df = pd.DataFrame({'col1':[11,12,13], 'col2':[21,22,23]})
df.to_csv('data/savecsv.csv')

# 从.csv文件读取读取DataFrame对象
df_csv = pd.read_csv(r'data/savecsv.csv', sep=',', header=0, index_col=0)
# 这里的sep是分隔符，当为‘,’时，可以在excel中方便的查看；为‘\t’时，反而在excel不能很好的显示了
# header    # 索引行，指定那一行是索引， 默认值0
# index_cols    # 索引列，指定那一列是做引， 默认值None， 即没有索引列， =-1代表最后一列
print(type(df_csv))
# <class 'pandas.core.frame.DataFrame'>
print(df_csv)
#    col1  col2
# 0    11    21
# 1    12    22
# 2    13    23

# 将DataFrame对象转成np.array对象
npdata2 = df_csv.values
print(type(npdata2))
# <class 'numpy.ndarray'>
print(npdata2)
# [[11 21]
#  [12 22]
#  [13 23]]

df.to_excel('data/saveexcel.xls')
df_excel = pd.read_excel('data/saveexcel.xls', header=0, index_col=0)
# sheet_name=0  # 指定sheet
# header    # 索引行，指定那一行是索引， 默认值0
# index_cols    # 索引列，指定那一列是做引， 默认值None， 即没有索引列， =-1代表最后一列
print(df_excel)
#    col1  col2
# 0    11    21
# 1    12    22
# 2    13    23