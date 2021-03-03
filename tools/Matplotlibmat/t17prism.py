# 棱柱
import matplotlib.pyplot  as plt

from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

fig = plt.figure()

ax = fig.gca(projection='3d')

ax.set_xlabel('X')
ax.set_xlim3d(0, 2)
ax.set_ylabel('Y')
ax.set_ylim3d(0, 1)
ax.set_zlabel('Z')
ax.set_zlim3d(0, 1)

# 画正四棱锥
# 顶点坐标
verts = [(0, 0, 0), (0, 1, 0), (1, 1, 0), (1, 0, 0), (0.5, 0.5, 0.707)]
# 面
faces = [[0, 1, 4], [1, 2, 4], [2, 3, 4], [0, 3, 4], [0, 1, 2, 3]]

# 每个面对应的点坐标
poly3d = [[verts[vert_id] for vert_id in face] for face in faces]  # 画顶点
x, y, z = zip(*verts)
ax.scatter(x, y, z)

collection = Poly3DCollection(poly3d, edgecolors='r', facecolor=[0.5, 0.5, 1], linewidths=1, alpha=0.3)
ax.add_collection3d(collection)

# ax.add_collection3d(Line3DCollection(poly3d, colors='b', linewidths=0.5))


# 画正四面体
verts1 = [(1, 1, 0), (1, 0, 0), (1.5, 0.5, 0.707), (0.5, 0.5, 0.707)]
faces1 = [[0, 2, 3], [0, 1, 2], [1, 2, 3], [0, 1, 3]]

poly3d1 = [[verts1[vert_id] for vert_id in face] for face in faces1]

x1, y1, z1 = zip(*verts1)
ax.scatter(x1, y1, z1)

collection1 = Poly3DCollection(poly3d1, edgecolors='g', facecolor=[1, 1, 0.5], linewidths=1, alpha=0.3)
ax.add_collection3d(collection1)

# 再画正四棱锥
verts2 = [(1, 0, 0), (1, 1, 0), (2, 1, 0), (2, 0, 0), (1.5, 0.5, 0.707)]
faces2 = [[0, 1, 4], [1, 2, 4], [2, 3, 4], [0, 3, 4], [0, 1, 2, 3]]

poly3d2 = [[verts2[vert_id] for vert_id in face] for face in faces2]

x2, y2, z2 = zip(*verts2)
ax.scatter(x2, y2, z2)

collection2 = Poly3DCollection(poly3d2, edgecolors='r', facecolor=[0.5, 0.5, 1], linewidths=1, alpha=0.3)
ax.add_collection3d(collection2)

plt.show()