import torch
import numpy as np
from tools.Deep_pytorch.t06modelsave import Net

# print(torch.linspace(-5,5,9).unsqueeze(1))

# print(torch.eye(5))

# t1 = torch.tensor([1,2,3])
# print(t1.unsqueeze(0))
# # tensor([[1, 2, 3]])
# print(t1.unsqueeze(1))
# # tensor([[1],
# #         [2],
# #         [3]])
# print(t1.unsqueeze(2))
# # IndexError: Dimension out of range (expected to be in range of [-2, 1], but got 2)
# print(t1.size())
# print(t1.unsqueeze(0).size())
# print(t1.unsqueeze(1).size())
# # torch.Size([3])
# # torch.Size([1, 3])
# # torch.Size([3, 1])
#
# t2 = torch.tensor([[1,2,3],[4,5,6]])
# print(t2.size())
# # torch.Size([2, 3])
# print(t2.unsqueeze(0).size())
# # torch.Size([1, 2, 3])
# print(t2.unsqueeze(1).size())
# # torch.Size([2, 1, 3])
# print(t2.unsqueeze(2).size())
# # torch.Size([2, 3, 1])
# # print(t2.unsqueeze(3).size())
# # IndexError: Dimension out of range (expected to be in range of [-3, 2], but got 3)
#
# print(t2.unsqueeze(0))
# # tensor([[[1, 2, 3],
# #          [4, 5, 6]]])
# print(t2.unsqueeze(1))
# # tensor([[[1, 2, 3]],
# #
# #         [[4, 5, 6]]])

# print(torch.rand(5))

# t1 = torch.tensor([1,2,3])
# t2 = torch.tensor([1,2,2])
# print((t1==t2).numpy())
# print(np.mean((t1==t2).numpy()))

# net2=torch.load('data/models/classnet.pkl')
# print(net2(torch.tensor([10.,10.])))
# print(net2(torch.tensor([1.,2.])))
# print(net2(torch.tensor([2.,1.])))
# print(net2(torch.tensor([1.,1.])))
# print(net2(torch.tensor([0.,0.])))
# tensor([0.9182, 0.0818], grad_fn=<SoftmaxBackward>)
# 通过模型计算（2，2）这个点的类型，可以看出属于0类的概率远大于属于1类的概率

# t1 = torch.tensor([1, 2, 3])
# t2 = torch.tensor([2, 2, 2])
# t = torch.tensor([[1, 7, 3], [4, 5, 6]])
# # tensor([[1, 7, 3],
# #         [4, 5, 6]])
#
# accurary = sum((t1 == t2).numpy()) / len(t1)
# print(accurary)
# # print(torch.max(t))
# # # tensor(7)
# # print(torch.max(t, 1))  # 第二个参数是维度，0取列内的最大值，1取行内的最大值
# # # torch.return_types.max(
# # # values=tensor([7, 6]),
# # # indices=tensor([1, 2]))
# # print(torch.max(t, 1)[0])  # 最大值
# # # tensor([7, 6])
# # print(torch.max(t, 1)[1])  # 最大值的索引
# # # tensor([1, 2])


# tuple1 = (1,2,3)
# print(type(tuple1))
# npt = np.array(tuple1)
# print(type(npt))
# print(npt)

# ll=np.array([1,2,3])
# ll2 =[1,2,3]
# print(ll2.ravel())

# print(np.random.uniform(0, 6, size=5)[:, np.newaxis])

# print(torch.log(torch.tensor(1.)))

# flag = torch.cuda.is_available()
# print(flag)
#
# ngpu= 1
# # Decide which device we want to run on
# device = torch.device("cuda:0" if (torch.cuda.is_available() and ngpu > 0) else "cpu")
# print(device)
# print(torch.cuda.get_device_name(0))
# print(torch.rand(3,3).cuda())
# True
# cuda:0
# GeForce GTX 1060
# tensor([[0.5772, 0.5287, 0.0946],
#         [0.9525, 0.7855, 0.1391],
#         [0.6858, 0.5143, 0.8188]], device='cuda:0')

# def fun(x,y):
#     return x+y
#
# print(fun({3,5}))

x = torch.tensor([[1,1], [2,2], [3,5], [-1,-4]]).type(torch.float)

net2=torch.load('data/models/classnet.pkl')
res = net2(x)
print(res)
prediction2 = torch.max(res, 1)
print(prediction2)