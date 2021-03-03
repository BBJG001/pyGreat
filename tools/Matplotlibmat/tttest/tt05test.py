# 两直线围成面
import matplotlib.pyplot  as plt
import numpy as np

from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

fig = plt.figure()

ax = fig.gca(projection='3d')

ax.set_xlabel('X')
ax.set_xlim3d(-1, 2)
ax.set_ylabel('Y')
ax.set_ylim3d(-1, 2)
ax.set_zlabel('Z')
ax.set_zlim3d(-1, 2)

# 顶点
dots = [(0,0,0), (1,0,0), (1,1,0), (0,1,0), (0,0,1), (1,0,1), (1,1,1), (0,1,1)]
# 面（上面点的索引）
faces = [(0,1,2,3), (4,5,6,7), (0,1,5,4), (1,2,6,5), (2,3,7,6), (3,0,4,7)]
# 将上面的“由点索引描述的面”映射回“由点坐标描述的面”
poly3d = [[dots[d_id] for d_id in face] for face in faces]
print(poly3d)
print(np.array(poly3d).shape)
x, y, z = zip(*dots)
ax.scatter(x, y, z)     # 画出8个顶点

collection = Poly3DCollection(poly3d, edgecolors='r', facecolor=[0.5, 0.5, 1], linewidths=1, alpha=0.3)
ax.add_collection3d(collection)

# ax.add_collection3d(Line3DCollection(poly3d, colors='b', linewidths=0.5))

plt.show()