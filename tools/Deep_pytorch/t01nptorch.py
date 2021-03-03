import torch
import numpy as np

# 生成测试数据
data = [-1,-2,1,1]
data_np = np.array(data)
# [-1 -2  1  1]
tensor = torch.Tensor(data)     # 多维数组也可以被叫做 张量（tensor），本文中就用tensor表示pytorch的数据
# tensor([-1., -2.,  1.,  1.])  # 默认转换成了浮点数

# 数据转换
tensorfromnp = torch.from_numpy(data_np)
# tensor([-1, -2,  1,  1], dtype=torch.int32)
npfromtensor = tensor.numpy()
# [-1. -2.  1.  1.]

# abs绝对值
absdata_np = np.abs(data_np)
# [1 2 1 1]
absdata_torch = torch.abs(tensor)
# tensor([1., 2., 1., 1.])

# 三角函数sin
sin_np = np.sin(data_np)
# [-0.84147098 -0.90929743  0.84147098  0.84147098]
sin_torch = np.sin(tensor)
# tensor([-0.8415, -0.9093,  0.8415,  0.8415])

# 均值
mean_np = np.mean(data_np)
# -0.25
mean_torch = torch.mean(tensor)
# tensor(-0.2500)

# 点乘
# 这里不再另外引入其他矩阵，又为了可以相乘，改变一下形状
data_np = data_np.reshape((2,2))
# [[-1 -2]
#  [ 1  1]]
tensor = tensor.reshape((2,2))
# [[-1 -2]
#  [ 1  1]]
res_np = np.matmul(data_np, data_np)
# [[-1  0]
#  [ 0 -1]]
res_torch = torch.mm(tensor, tensor)
# tensor([[-1.,  0.],
#         [ 0., -1.]])
# 但是pytorch对于A.dot(B)的，要求A和B只能是一维的，否则就会报错
dot_np = data_np.dot(data_np)
# [[-1  0]
#  [ 0 -1]]
# dot_torch = tensor.dot(tensor)  # RuntimeError: 1D tensors expected, . . .
