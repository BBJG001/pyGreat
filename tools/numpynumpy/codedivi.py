import numpy as np

A = np.arange(12).reshape((3, 4))
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# # 平均分割np.split(array, split_num, axis=0)
# print(np.split(A, 2, axis=0))
# # 报错，无法把3行按行平均分成2个
# print(np.split(A, 2, axis=1))       # 平均分，按列（axis=1）分成2个
# # [array([[0, 1],
# #        [4, 5],
# #        [8, 9]]), array([[ 2,  3],
# #        [ 6,  7],
# #        [10, 11]])]

# # 不均等分割np.array_split(array, split_num, axis=1)
# print(np.array_split(A, 3, axis=0))
# # 结果有 l/n 和 l/n+1 为的子列表组成，前面的大
# # [array([[0, 1],
# #        [4, 5],
# #        [8, 9]]), array([[ 2],
# #        [ 6],
# #        [10]]), array([[ 3],
# #        [ 7],
# #        [11]])]

# # 其他分割np.vsplit()、np.hsplit()，也是两种平均分
# print(np.vsplit(A, 3)) #vertical，等于print(np.split(A, 3, axis=0))，竖直上分是水平切？
# # [array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]
# print(np.hsplit(A, 2)) #等于 print(np.split(A, 2, axis=1))
# # [array([[0, 1],
# #        [4, 5],
# #        [8, 9]]), array([[ 2,  3],
# #        [ 6,  7],
# #        [10, 11]])]