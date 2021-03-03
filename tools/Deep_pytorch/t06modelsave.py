import torch
import torch.nn.functional as F     # 激励函数都在这
import matplotlib.pyplot as plt

torch.manual_seed(0)    # 为了使每次随机生成的数据都是一样的

# 生成训练数据
n_data = torch.ones(100, 2)  # 数据的基本形态，全1矩阵，shape=（100，2）
x0 = torch.normal(2 * n_data, 1)  # 类型0 x data (tensor), shape=(100, 2)
y0 = torch.zeros(100)  # 类型0 y data (tensor), shape=(100, )
x1 = torch.normal(-2 * n_data, 1)  # 类型1 x data (tensor), shape=(100, 1)
y1 = torch.ones(100)  # 类型1 y data (tensor), shape=(100, )

# 注意 x, y 数据的数据形式是一定要像下面一样 (torch.cat 是在合并数据)
x = torch.cat((x0, x1), 0)
y = torch.cat((y0, y1), 0).type(torch.long)
# 为y改变一下数据类型，因为网络的输出结果是long类型，在计算loss时需要匹配

class Net(torch.nn.Module):

    def __init__(self, n_feature, n_hidden, n_output):
        super(Net, self).__init__()  # 继承 __init__ 功能
        self.hidden = torch.nn.Linear(n_feature, n_hidden)  # 隐藏层线性输出
        self.predict = torch.nn.Linear(n_hidden, n_output)  # 输出层线性输出

    def forward(self, x):  # 这同时也是 Module 中的 forward 功能
        x = F.relu(self.hidden(x))  # 激励函数(隐藏层的线性值)
        y = F.softmax(self.predict(x))  # 输出值

        return y

if __name__ == '__main__':

    # 声明一个网络
    net = Net(n_feature=2, n_hidden=10, n_output=2)

    # optimizer 是训练的工具
    optimizer = torch.optim.SGD(net.parameters(), lr=0.02)
    loss_func = torch.nn.CrossEntropyLoss()

    for t in range(100):
        res = net(x)  # 喂给 net 训练数据 x, 输出分析值

        loss = loss_func(res, y)  # 计算两者的误差

        optimizer.zero_grad()  # 清空上一步的残余更新参数值
        loss.backward()  # 误差反向传播, 计算参数更新值
        optimizer.step()  # 将参数更新值施加到 net 的 parameters 上

    plt.figure(figsize=(12,4))

    prediction = torch.max(net(x), 1)[1]
    plt.subplot(131, title='net')
    plt.scatter(x[:, 0], x[:, 1], c=prediction, lw=0, cmap='RdYlGn')

    torch.save(net, 'data/models/classnet.pkl')     # 保存整个网络（结构+参数）
    torch.save(net.state_dict(), 'data/models/classnet_params.pkl')  # 只保存网络中的参数 (速度快, 占内存少)
    print('-----------------\n',net.state_dict())

    net2=torch.load('data/models/classnet.pkl')

    prediction2 = torch.max(net2(x), 1)[1]
    plt.subplot(132, title='net2')
    plt.scatter(x[:, 0], x[:, 1], c=prediction2, lw=0, cmap='RdYlGn')

    net3=Net(n_feature=2, n_hidden=10, n_output=2)
    # 将保存的参数复制到 net3
    net3.load_state_dict(torch.load('data/models/classnet_params.pkl'))

    prediction3 = torch.max(net3(x), 1)[1]
    plt.subplot(133, title='net3')
    plt.scatter(x[:, 0], x[:, 1], c=prediction3, lw=0, cmap='RdYlGn')


    print(net(torch.tensor([2., 5.])))
    print(net2(torch.tensor([2., 5.])))
    print(net2(torch.tensor([3., 5.])))
    print(net3(torch.tensor([2., 5.])))
    print(net3(torch.tensor([3., 2.])))

    plt.show()
