import torch
from torch import nn
from torch.nn import init
import torch.utils.data as Data
import torch.nn.functional as F
import matplotlib.pyplot as plt

torch.manual_seed(1)

# 超参数
N_SAMPLES = 2000
BATCH_SIZE = 64
EPOCH = 20
N_HIDDEN = 8
B_INIT = -0.2   # 模拟不好的 参数初始化

# training data
x_train = torch.unsqueeze(torch.linspace(-7, 10, N_SAMPLES), 1)
y_train = x_train**2 - 5 + torch.normal(0, 2, x_train.shape)

# test data
x_test = torch.unsqueeze(torch.linspace(-7, 10, 200), 1)
y_test = x_test**2 - 5 + torch.normal(0, 2, x_test.shape)

train_dataset = Data.TensorDataset(x_train, y_train)
train_loader = Data.DataLoader(dataset=train_dataset, batch_size=BATCH_SIZE, shuffle=True, )

# show data
# plt.scatter(x_train, y_train, c='#FF9359', s=10, alpha=0.9, label='train')
# plt.legend(loc='upper left')
# plt.show()

net = torch.nn.Sequential(
    torch.nn.Linear(1, N_HIDDEN),
    torch.nn.ReLU(),
    torch.nn.Linear(N_HIDDEN, N_HIDDEN),
    torch.nn.ReLU(),
    torch.nn.Linear(N_HIDDEN, 1),
)

net_bn = torch.nn.Sequential(
    # torch.nn.BatchNorm1d(1),
    torch.nn.Linear(1, N_HIDDEN),
    torch.nn.BatchNorm1d(N_HIDDEN),
    torch.nn.ReLU(),
    torch.nn.Linear(N_HIDDEN, N_HIDDEN),
    torch.nn.BatchNorm1d(N_HIDDEN),
    torch.nn.ReLU(),
    torch.nn.Linear(N_HIDDEN, 1),
)

optimizer_ = torch.optim.Adam(net.parameters(), lr=0.01)
optimizer_bn = torch.optim.Adam(net_bn.parameters(), lr=0.01)
loss_func = torch.nn.MSELoss()

plt.ion()   # 开启pyplot的交互模式
for epoch in range(EPOCH):
    for step, (b_x, b_y) in enumerate(train_loader):  # 分配 batch data, normalize x when iterate train_loader
        pred_ = net(b_x)
        pred_bn = net_bn(b_x)

        loss_ = loss_func(pred_, b_y)
        loss_bn = loss_func(pred_bn, b_y)

        optimizer_.zero_grad()
        optimizer_bn.zero_grad()
        loss_.backward()
        loss_bn.backward()
        optimizer_.step()
        optimizer_bn.step()

        # 拿测试数据测测准确度
        if step % 200 == 0:
            net.eval()
            net_bn.eval()

            # 进入测试模型，绘制图像
            test_pred_ = net(x_test)
            test_pred_bn = net_bn(x_test)

            plt.cla()

            # plt.scatter(x_train, y_train, c='red', s=10, alpha=1, label='train')
            plt.scatter(x_test, y_test, c='green', s=10, alpha=0.5, label='test')
            plt.plot(x_test, test_pred_.detach().numpy(), 'b-', lw=2, label='net')
            plt.plot(x_test, test_pred_bn.detach().numpy(), 'm--', lw=2, label='net_bn')
            plt.ylim(-20, 100)
            plt.text(-3, 70, 'net_loss: %.4f'%loss_func(y_test, test_pred_),
                     fontdict={'size': 15, 'color': 'black'})
            plt.text(-3, 60, 'net_loss_bn: %.4f'%loss_func(y_test, test_pred_bn),
                     fontdict={'size': 15, 'color': 'black'})
            print('net_loss: %.4f'%loss_func(y_test, test_pred_))
            print('net_loss_bn: %.4f'%loss_func(y_test, test_pred_bn))

            plt.legend(loc='upper left')
            plt.pause(0.1)

            # 作图完，进入训练模式
            net.train()
            net_bn.train()

plt.ioff()  # 关闭交互模式
plt.show()