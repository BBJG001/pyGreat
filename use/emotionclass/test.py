import numpy as np
import torch

SEQUENCE_LENGTH = 20

# cols = ['col'+str(i) for i in range(SEQUENCE_LENGTH)]
# print(cols)

ll1 = np.array([[1,2,3],[4,5,6]])
ll2 = np.array([7,8])

# ll = np.concatenate((ll1, ll2[:, np.newaxis]), axis=1)

# print(ll2.reshape((-1,1)))

e = np.arange(10,70,10).reshape((-1,3))
# [[10 20 30]
#  [40 50 60]]
print(len(e))


t1 = torch.tensor([[[1,2],[3,4]],[[5,6],[7,8]]])
print(t1)
# tensor([[1, 2],
#         [3, 4]])

print(t1.size())
print(t1.view(-1))