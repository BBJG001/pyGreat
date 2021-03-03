import numpy as np
import pandas as pd


# ll = [1,2,3,4,5,6,7]
# ll2 = [7,6,5,4,3,2,1]
# # print(sum(ll==ll2))
# print(np.array(ll)==np.array(ll2))
# print([i for i in ll if i>4])

# print(np.any([False, True]))

# dates = pd.date_range('20200218', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)), columns=['A','B','C','D'])
print(df)
df['E'] = None
print(df)
print(df.columns.tolist())
# print(list(df._stat_axis.values.tolist()))
print(df.index.tolist())
print('B' in df.columns)
print(3 in df.index)

objpd1 = pd.DataFrame(columns=range(4), dtype=np.float64)
objpd1[5] = None
print(objpd1)
