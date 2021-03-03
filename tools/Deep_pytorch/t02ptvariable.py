import torch
from torch.autograd import Variable # torch 中 Variable 模块

# 定义一个张量（tensor）
tensor = torch.FloatTensor([[1,3],[5,7]])
# tensor([[1., 3.],
#         [5., 7.]])
# 将tensor封装为Variable
variable = Variable(tensor, requires_grad=True) # 必须传一个torch的tensor
# 一个常用属性，requires_grad是否计算其梯度，也就是是否对变量进行优化更新，感觉有些像tf.Variable的trainable属性
# tensor([[1., 3.],
#         [5., 7.]], requires_grad=True)
# 看起来torch.Tensor跟torch.autograd.Variable是一样的，只是因为两个类的__str__是类似的，有些操作Tensor是无法进行

# 构造函数y=average(sum（x^2）)进行Variable实例演示
t_out = torch.mean(tensor*tensor)       # x^2
# tensor(21.)
v_out = torch.mean(variable*variable)   # x^2
# tensor(21., grad_fn=<MeanBackward0>)

# 模拟 v_out 的误差反向传递
v_out.backward()
# Tensor类的计算结果t_out是不能进行此操作的

# 下面两步看不懂没关系, 只要知道 Variable 是计算图的一部分, 可以用来传递误差就好.
# v_out = 1/4 * sum(variable*variable) 这是计算图中的 v_out 计算步骤
# 针对于 v_out 的梯度就是, d(v_out)/d(variable) = 1/4*2*variable = variable/2

print(variable.grad)    # 计算 Variable 的梯度
# tensor([[0.5000, 1.5000],
#         [2.5000, 3.5000]])