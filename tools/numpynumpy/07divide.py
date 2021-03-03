import numpy as np

# 生成测试数据（下述维度描述针对此二维数据）
a = np.arange(12).reshape((3,4))
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]



# 均等切分——np.split(A,n,axis=0)
# np.split(A,n,axis=0)把所有切分子集放在一个列表中返回
# A：要切分的矩阵
# n：均等切分成n个，若不能整除会报错
# axis：从哪个维度切分，索引从0开始
## 竖直切，也就是切第二维度
resdivide = np.split(a,2,axis=1)    # 切成2个
# [array([[0, 1],
#        [4, 5],
#        [8, 9]]), array([[ 2,  3],
#        [ 6,  7],
#        [10, 11]])]

## 水平切，也就是切分第一维度
resdivide = np.split(a,3,axis=0)    # 切成3个
# [array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]

# 均等切分——np.vsplit()与np.hsplit()
## np.vsplit()
resdivide = np.vsplit(a,3)
# [array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]
## np.hsplit()
resdivide = np.hsplit(a,2)
# [array([[0, 1],
#        [4, 5],
#        [8, 9]]), array([[ 2,  3],
#        [ 6,  7],
#        [10, 11]])]


# 不均等切分，np.array_split(A,n,axis=0)
# np.array_split(A,n,axis=0)把所有切分子集放在一个列表中返回
# A：要切分的矩阵
# n：切分成n个，额，举例来说明吧，5列分成3份，就是2，2，1；10列分成4分就是3，3，2，2
# axis：从哪个维度切分，索引从0开始
# 竖直切
resdivide = np.array_split(a,3,axis=1)
# [array([[0, 1],
#        [4, 5],
#        [8, 9]]), array([[ 2],
#        [ 6],
#        [10]]), array([[ 3],
#        [ 7],
#        [11]])]
# 把4分成了2，1，1
# 水平切
resdivide = np.array_split(a,2,axis=0)
# [array([[0, 1, 2, 3],
#        [4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]
# 把3分成了2，1

