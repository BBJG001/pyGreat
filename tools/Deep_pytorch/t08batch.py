import torch
import torch.utils.data as Data
torch.manual_seed(1)    # reproducible

BATCH_SIZE = 8      # 批训练的数据个数

# 深度学习可行的一个前提是假设数据之间是相互独立的，用相关的数据进行训练会让训练的模型局限于满足一撮数据，没有实用性
# 而更多的现实情况是数据之间存在着或多或少的相关性，所以深度学习中常用海量数据来弥补数据间相关所产生的训练模型的不足
# 在大量数据中学习中，小批量（batch）梯度下降是一种比较好的方式，每次选取一小部分数据来进行参数更新，既能沿着较好的方向更新，又能兼顾训练的效率
#
# 另外，从数据集中随机（不连续）抽取数据也是可以减弱数据相关性的影响的。这一点在随机森林中的到了充分的利用（这里的随机与随机森林中的随机不完全相同）
#
# pytorch中引入了对数据进行切组的机制


x = torch.linspace(0, 9, 10)       # x data (torch tensor)
y = torch.linspace(9, 0, 10)       # y data (torch tensor)

# 先转换成 torch 能识别的 Dataset
torch_dataset = Data.TensorDataset(x, y)

# 把 dataset 放入 DataLoader
loader = Data.DataLoader(
    dataset=torch_dataset,      # 数据，封装进Data.TensorDataset()类的数据
    batch_size=BATCH_SIZE,      # 每块的大小
    shuffle=True,               # 要不要打乱数据 (打乱比较好)
    num_workers=2,              # 多线程来读数据
)

if __name__ == '__main__':
    # 进行3轮训练（每次拿全部的数据进行训练）
    for epoch in range(3):
        # 在一轮中迭代获取每个batch（把全部的数据分成小块一块块的训练）
        for step, (batch_x, batch_y) in enumerate(loader):  # 每一步 loader 释放一小批数据用来学习
            # 假设这里就是你训练的地方...

            # 打出来一些数据
            print('Epoch: ', epoch, '| Step: ', step, '| batch x: ',
                  batch_x, '| batch y: ', batch_y)

'''
BATCH_SIZE = 5 时的结果
Epoch:  0 | Step:  0 | batch x:  tensor([4., 6., 9., 2., 3.]) | batch y:  tensor([5., 3., 0., 7., 6.])
Epoch:  0 | Step:  1 | batch x:  tensor([1., 0., 7., 8., 5.]) | batch y:  tensor([8., 9., 2., 1., 4.])
Epoch:  1 | Step:  0 | batch x:  tensor([3., 5., 6., 9., 7.]) | batch y:  tensor([6., 4., 3., 0., 2.])
Epoch:  1 | Step:  1 | batch x:  tensor([4., 2., 1., 0., 8.]) | batch y:  tensor([5., 7., 8., 9., 1.])
Epoch:  2 | Step:  0 | batch x:  tensor([3., 1., 4., 5., 9.]) | batch y:  tensor([6., 8., 5., 4., 0.])
Epoch:  2 | Step:  1 | batch x:  tensor([2., 8., 0., 7., 6.]) | batch y:  tensor([7., 1., 9., 2., 3.])
'''

# 当无法均等分成若干块时，先按每块BATCH_SIZE大小提取，最后剩下的不足BATCH_SIZE留作最后一块

'''
BATCH_SIZE = 8 时的结果 
Epoch:  0 | Step:  0 | batch x:  tensor([4., 6., 9., 2., 3., 1., 0., 7.]) | batch y:  tensor([5., 3., 0., 7., 6., 8., 9., 2.])
Epoch:  0 | Step:  1 | batch x:  tensor([8., 5.]) | batch y:  tensor([1., 4.])
Epoch:  1 | Step:  0 | batch x:  tensor([3., 5., 6., 9., 7., 4., 2., 1.]) | batch y:  tensor([6., 4., 3., 0., 2., 5., 7., 8.])
Epoch:  1 | Step:  1 | batch x:  tensor([0., 8.]) | batch y:  tensor([9., 1.])
Epoch:  2 | Step:  0 | batch x:  tensor([3., 1., 4., 5., 9., 2., 8., 0.]) | batch y:  tensor([6., 8., 5., 4., 0., 7., 1., 9.])
Epoch:  2 | Step:  1 | batch x:  tensor([7., 6.]) | batch y:  tensor([2., 3.])
'''