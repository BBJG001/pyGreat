import torch
import matplotlib.pyplot as plt

torch.manual_seed(1)    # 控制torch中的随机机制，使每次的结果相同

N_SAMPLES = 40
N_HIDDEN = 300

# 生成测试数据
x = torch.unsqueeze(torch.linspace(-1, 1, N_SAMPLES), 1)
y = x + 0.3*torch.normal(torch.zeros(N_SAMPLES, 1), torch.ones(N_SAMPLES, 1))

split = int(0.6*N_SAMPLES)
x_train, x_test = x[:split], x[split:]
y_train, y_test = y[:split], y[split:]

# 显示测试数据
# plt.scatter(x_train, y_train, c='red', s=10, alpha=1, label='train')
# plt.scatter(x_test, y_test, c='green', s=10, alpha=1, label='test')
# plt.legend(loc='upper left')
# plt.show()

net_overfitting = torch.nn.Sequential(
    torch.nn.Linear(1, N_HIDDEN),
    torch.nn.ReLU(),
    torch.nn.Linear(N_HIDDEN, N_HIDDEN),
    torch.nn.ReLU(),
    torch.nn.Linear(N_HIDDEN, 1),
)

net_dropped = torch.nn.Sequential(
    torch.nn.Linear(1, N_HIDDEN),
    torch.nn.Dropout(0.5),  # drop 50% of the neuron
    torch.nn.ReLU(),
    torch.nn.Linear(N_HIDDEN, N_HIDDEN),
    torch.nn.Dropout(0.5),  # drop 50% of the neuron
    torch.nn.ReLU(),
    torch.nn.Linear(N_HIDDEN, 1),
)

optimizer_ofit = torch.optim.Adam(net_overfitting.parameters(), lr=0.01)
optimizer_drop = torch.optim.Adam(net_dropped.parameters(), lr=0.01)
loss_func = torch.nn.MSELoss()

plt.ion()   # 开启pyplot的交互模式
for t in range(500):
    pred_ofit = net_overfitting(x)
    pred_drop = net_dropped(x)

    loss_ofit = loss_func(pred_ofit, y)
    loss_drop = loss_func(pred_drop, y)

    optimizer_ofit.zero_grad()
    optimizer_drop.zero_grad()
    loss_ofit.backward()
    loss_drop.backward()
    optimizer_ofit.step()
    optimizer_drop.step()

    # 接着上面来
    if t % 10 == 0:  # 每 10 步画一次图
        # 将神经网络转换成测试形式, 画好图之后改回 训练形式
        net_overfitting.eval()
        net_dropped.eval()  # 因为 drop 网络在 train 的时候和 test 的时候参数不一样.

        # 这里为了作图，我处理了所有x
        test_pred_ofit = net_overfitting(x)
        test_pred_drop = net_dropped(x)

        plt.cla()

        plt.scatter(x_train, y_train, c='red', s=10, alpha=1, label='train')
        plt.scatter(x_test, y_test, c='green', s=10, alpha=1, label='test')
        plt.plot(x.detach().numpy(), test_pred_ofit.detach().numpy(), 'y-', lw=2, label='overfitting')
        plt.plot(x.detach().numpy(), test_pred_drop.detach().numpy(), 'b--', lw=2, label='dropout(50%)')
        plt.ylim(-1.7, 1.7)
        plt.text(0, -0.7,
                 'train overfitting loss=%.4f' % loss_func(test_pred_ofit[:split], y[:split]).detach().numpy(),
                 fontdict={'size': 15, 'color': 'red'})
        plt.text(0, -0.95,
                 'train dropout loss=%.4f' % loss_func(test_pred_drop[:split], y[:split]).detach().numpy(),
                 fontdict={'size': 15, 'color': 'red'})
        plt.text(0, -1.2,
                 'test overfitting loss=%.4f' % loss_func(test_pred_ofit[split:], y[split:]).detach().numpy(),
                 fontdict={'size': 15, 'color': 'green'})
        plt.text(0, -1.45,
                 'test dropout loss=%.4f' % loss_func(test_pred_drop[split:], y[split:]).detach().numpy(),
                 fontdict={'size': 15, 'color': 'green'})
        plt.legend(loc='upper left')
        plt.pause(0.1)

        # 将两个网络改回 训练形式
        net_overfitting.train()
        net_dropped.train()

plt.ioff()  # 关闭交互模式
plt.show()