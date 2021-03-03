import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt

torch.manual_seed(1)
np.random.seed(1)

# 超参数
BATCH_SIZE = 64
LR_G = 0.0001           # 生成网络的学习率
LR_D = 0.0001           # 评价网络的学习率
N_IDEAS = 5             # 生成网络“创作”的灵感的个数，即输入的维度
ART_COMPONENTS = 15     # 生成网络在画布内可以画的点的个数，即输出的维度
PAINT_POINTS = np.vstack([np.linspace(-1, 1, ART_COMPONENTS) for _ in range(BATCH_SIZE)])
# 在(-1, 1)上生成15个数

def artist_works():     # 供评价网络学习的优秀作品
    a = np.random.uniform(1, 2, size=BATCH_SIZE)[:, np.newaxis]
    paintings = a * np.power(PAINT_POINTS, 2) + (a-1)   # y=a*x^2+a-1
    paintings = torch.from_numpy(paintings).float()     # 转换成tensor
    return paintings

# 构造生成网络
G = nn.Sequential(                      # 生成器
    nn.Linear(N_IDEAS, 128),            # 随机灵感（可以按正态分布取值）
    nn.ReLU(),
    nn.Linear(128, ART_COMPONENTS),     # 根据随机灵感进行创作
)

# 构造评价网络
D = nn.Sequential(                      # 评价器
    nn.Linear(ART_COMPONENTS, 128),     # 接收一件作品（来自大师或者上面的生成网络）
    nn.ReLU(),
    nn.Linear(128, 1),
    nn.Sigmoid(),                       # 返回生成网络的作品跟优秀作品的相似度(0,1)，或者说是评价输入是优秀作品的概率
)

# 优化器
opt_D = torch.optim.Adam(D.parameters(), lr=LR_D)
opt_G = torch.optim.Adam(G.parameters(), lr=LR_G)

plt.ion()   # 用来支持画动态图

for step in range(10000):
    artist_paintings = artist_works()           # 优秀作品
    G_ideas = torch.randn(BATCH_SIZE, N_IDEAS)  # 随机构造生成网络的输入数据
    G_paintings = G(G_ideas)                    # 调用生成网络生成作品

    prob_artist0 = D(artist_paintings)          # 评价网络评价优秀作品，用来后面优化评价结果，反向修正评价网络的参数
    prob_artist1 = D(G_paintings)               # 评价网络评价生成网络的作品

    # 计算损失
    D_loss = - torch.mean(torch.log(prob_artist0) + torch.log(torch.tensor(1.) - prob_artist1))
    # 让评价器去批判生成器，你的生成作品离1很远，生成器就会更加趋向1的去生成作品
    G_loss = torch.mean(torch.log(torch.tensor(1.) - prob_artist1))
    # 让评价器把优秀作品的评价结果趋近于1

    # 清空梯度
    opt_D.zero_grad()
    # 反向传递
    D_loss.backward(retain_graph=True)      # retain_graph 这个参数是为了再次使用中间变量
    # 执行优化
    opt_D.step()

    opt_G.zero_grad()
    G_loss.backward()
    opt_G.step()

    # 可视化
    if step % 50 == 0:
        plt.cla()
        # 生成网络作品
        plt.plot(PAINT_POINTS[0], G_paintings.detach().numpy()[0], c='#4AD631', lw=3, label='Generated painting', )
        # 优秀作品上限
        plt.plot(PAINT_POINTS[0], 2 * np.power(PAINT_POINTS[0], 2) + 1, c='#74BCFF', lw=3, label='upper bound')
        # 优秀作品下限
        plt.plot(PAINT_POINTS[0], 1 * np.power(PAINT_POINTS[0], 2) + 0, c='#FF9359', lw=3, label='lower bound')
        plt.text(-.5, 2.3, 'D accuracy=%.2f (0.5 for D to converge)' % prob_artist0.mean(), fontdict={'size': 13})
        plt.text(-.5, 2, 'D score= %.2f (-1.38 for G to converge)' % -D_loss, fontdict={'size': 13})
        plt.ylim((0, 3))
        plt.legend(loc='upper right', fontsize=10)
        plt.draw()
        plt.pause(0.01)     # 暂停0.01s

plt.ioff()
plt.show()