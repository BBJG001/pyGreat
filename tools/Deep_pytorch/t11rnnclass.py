import torch
from torch import nn
import torchvision
import torch.utils.data as Data
import torchvision.datasets as dsets
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import os


torch.manual_seed(1)  # 为pytorch中的随机操作设置一个随机种子，使得每次随机的结果都一样

# 一些超参数（全局参数）
EPOCH = 2           # 训练整批数据多少次
BATCH_SIZE = 64     # 小批量梯度下降，每次拿一个batch的数据来训练
TIME_STEP = 28      # rnn 时间步数 / 图片高度
INPUT_SIZE = 28     # rnn 每步输入值 / 图片每行像素
LR = 0.01           # 学习率
if os.path.exists('mnist/'):
    DOWNLOAD_MNIST = False
else:
    DOWNLOAD_MNIST = True

# Mnist 手写数字
train_data = torchvision.datasets.MNIST(
    root='./mnist/',    # 保存或者提取位置
    train=True,  # this is training data
    transform=torchvision.transforms.ToTensor(),    # 转换 PIL.Image or numpy.ndarray 成
                                                    # torch.FloatTensor (C x H x W), 训练的时候 normalize 成 [0.0, 1.0] 区间
    download=DOWNLOAD_MNIST,          # 没下载就下载, 下载了就不用再下了
)

test_data = torchvision.datasets.MNIST(root='./mnist/', train=False)

# 批训练 50samples, 1 channel, 28x28 (50, 1, 28, 28)
train_loader = Data.DataLoader(
    dataset=train_data,
    batch_size=BATCH_SIZE,
    shuffle=True,
    num_workers=0,  # 多进程数量，0表示不开多进程，若开多进程调用时需在main中，参见https://blog.csdn.net/BBJG_001/article/details/104369216
)

# 为了节约时间, 我们测试时只测试前2000个
test_x = torch.unsqueeze(test_data.test_data, dim=1).type(torch.FloatTensor)[:2000]/255.   # shape from (2000, 28, 28) to (2000, 1, 28, 28), value in range(0,1)
test_y = test_data.test_labels[:2000]

class RNN(nn.Module):
    def __init__(self):
        super(RNN, self).__init__()

        self.rnn = nn.LSTM(     # LSTM 效果要比 nn.RNN() 好多了
            input_size=28,      # 图片每行的数据像素点
            hidden_size=64,     # rnn 隐藏层的尺寸
            num_layers=1,       # 有几层 RNN layers
            batch_first=True,   # input & output 会是以 batch size 为第一维度的特征集 e.g. (batch, time_step, input_size)
        )

        self.out = nn.Linear(64, 10)    # 输出层

    def forward(self, x):
        # x shape (batch, time_step, input_size)
        # r_out shape (batch, time_step, output_size)
        # h_n shape (n_layers, batch, hidden_size)   LSTM 有两个 hidden states, h_n 是分线, h_c 是主线
        # h_c shape (n_layers, batch, hidden_size)
        r_out, (h_n, h_c) = self.rnn(x, None)   # None 表示 hidden state 会用全0的 state

        # 选取最后一个时间点的 r_out 输出
        # 这里 r_out[:, -1, :] 的值也是 h_n 的值
        out = self.out(r_out[:, -1, :])
        return out

rnn = RNN()
print(rnn)
'''
RNN(
  (rnn): LSTM(28, 64, batch_first=True)
  (out): Linear(in_features=64, out_features=10, bias=True)
)
'''

optimizer = torch.optim.Adam(rnn.parameters(), lr=LR)   # optimize all parameters
loss_func = nn.CrossEntropyLoss()   # the target label is not one-hotted

# 训练 测试
for epoch in range(EPOCH):
    for step, (x, b_y) in enumerate(train_loader):   # gives batch data
        b_x = x.view(-1, 28, 28)   # reshape x to (batch, time_step, input_size)
        if step==0:
            print(b_x.shape)
        output = rnn(b_x)               # rnn output
        loss = loss_func(output, b_y)   # cross entropy loss
        optimizer.zero_grad()           # clear gradients for this training step
        loss.backward()                 # backpropagation, compute gradients
        optimizer.step()                # apply gradients

        # 拿测试数据测测准确度
        if step % 100 == 0:
            test_output = rnn(test_x.view(-1, 28, 28))
            pred_y = torch.max(test_output, 1)[1]
            accurary = sum((test_y == pred_y).numpy()) / len(test_y)
            print('Epoch: {} | step: {:0>4d} | train loss: {:.5f} | test accurary: {:.3f}'.format(epoch, step, loss,                                                                                   accurary))
            '''
            ...
            Epoch: 1 | step: 0600 | train loss: 0.15526 | test accurary: 0.971
            Epoch: 1 | step: 0700 | train loss: 0.31250 | test accurary: 0.973
            Epoch: 1 | step: 0800 | train loss: 0.07279 | test accurary: 0.971
            Epoch: 1 | step: 0900 | train loss: 0.11018 | test accurary: 0.968
            '''

test_output = rnn(test_x.view(-1, 28, 28))
pred_y = torch.max(test_output, 1)[1]  # 把数据条目中维度为1 的删除掉
print(pred_y, 'prediction number')
print(test_y, 'real number')
print('accuracy:', sum((test_y == pred_y).numpy()) / len(test_y))
'''
tensor([7, 2, 1,  ..., 3, 9, 5]) prediction number
tensor([7, 2, 1,  ..., 3, 9, 5]) real number
'''