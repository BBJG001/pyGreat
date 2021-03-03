import torch
import torch.nn as nn
import torch.utils.data as Data
from data_helper import do_data_helper
import matplotlib.pyplot as plt

torch.manual_seed(1)  #

# 超参数
EPOCH = 1
BATCH_SIZE = 100
LR = 0.001  # 学习率
DROP = 0.3  # 放置过拟合扔掉一些

TRAIN_PENCENT = 0.8     # 训练数据占的比重

# 获得x,y
x, y = do_data_helper()
# 切分出训练数据和测试数据
train_num = int(len(y) * TRAIN_PENCENT)
train_x = torch.tensor(x[:train_num]).unsqueeze(1)
# print(train_x.shape)
# print(train_x.size())
# print(train_x)
train_y = torch.tensor(y[:train_num])
test_x = torch.tensor(x[train_num:]).unsqueeze(1)
test_y = torch.tensor(y[train_num:])

torch_dataset = Data.TensorDataset(train_x, train_y)
train_loader = Data.DataLoader(
    dataset=torch_dataset,
    batch_size=BATCH_SIZE,
    shuffle=False,
    num_workers=2
)

# 卷积网络
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Sequential(  # input shape (1, 10, 100)
            nn.Conv2d(
                in_channels=1,  # input height，厚度，黑白的，一层厚
                out_channels=16,  # 过滤器/卷积核的个数
                kernel_size=5,  # 过滤器/卷积核的规格、尺寸 5*5*channel
                stride=1,  # 步长
                padding=2,  # 如果想要 con2d 出来的图片长宽没有变化, padding=(kernel_size-1)/2 当 stride=1
            ),  # output shape (16, 10, 100)
            nn.Dropout2d(DROP),
            nn.ReLU(),  # activation
            nn.MaxPool2d(kernel_size=2),  # 在 2x2 空间里向下采样, output shape (16, 5, 50)
            # nn.MaxPool2d()的stride默认值是kernel_size
        )
        self.conv2 = nn.Sequential(  # input shape (16, 5, 50)
            nn.Conv2d(16, 32, 5, 1, 2),  # output shape (32, 5, 50)
            nn.Dropout2d(DROP),
            nn.ReLU(),  # activation
            nn.MaxPool2d(1),  # output shape (32, 5, 50)
        )
        # 输出层
        self.out = nn.Sequential(
            nn.Linear(32 * 5 * 50, 6),  # fully connected layer, output 10 classes
            nn.Dropout2d(DROP),
            nn.Softmax(dim=-1)  # 在行上进行softmax
        )

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = x.view(x.size(0), -1)  # 把conv2的宽7*高7*厚32的数据拉成1维 (batch_size, 32 * 7 * 7)
        output = self.out(x)
        return output

cnn = CNN()
losslist = []

optimizer = torch.optim.Adam(cnn.parameters(), lr=LR)  # optimize all cnn parameters
loss_func = nn.CrossEntropyLoss()  # the target label is not one-hotted
if __name__ == '__main__':
    # training and testing
    for epoch in range(EPOCH):
        for step, (b_x, b_y) in enumerate(train_loader):  # 分配 batch data, normalize x when iterate train_loader
            output = cnn(b_x)  # cnn output
            loss = loss_func(output, b_y)  # cross entropy loss
            optimizer.zero_grad()  # clear gradients for this training step
            loss.backward()  # backpropagation, compute gradients
            optimizer.step()  # apply gradients
            losslist.append(loss)

            if step % 10 == 0:
                test_output = cnn(test_x)
                pred_y = torch.max(test_output, 1)[1]
                accurary = sum((test_y == pred_y).numpy()) / len(test_y)
                print('Epoch: {} | step: {:0>4d} | train loss: {:.5f} | test accurary: {:.3f}'.format(epoch, step, loss, accurary))
    # 保存模型
    torch.save(cnn, r'data/models/classmodel.pkl')

    test_output = cnn(test_x)
    pred_y = torch.max(test_output, 1)[1]
    print(pred_y, 'prediction number')
    print(test_y, 'real number')
    print('accuracy:', sum((test_y == pred_y).numpy()) / len(test_y))

    plt.plot(range(len(losslist)), losslist)
    plt.show()

