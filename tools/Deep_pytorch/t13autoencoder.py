import torch
import torch.nn as nn
import torch.utils.data as Data
import torchvision
import matplotlib.pyplot as plt
import os
import numpy as np
from sklearn import svm
from sklearn.model_selection import GridSearchCV

# 超参数
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

EPOCH = 10
BATCH_SIZE = 64
LR = 0.005
if os.path.exists('mnist/'):  # 如果已经存在（下载）了就不用下载了
    DOWNLOAD_MNIST = False
else:
    DOWNLOAD_MNIST = True   # 下过数据的话, 就可以设置成 False
N_TEST_IMG = 5          # 到时候显示 5张图片看效果, 如上图一

####################################### 获取手写数字图片数据
train_data = torchvision.datasets.MNIST(
    root='./mnist/',
    train=True,                                     # this is training data
    transform=torchvision.transforms.ToTensor(),    # Converts a PIL.Image or numpy.ndarray to
                                                    # torch.FloatTensor of shape (C x H x W) and normalize in the range [0.0, 1.0]
    download=DOWNLOAD_MNIST,                        # download it if you don't have it
)

test_data = torchvision.datasets.MNIST(root='./mnist/', train=False)

# 批训练 50samples, 1 channel, 28x28 (50, 1, 28, 28)
train_loader = Data.DataLoader(
    dataset=train_data,
    batch_size=BATCH_SIZE,
    shuffle=True,
    num_workers=0
)

################################# 构造编码器
class AutoEncoder(nn.Module):
    def __init__(self):
        super(AutoEncoder, self).__init__()

        # 编码网络
        self.encoder = nn.Sequential(
            nn.Linear(28*28, 128),
            nn.Tanh(),
            nn.Linear(128, 64),
            nn.Tanh(),
            nn.Linear(64, 12),
            nn.Tanh(),
            nn.Linear(12, 3),   # 压缩成3个特征, 是为了寿面好进行 3D 图像可视化
            # 当然也可以压缩到5个特征，选其中的三个来作图
        )
        # 解码网络
        self.decoder = nn.Sequential(
            nn.Linear(3, 12),
            nn.Tanh(),
            nn.Linear(12, 64),
            nn.Tanh(),
            nn.Linear(64, 128),
            nn.Tanh(),
            nn.Linear(128, 28*28),
            nn.Sigmoid(),       # 激励函数让输出值在 (0, 1)
        )

    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return encoded, decoded

autoencoder = AutoEncoder()

############################## 训练编码器
optimizer = torch.optim.Adam(autoencoder.parameters(), lr=LR)
loss_func = nn.MSELoss()

for epoch in range(EPOCH):
    for step, (x, b_label) in enumerate(train_loader):
        b_x = x.view(-1, 28*28)   # batch x, shape (batch, 28*28)
        # b_y跟b_x是一样

        encoded_x, decoded_x = autoencoder(b_x)

        loss = loss_func(decoded_x, b_x)    # 这里如果写成b_x会更容易裂解
        optimizer.zero_grad()               # clear gradients for this training step
        loss.backward()                     # backpropagation, compute gradients
        optimizer.step()                    # apply gradients

################################### 用SVM分类
# 取1000个训练数据来训练svm
svm_train = train_data.train_data[:1000].view(-1, 28 * 28).type(torch.FloatTensor) / 255.
s_t_x_afterencoder = autoencoder(svm_train)[0].data.numpy()
print(s_t_x_afterencoder.shape())
s_t_y = train_data.train_labels[:1000].numpy()  # 标签值
print(s_t_y.shape())
# 取1000个训练数据来测试
svm_test = test_data.test_data[:1000].view(-1, 28 * 28).type(torch.FloatTensor) / 255.
s_te_x_afterencoder = autoencoder(svm_test)[0].data.numpy()
s_te_y = test_data.test_labels[:1000].numpy()  # 标签值

c_can = np.logspace(-3, 2, 10)
gamma_can = np.logspace(-3, 2, 10)

model = svm.SVC(kernel='rbf', decision_function_shape='ovr', random_state=1)
clf = GridSearchCV(model, param_grid={'C': c_can, 'gamma': gamma_can}, cv=5, n_jobs=5)
clf.fit(s_t_x_afterencoder, s_t_y)

print('测试集准确率：\t', clf.score(s_te_x_afterencoder, s_te_y))  # 因为压缩到了三个特征，准确率并不是很高
# 测试集准确率：	 0.764

########################### 画图的部分
# 取200个数据来作图
view_data = train_data.train_data[:200].view(-1, 28 * 28).type(torch.FloatTensor) / 255.
encoded_data, _ = autoencoder(view_data)  # 提取压缩的特征值
fig = plt.figure(2)
ax = Axes3D(fig)  # 3D 图
# x, y, z 的数据值
X = encoded_data.data[:, 0].numpy()
Y = encoded_data.data[:, 1].numpy()
Z = encoded_data.data[:, 2].numpy()
values = train_data.train_labels[:200].numpy()  # 标签值
for x, y, z, s in zip(X, Y, Z, values):
    c = cm.rainbow(int(255 * s / 9))  # 上色
    ax.text(x, y, z, s, backgroundcolor=c)  # 标位子
ax.set_xlim(X.min(), X.max())
ax.set_ylim(Y.min(), Y.max())
ax.set_zlim(Z.min(), Z.max())
plt.show()