import torch
import torch.nn.functional as F     # 激励函数都在这
from torch.autograd import Variable

# 做一些假数据来观看图像
x = torch.linspace(-5,5,200).unsqueeze(1)   # .unsqueeze()作用为增加1个维度，x.size=(200,1)
x = torch.tensor(x)  # x data (tensor), shape=(100, 1)
x = Variable(x)

# 激活函数可以理解为 y_=f(Wx) ,
# 为了后面更好的观察激活函数的效果， 这里令W=“1”， 即y=x
# 则y_=f(Wx)=f(x)
W = torch.eye(200)   # 对角矩阵
# 当传入值为5是，W=
# tensor([[1., 0., 0., 0., 0.],
#         [0., 1., 0., 0., 0.],
#         [0., 0., 1., 0., 0.],
#         [0., 0., 0., 1., 0.],
#         [0., 0., 0., 0., 1.]])
W = Variable(W)

y_ = W.mm(x)     # Wx, mm()是pytorch中的矩阵点乘

# 几种常用的 激励函数    y_activate=f(y)=f(Wx)
y_relu = F.relu(y_)
y_sigmoid = F.sigmoid(y_)
y_tanh = F.tanh(y_)
y_softplus = F.softplus(y_)
# y_softmax = F.softmax(y)  softmax 比较特殊, 不能直接显示, 不过他是关于概率的, 用于分类

print(type(y_relu))

# 作图观察
import matplotlib.pyplot as plt  # python 的可视化模块

plt.figure(1, figsize=(8, 6))
plt.subplot(221)
plt.plot(x, y_relu, c='red', label='relu')
plt.ylim((-1, 5))
plt.legend(loc='best')

plt.subplot(222)
plt.plot(x, y_sigmoid, c='red', label='sigmoid')
plt.ylim((-0.2, 1.2))
plt.legend(loc='best')

plt.subplot(223)
plt.plot(x, y_tanh, c='red', label='tanh')
plt.ylim((-1.2, 1.2))
plt.legend(loc='best')

plt.subplot(224)
plt.plot(x, y_softplus, c='red', label='softplus')
plt.ylim((-0.2, 6))
plt.legend(loc='best')

plt.show()