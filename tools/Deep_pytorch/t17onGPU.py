import torch
import torch.nn as nn
import torch.utils.data as Data
import torchvision  # 数据库模块
import os
import time

torch.manual_seed(1)  # 为pytorch中的随机操作设置一个随机种子，使得每次随机的结果都一样

# 一些超参数（全局参数）
EPOCH = 2  # 训练整批数据多少次, 为了节约时间, 我们只训练一次
BATCH_SIZE = 50     # 小批量梯度下降的梯度规格，每次拿一个batch的数据来训练，来优化一波参数
LR = 0.001  # 学习率
if os.path.exists('mnist/'):  # 如果已经存在（下载）了就不用下载了
    DOWNLOAD_MNIST = False
else:
    DOWNLOAD_MNIST = True

# Mnist 手写数字
train_data = torchvision.datasets.MNIST(
    root='./mnist/',  # 保存或者提取位置
    train=True,  # this is training data
    transform=torchvision.transforms.ToTensor(),  # 转换 PIL.Image or numpy.ndarray 成
    # torch.FloatTensor (C x H x W), 训练的时候 normalize 成 [0.0, 1.0] 区间
    download=DOWNLOAD_MNIST,  # 没下载就下载, 下载了就不用再下了
)

test_data = torchvision.datasets.MNIST(root='./mnist/', train=False)

# 批训练 50samples, 1 channel, 28x28 (50, 1, 28, 28)
train_loader = Data.DataLoader(
    dataset=train_data,
    batch_size=BATCH_SIZE,
    shuffle=True,
    num_workers=0
)

'''这里做了改动 .cuda()'''
# 为了节约时间, 我们测试时只测试前2000个（unsqueeze增加维度）
test_x = torch.unsqueeze(test_data.test_data, dim=1).type(torch.FloatTensor)[:2000].cuda() / 255.
# shape from (2000, 28, 28) to (2000, 1, 28, 28), value in range(0,1)
test_y = test_data.test_labels[:2000].cuda()

class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Sequential(  # input shape (1, 28, 28)
            nn.Conv2d(
                in_channels=1,  # input height，厚度，黑白的，一层厚
                out_channels=16,  # 过滤器/卷积核的个数
                kernel_size=5,  # 过滤器/卷积核的规格、尺寸 5*5*channel
                stride=1,  # 步长
                padding=2,  # 如果想要 con2d 出来的图片长宽没有变化, padding=(kernel_size-1)/2 当 stride=1
            ),  # output shape (16, 28, 28)
            nn.ReLU(),  # 激活函数
            nn.MaxPool2d(kernel_size=2),  # 在 2x2 空间里向下采样, output shape (16, 14, 14)
            # nn.MaxPool2d()的stride默认值是kernel_size
        )
        self.conv2 = nn.Sequential(  # input shape (16, 14, 14)
            nn.Conv2d(16, 32, 5, 1, 2),  # output shape (32, 14, 14)
            nn.ReLU(),  # activation
            nn.MaxPool2d(2),  # output shape (32, 7, 7)
        )
        # 输出层
        self.out = nn.Sequential(
            nn.Linear(32 * 7 * 7, 10),  # fully connected layer, output 10 classes
            nn.Softmax(dim=-1)  # 分类中常用的激活函数，dim=-1,在行上进行softmax
        )

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = x.view(x.size(0), -1)  # 把conv2的宽7*高7*厚32的数据拉成1维 (batch_size, 32 * 7 * 7)
        output = self.out(x)
        return output

cnn = CNN()
'''这里做了改动，cnn.cuda()'''
cnn.cuda()
# print(cnn)  # 网络结构
'''
CNN(
  (conv1): Sequential(
    (0): Conv2d(1, 16, kernel_size=(5, 5), stride=(1, 1), padding=(2, 2))
    (1): ReLU()
    (2): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
  )
  (conv2): Sequential(
    (0): Conv2d(16, 32, kernel_size=(5, 5), stride=(1, 1), padding=(2, 2))
    (1): ReLU()
    (2): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
  )
  (out): Sequential(
    (0): Linear(in_features=1568, out_features=10, bias=True)
    (1): Softmax(dim=-1)
  )
)
'''

optimizer = torch.optim.Adam(cnn.parameters(), lr=LR)  # 优化器，传入所有参数
loss_func = nn.CrossEntropyLoss()  # 损失函数
if __name__ == '__main__':
    # training and testing
    for epoch in range(EPOCH):
        ts = time.time()
        for step, (b_x, b_y) in enumerate(train_loader):  # 分配 batch data, normalize x when iterate train_loader
            '''在 train 的时候, 将每次的training data 变成 GPU 形式. + .cuda()'''
            output = cnn(b_x.cuda())  # 拿一个batch的数据跑一圈网络，得一个batch的预测值
            loss = loss_func(output, b_y.cuda())  # 计算损失
            optimizer.zero_grad()  # 清零梯度（上一茬的梯度还在）
            loss.backward()  # 误差反向传递
            optimizer.step()  # 梯度优化参数

            # 拿测试数据测测准确度
            if step % 100 == 0:
                test_output = cnn(test_x)
                pred_y = torch.max(test_output, 1)[1]
                '''这里有改动，在某些计算的时候，还是需要转到cpu上来'''
                accurary = sum((test_y.cpu() == pred_y.cpu()).numpy()) / len(test_y)
                print('Epoch: {} | step: {:0>4d} | train loss: {:.5f} | test accurary: {:.3f}'.format(epoch, step, loss,                                                                                  accurary))
                '''
                ...
                Epoch: 1 | step: 0800 | train loss: 1.46197 | test accurary: 0.974
                Epoch: 1 | step: 0900 | train loss: 1.46265 | test accurary: 0.975
                Epoch: 1 | step: 1000 | train loss: 1.46209 | test accurary: 0.973
                Epoch: 1 | step: 1100 | train loss: 1.52070 | test accurary: 0.980    
                '''
        # te = time.time()    # 算一下处理这一batch的时间
        # print('time cost:', te-ts)

    # 可以不必有这保存提取的过程，只是为了全一下流程
    # 训练结束后保存模型
    torch.save(cnn, r'data/models/ministcnn.pkl')
    # 提取模型测试模型
    cnn2 = torch.load(r'data/models/ministcnn.pkl')

    test_output = cnn2(test_x)
    pred_y = torch.max(test_output, 1)[1]  # 把数据条目中维度为1 的删除掉
    print(pred_y, 'prediction number')
    print(test_y.cpu(), 'real number')
    print('accuracy:', sum((test_y.cpu() == pred_y.cpu()).numpy()) / len(test_y))
    '''
    tensor([7, 2, 1,  ..., 3, 9, 5]) prediction number
    tensor([7, 2, 1,  ..., 3, 9, 5]) real number
    accuracy: 0.9805
    '''
