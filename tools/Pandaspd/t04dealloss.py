import pandas as pd
import numpy as np

dates = pd.date_range('20200220', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates, columns=['A','B','C','D'])
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan
'''
             A     B     C   D
2020-02-20   0   NaN   2.0   3
2020-02-21   4   5.0   NaN   7
2020-02-22   8   9.0  10.0  11
2020-02-23  12  13.0  14.0  15
2020-02-24  16  17.0  18.0  19
2020-02-25  20  21.0  22.0  23
'''

# 删除数据
df2 = df.dropna(
    axis=0,     # 0: 对行进行操作; 1: 对列进行操作
    how='any'   # 'any': 只要存在 NaN 就 drop 掉; 'all': 必须全部是 NaN 才 drop
    )
#              A     B     C   D
# 2020-02-22   8   9.0  10.0  11
# 2020-02-23  12  13.0  14.0  15
# 2020-02-24  16  17.0  18.0  19
# 2020-02-25  20  21.0  22.0  23

# 填充数据
df3 = df.fillna(value=0)
#              A     B     C   D
# 2020-02-20   0   0.0   2.0   3
# 2020-02-21   4   5.0   0.0   7
# 2020-02-22   8   9.0  10.0  11
# 2020-02-23  12  13.0  14.0  15
# 2020-02-24  16  17.0  18.0  19
# 2020-02-25  20  21.0  22.0  23

# 判断是否为空
df4 = df.isnull()   # 为空的部分返回True，非空的部位返回False
#                 A      B      C      D
# 2020-02-20  False   True  False  False
# 2020-02-21  False  False   True  False
# 2020-02-22  False  False  False  False
# 2020-02-23  False  False  False  False
# 2020-02-24  False  False  False  False
# 2020-02-25  False  False  False  False

# 判断整个对象中是否 存在 空值
# np.any(object), object中有True为True，全False为False
nullres = np.any(df.isnull())
# True
