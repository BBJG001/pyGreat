import csv
import numpy as np
import pandas as pd
from sklearn import preprocessing

# 过滤转换字符串的方法
def iris_type(s):
    it = {b'Iris-setosa': 0, b'Iris-versicolor': 1, b'Iris-virginica': 2}
    return it[s]

if __name__ == "__main__":
    path = 'Advertising.csv'  #
    # # 手写读取数据（python基础读文件）
    '''
    f = open(path,'r')
    x = []
    y = []
    for i, d in enumerate(f):
        if i == 0:
            continue
        d = d.strip()                   #去空字符
        if not d:                       #空则跳过
            continue
        #d = map(float, d.split(','))   #don't work
        d = d.split(',')                #这样搞出来是字符串类型
        x.append(d[1:-1])
        y.append(d[-1])
    # print(x)
    # print(y)
    x = np.array(x)
    y = np.array(y)
    # 字符串的转换，处理的鸢尾花的数据，跟这里的path不匹配
    # y[y == 'Iris-setosa'] = 0
    # y[y == 'Iris-versicolor'] = 1
    # y[y == 'Iris-virginica'] = 2
    # y = y.astype(dtype=np.int)
    f.close()
    '''

    # # Python自带库csv读取数据
    '''
    f = open(path, 'r')
    print(f)
    d = csv.reader(f)
    for line in d:
        print(line)
    f.close()
    '''

    # # numpy读入
    '''
    p = np.loadtxt(path, delimiter=',', skiprows=1) #从哪一行开始，默认0
    print(p)
    '''

    # pandas读入

    data = pd.read_csv(path, sep=',', header=0).values    # TV、Radio、Newspaper、Sales
    print(data)
    # sep：默认是','，逗号可以在表格中显示，\t反而不行
    # header：=0就是表格中最上面一行，1是第二行
    # pad.read_csv()读出来的可以根据行首属性名进行操作提取列；pd.read_csv().values则是将读取数据转换成了二维列表，可以按正常的list操作
    # np.savetxt(pathin, datain, delimiter=',', header='x,y,z,I', fmt='%.2f')也可以保存成csv，不过读出来标题行多一个#，显示效果不好
    # pd保存数据
    # output_train = pd.DataFrame({'blogs': bloglist, 'points': pointslist})
    # output_train.to_csv(os.path.join('data', 'train_data.csv'), sep='\t', index=False)
    x = data[['TV', 'Radio', 'Newspaper']]
    # x = data[['TV', 'Radio']]
    y = data['Sales']
    print(x)
    print(y)

    # np读取
    datain = np.load('../data/d_inpro.npy', allow_pickle=True)


    # # 使用sklearn的数据预处理（处理数据中的字符串）
    '''
    df = pd.read_csv(path, header=0)  # 这里的path是鸢尾花数据
    x = df.values[:, :-1]
    y = df.values[:, -1]
    print('x = \n', x)
    print('y = \n', y)
    le = preprocessing.LabelEncoder()   #sklearn下的预处理模块
    le.fit(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'])
    print(le.classes_)
    y = le.transform(y) # le匹配的部分，即'Iris-setosa', 'Iris-versicolor', 'Iris-virginica'变成了0、1、2
    print('Last Version, y = \n', y)
    '''

    # np处理数据中的字符串。路径，浮点型数据，逗号分隔，第4列使用函数iris_type单独处理
    '''
    data = np.loadtxt(path, dtype=float, delimiter=',', converters={4: iris_type})
    print(data)
    # 以4分割，4之前（0到3列）组成x，第4列（这里只有第4列）及之后组成y；axis默认为0（按行分割），这里设置为1（按列分割）
    x, y = np.split(data, (4,), axis=1)
    '''