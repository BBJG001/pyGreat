# 缺失值和空值
# https://blog.csdn.net/lwgkzl/article/details/80948548
# 删掉全0或全1的列
# https://blog.csdn.net/qxqxqzzz/article/details/88352576
import pandas as pd
import numpy as np
# 待完善


def testKillAllVal(obj_df):
    print(obj_df)
    obj_df = obj_df.loc[~(obj_df==5).all(axis=1), :]  # 删除一行全5, 删除行，轴是1

    obj_df = obj_df.loc[:, ~(obj_df ==88).all(axis=0)]  # 删除一列


    obj_df = obj_df[~(obj_df==6).all(axis=1)]   # 删除行
    # obj_df = obj_df[~(obj_df==99).all(axis=0)]   # 删除列，不可行！！！

    print(obj_df)

def test():
    dates = pd.date_range('20200217', periods=6)
    df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
    df.loc['rowx'] = 5  # 优雅地增加一行全5
    df.loc['rowy'] = 6
    addv = [[88, 99]]*8
    df = pd.concat([df, pd.DataFrame(addv, columns=['col88', 'col99'], index=df.index)], axis=1)


    testKillAllVal(df)

if __name__ == '__main__':
    test()