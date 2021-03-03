import numpy as np

# 生成测试数据
a = np.arange(1,4)
# [1 2 3]
b = np.arange(10,40,10)
# [10 20 30]
c = np.arange(1,7).reshape((2,3))
# [[1 2 3]
#  [4 5 6]]
d = np.arange(10,70,10).reshape((2,3))
# [[10 20 30]
#  [40 50 60]]

# np.vstack((A,B))：竖向（vertical）堆叠
rescombine = np.vstack((a,b))   # 注意传参方式为（(a,b)）
# [[ 1  2  3]
#  [10 20 30]]
# ！！！该方法把两个堆叠的一维数据编程了二维
rescombine = np.vstack((c,d))   # 注意传参方式为（(c,d)）
# [[ 1  2  3]
#  [ 4  5  6]
#  [10 20 30]
#  [40 50 60]]
# ！！！该方法并没有把两个堆叠的二维数据编程三维的

# np.hstack((A,B))：水平（horizontal）延伸
rescombine = np.hstack((a,b))
# [ 1  2  3 10 20 30]
# ！！！水平延伸一维数据的时候，并没有为其增加维度
rescombine = np.hstack((c,d))
# [[ 1  2  3 10 20 30]
#  [ 4  5  6 40 50 60]]
# ！！！水平延伸二维数据的时候，也没有为其增加维度

# np.concatenate((A,B,B,A),axis=0)：多个矩阵合并
## 先测试二维数据
rescombine = np.concatenate((c,d,d,c),axis=0)
# [[ 1  2  3]
#  [ 4  5  6]
#  [10 20 30]
#  [40 50 60]
#  [10 20 30]
#  [40 50 60]
#  [ 1  2  3]
#  [ 4  5  6]]
rescombine = np.concatenate((c,d,d,c),axis=1)
# [[ 1  2  3 10 20 30 10 20 30  1  2  3]
#  [ 4  5  6 40 50 60 40 50 60  4  5  6]]

## 一维数据合并的时候
rescombine = np.concatenate((a,b,b,a),axis=0)
# [ 1  2  3 10 20 30 10 20 30  1  2  3]
# 水平方向并没有问题
# rescombine = np.concatenate((a,b,b,a),axis=1)
# numpy.AxisError: axis 1 is out of bounds for array of dimension 1
# np.concatenate()并不会为合并数据添加一个维度

# np.newaxis：字面意思理解，一个新的轴，可以实现为array增加一个维度
a_ = a[np.newaxis,:]    # 这里的np.newaxis可以理解为1，‘:’可以理解为所有维度，那么a_的维度就成了（1，3），注意这已经是一个二维数据了
# [[1 2 3]]
b_ = b[np.newaxis,:]
# [[10 20 30]]
_a = a[:,np.newaxis]
# [[1]
#  [2]
#  [3]]
_b = b[:,np.newaxis]
# [[10]
#  [20]
#  [30]]

# 接下来就是见证混乱的时刻
rescombine = np.concatenate((a_,b_,b_,a_),axis=0)
# [[ 1  2  3]
#  [10 20 30]
#  [10 20 30]
#  [ 1  2  3]]
# 可以这么理解，四个（1，3）在第1维度（也就是axis=0（索引从0开始））上延伸，就变成了（4，3）
rescombine = np.concatenate((a_,b_,b_,a_),axis=1)   # 四个(1,3)竖直
# [[ 1  2  3 10 20 30 10 20 30  1  2  3]]
# 四个（1，3）在第2维度（也就是axis=1（索引从0开始））上延伸，就变成了（1，12）
rescombine = np.concatenate((_a,_b,_b,_a),axis=0)
# [[ 1]
#  [ 2]
#  [ 3]
#  [10]
#  [20]
#  [30]
#  [10]
#  [20]
#  [30]
#  [ 1]
#  [ 2]
#  [ 3]]
# (3,1)->(3*4,1)->(12,1)
rescombine = np.concatenate((_a,_b,_b,_a),axis=1)
# [[ 1 10 10  1]
#  [ 2 20 20  2]
#  [ 3 30 30  3]]
# (3,1)->(3,1*4)->(3,12)
