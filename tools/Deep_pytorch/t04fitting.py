import torch
import matplotlib.pyplot as plt
import torch.nn.functional as F     # 激励函数都在这

# 构造测试数据
x = torch.linspace(-1, 1, 100).unsqueeze(1)  # x data (tensor), shape=(100, 1)
y = x.pow(2) + 0.2*torch.rand(x.size())                 # noisy y data (tensor), shape=(100, 1)

# 画图
plt.scatter(x, y)
# plt.show()

class Net(torch.nn.Module):  # 继承 torch 的 Module
    # 我理解为这是在声明网络的静态结构
    def __init__(self, n_feature, n_hidden, n_output):
        super(Net, self).__init__()     # 继承 __init__ 功能
        # 定义每层用什么样的形式
        # .Liner()，“直”（线性）部分，相当与y=f(Wx)中Wx
        self.hidden = torch.nn.Linear(n_feature, n_hidden)   # 隐藏层线性输出
        self.predict = torch.nn.Linear(n_hidden, n_output)   # 输出层线性输出
        # 上面两句就是声明了Net有两层，hidden和predict
        # 如果有多层可以self.hidden1,self.hidden2...,应该注意前尾部与后首的连贯，就是上面两句的n_hidden参数

    # 我理解为声明网络的处理流程，有动态的意思
    def forward(self, x):   # 这同时也是 Module 中的 forward 功能
        # 正向传播输入值, 神经网络分析出输出值
        # 激活函数激活，“弯”非线性部分，相当于y=f(Wx)中的f()部分
        x = F.relu(self.hidden(x))      # 激励函数(隐藏层的线性值)
        # 这一句可以理解为x1=f（x0）
        y = self.predict(x)             # 输出值
        # 最后这一层输出没有使用激活函数是因为激活函数会把y限定在一定范围内，这里使用激活函数显然是不合理的
        return y

# 声明一个网络
net = Net(n_feature=1, n_hidden=10, n_output=1)

# 通过print可以直接打印网络的结构
# print(net)  # net 的结构
# Net(
#   (hidden): Linear(in_features=1, out_features=10, bias=True)
#   (predict): Linear(in_features=10, out_features=1, bias=True)
# )

# optimizer 是训练的工具
optimizer = torch.optim.SGD(net.parameters(), lr=0.2)
# 传入 net 的所有参数, 学习率
loss_func = torch.nn.MSELoss()
# 误差的计算方式，这里选用的是均方误差

plt.ion()   # 画图
plt.show()

for t in range(1000):
    prediction = net(x)     # 为 net 训练数据 x, 输出预测值

    loss = loss_func(prediction, y)     # 计算两者的均方误差
    # 实践证明这个loss_func只能在上面（未训练之前）声明，下面调用，这里写成loss = torch.nn.MSELoss(prediction, y)会报错

    optimizer.zero_grad()   # 上一步的更新梯度留在net.parameters()中，清空上一步的残余更新参数值
    loss.backward()         # 误差反向传播, 计算参数更新值
    optimizer.step()        # 更新参数（net.patameters()）

    # 接着上面来
    if t % 5 == 0:
        # plot and show learning process
        plt.cla()
        plt.scatter(x, y)
        plt.plot(x, prediction.detach().numpy(), 'r-', lw=5)
        plt.text(0.5, 0, 'Loss=%.4f' % loss, fontdict={'size': 20, 'color': 'red'})
        plt.pause(0.1)