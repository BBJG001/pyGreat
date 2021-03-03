# 用来随机生成测试数据
import numpy as np
import pandas as pd

pathin = '../data/datain.csv'  # 生成的左边节点的保存位置
pathout = '../data/dataout.csv'  # 生成的右边节点的保存位置

np.random.seed(1)
dim = 5  # 网格的规格（边长）

sdim = dim * dim

x = np.linspace(-1, 1, dim)
y = np.linspace(-1, 1, dim)
X, Y = np.meshgrid(x, y)
lx = X.reshape([sdim, 1])
ly = Y.reshape([sdim, 1])

lzin = np.array([3] * sdim).reshape([sdim, 1])
lzout = np.array([4] * sdim).reshape([sdim, 1])

P = np.random.rand(sdim).reshape([sdim, 1]) * 50

I = np.random.rand(sdim).reshape([sdim, 1]) * 100

datain = np.concatenate((lx, ly, lzin, I,), axis=1)
dataout = np.concatenate((lx, ly, lzout, P, I), axis=1)

np.savetxt(pathin, datain, delimiter=',', header='x,y,z,I', fmt='%.2f')
np.savetxt(pathout, dataout, delimiter=',', header='x,y,z,P,I', fmt='%.2f')

# testin = pd.read_csv(pathin, sep=',')
# testout = pd.read_csv(pathout, sep=',')
#
# print(testin)
# print(testout)
# 用来随机生成测试数据
import numpy as np
import pandas as pd

pathin = '../data/datain.csv'  # 生成的左边节点的保存位置
pathout = '../data/dataout.csv'  # 生成的右边节点的保存位置

np.random.seed(1)
dim = 5  # 网格的规格（边长）

sdim = dim * dim
# 网格
x = np.linspace(-1, 1, dim)
y = np.linspace(-1, 1, dim)
X, Y = np.meshgrid(x, y)
lx = X.reshape([sdim, 1])
ly = Y.reshape([sdim, 1])

lzin = np.array([3] * sdim).reshape([sdim, 1])
lzout = np.array([4] * sdim).reshape([sdim, 1])

P = np.random.rand(sdim).reshape([sdim, 1]) * 50

I = np.random.rand(sdim).reshape([sdim, 1]) * 100

datain = np.concatenate((lx, ly, lzin, I,), axis=1)
dataout = np.concatenate((lx, ly, lzout, P, I), axis=1)

np.savetxt(pathin, datain, delimiter=',', header='x,y,z,I', fmt='%.2f')
np.savetxt(pathout, dataout, delimiter=',', header='x,y,z,P,I', fmt='%.2f')

# testin = pd.read_csv(pathin, sep=',')
# testout = pd.read_csv(pathout, sep=',')
#
# print(testin)
# print(testout)
