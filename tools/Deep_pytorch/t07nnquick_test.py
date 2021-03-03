import torch
import torch.nn.functional as F     # 激励函数都在这
import matplotlib.pyplot as plt

torch.manual_seed(0)    # 为了使每次随机生成的数据都是一样的

# 生成测试数据
n_data = torch.ones(100, 2)
x0 = torch.normal(2 * n_data, 1)
y0 = torch.zeros(100)
x1 = torch.normal(-2 * n_data, 1)
y1 = torch.ones(100)

# 拼接
x = torch.cat((x0, x1), 0)
y = torch.cat((y0, y1), 0).type(torch.long)

class Net(torch.nn.Module):
    def __init__(self, n_feature, n_hidden, n_output):
        super(Net, self).__init__()
        self.hidden = torch.nn.Linear(n_feature, n_hidden)
        self.predict = torch.nn.Linear(n_hidden, n_output)

    def forward(self, x):
        x = F.relu(self.hidden(x))
        y = F.softmax(self.predict(x), dim=-1)
        return y

if __name__ == '__main__':

    net1 = Net(n_feature=2, n_hidden=10, n_output=2)  # 这是我们用这种方式搭建的 net1

    net2 = torch.nn.Sequential(
        torch.nn.Linear(2, 10),
        torch.nn.ReLU(),
        torch.nn.Linear(10, 2),
        torch.nn.Softmax(dim=-1)
    )

    print(net1)
    """
    Net(
      (hidden): Linear(in_features=2, out_features=10, bias=True)
      (predict): Linear(in_features=10, out_features=2, bias=True)
    )
    """
    print(net2)
    """
    (Sequential(
      (0): Linear(in_features=2, out_features=10, bias=True)
      (1): ReLU()
      (2): Linear(in_features=10, out_features=2, bias=True)
      (3): Softmax(dim=None)
    )
    """

    # optimizer 是训练的工具
    optimizer1 = torch.optim.SGD(net1.parameters(), lr=0.02)
    optimizer2 = torch.optim.SGD(net2.parameters(), lr=0.02)
    # 传入 net 的所有参数, 学习率
    loss_func = torch.nn.CrossEntropyLoss()
    # 误差的计算方式，这里选用的交叉熵损失
    # 交叉熵损失是分类中常用的一种损失函数，表示数据的不确定程度，大概可以这么理解，越合理的分类结果（视觉上就是成堆聚在一块的分成一类），其交叉熵值越小，反之，则越大

    for t in range(100):
        res = net1(x)  # 喂给 net 训练数据 x, 输出分析值

        loss = loss_func(res, y)  # 计算两者的误差

        optimizer1.zero_grad()  # 清空上一步的残余更新参数值
        loss.backward()  # 误差反向传播, 计算参数更新值
        optimizer1.step()  # 将参数更新值施加到 net 的 parameters 上

    for t in range(100):
        res = net2(x)  # 喂给 net 训练数据 x, 输出分析值

        loss = loss_func(res, y)  # 计算两者的误差

        optimizer2.zero_grad()  # 清空上一步的残余更新参数值
        loss.backward()  # 误差反向传播, 计算参数更新值
        optimizer2.step()  # 将参数更新值施加到 net 的 parameters 上

    prediction1 = torch.max(net1(x), 1)[1]
    prediction2 = torch.max(net2(x), 1)[1]

    plt.figure(figsize=(8,4))
    plt.subplot(121)
    plt.scatter(x[:, 0], x[:, 1], c=prediction1, lw=0, cmap='RdYlGn')

    plt.subplot(122)
    plt.scatter(x[:, 0], x[:, 1], c=prediction2, lw=0, cmap='RdYlGn')

    print(net1(torch.tensor([2., 2.])))
    print(net2(torch.tensor([2., 2.])))

    plt.show()

