import torch
import torch.nn.functional as F     # 激励函数都在这
import matplotlib.pyplot as plt

torch.manual_seed(0)    # 为了使每次随机生成的数据都是一样的

# 生成训练数据
n_data = torch.ones(100, 2)  # 数据的基本形态，全1矩阵，shape=（100，2）
x0 = torch.normal(2 * n_data, 1)  # 类型0 x data (tensor), shape=(100, 2)
# print(torch.normal(2*n_data, 1))
# normal()传的两个值为均值和标准差，2*n_data就成了一个全是2的矩阵
# normal()出的矩阵中的数据满足以2为均值，以1为标准差的正则分布（就是大部分数据都离2很近，少量数据离2远）
y0 = torch.zeros(100)  # 类型0 y data (tensor), shape=(100, )
x1 = torch.normal(-2 * n_data, 1)  # 类型1 x data (tensor), shape=(100, 1)
# normal()出的矩阵中的数据满足以-2为均值，以1为标准差的正则分布
y1 = torch.ones(100)  # 类型1 y data (tensor), shape=(100, )

# 注意 x, y 数据的数据形式是一定要像下面一样 (torch.cat 是在合并数据)
x = torch.cat((x0, x1), 0)
y = torch.cat((y0, y1), 0).type(torch.long)
# 为y改变一下数据类型，因为网络的输出结果是long类型，在计算loss时需要匹配

# # 观察一下生成的数据
# plt.scatter(x0[:, 0], x0[:, 1], color='red')
# plt.scatter(x1[:, 0], x1[:, 1], color='green')
# plt.show()


class Net(torch.nn.Module):  # 继承 torch 的 Module
    # 我理解为这是在声明网络的静态结构
    def __init__(self, n_feature, n_hidden, n_output):
        super(Net, self).__init__()  # 继承 __init__ 功能
        # 定义每层用什么样的形式
        # .Liner()，“直”（线性）部分，相当与y=f(Wx)中Wx
        self.hidden = torch.nn.Linear(n_feature, n_hidden)  # 隐藏层线性输出
        self.predict = torch.nn.Linear(n_hidden, n_output)  # 输出层线性输出
        # 上面两句就是声明了Net有两层，hidden和predict
        # 如果有多层可以self.hidden1,self.hidden2...,应该注意前尾部与后首的连贯，就是上面两句的n_hidden参数

    # 我理解为声明网络的处理流程，有动态的意思
    def forward(self, x):  # 这同时也是 Module 中的 forward 功能
        # 正向传播输入值, 神经网络分析出输出值
        # 激活函数激活，“弯”非线性部分，相当于y=f(Wx)中的f()部分
        x = F.relu(self.hidden(x))  # 激励函数(隐藏层的线性值)
        # 这一句可以理解为x1=f（x0）
        # y = self.predict(x)  # 输出值
        y = F.softmax(self.predict(x), dim=-1)  # 输出值
        # softmax()是分类中常用的激活函数，它可以将输出转成表达当前数据在每一类上的概率，eg[0.1, 0.9]
        # dim   0 表示对列进行softmax； -1 表示对行进行softmax
        return y

if __name__ == '__main__':

    # 声明一个网络
    net = Net(n_feature=2, n_hidden=10, n_output=2)
    # 数据有两个特征，即点的横纵两个坐标
    # 我们（最开始）输入的y是1维的，但是它的（最终）输出是2维的 tensor (p_class0, p_class1)

    # 通过print可以直接打印网络的结构
    # print(net)  # net 的结构
    # Net(
    #   (hidden): Linear(in_features=2, out_features=10, bias=True)
    #   (predict): Linear(in_features=10, out_features=2, bias=True)
    # )

    # optimizer 是训练的工具
    optimizer = torch.optim.SGD(net.parameters(), lr=0.02)
    # 传入 net 的所有参数, 学习率
    loss_func = torch.nn.CrossEntropyLoss()
    # 误差的计算方式，这里选用的交叉熵损失
    # 交叉熵损失是分类中常用的一种损失函数，表示数据的不确定程度，大概可以这么理解，越合理的分类结果（视觉上就是成堆聚在一块的分成一类），其交叉熵值越小，反之，则越大

    plt.ion()   # 画图
    plt.show()

    for t in range(100):
        res = net(x)  # 喂给 net 训练数据 x, 输出分析值

        # if t==90:
        #     print(res)

        loss = loss_func(res, y)  # 计算两者的误差

        optimizer.zero_grad()  # 清空上一步的残余更新参数值
        loss.backward()  # 误差反向传播, 计算参数更新值
        optimizer.step()  # 将参数更新值施加到 net 的 parameters 上

        # 接着上面来
        if t % 2 == 0:
            plt.cla()
            # 过了一道 softmax 的激励函数后的最大概率才是预测值
            prediction = torch.max(res, 1)[1]
            plt.scatter(x[:, 0], x[:, 1], c=prediction, lw=0, cmap='RdYlGn')
            accuracy = sum((prediction == y).numpy()) / 200.  # 预测中有多少和真实值一样
            plt.text(1.5, -4, 'Accuracy=%.2f' % accuracy, fontdict={'size': 20, 'color': 'red'})
            plt.pause(0.1)

    torch.save(net, 'data/models/classnet.pkl')
    torch.save(net.state_dict(), 'data/models/classnet_params.pkl')

    net2=torch.load('data/models/classnet.pkl')
    print(net2(torch.tensor([2.,2.])))
    # tensor([0.9182, 0.0818], grad_fn=<SoftmaxBackward>)
    # 通过模型计算（2，2）这个点的类型，可以看出属于0类的概率远大于属于1类的概率

    plt.ioff()  # 停止画图
    plt.show()
