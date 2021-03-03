# 画螺丝
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from pylab import *
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

def draw(ax, r, high, offset=0., **kwargs):
    t = np.linspace(0, high, 500)
    z = t+offset
    k = 10 * np.pi
    x = r * sin(k * t)
    y = r * cos(k * t)
    if offset<0:
        cut = 0
        for i in range(500):
            if z[cut]>=0:
                break
            cut+=1
        z=z[cut:]
        x=x[cut:]
        y=y[cut:]
    elif offset>0:
        cut = len(z)-1
        for i in range(500):
            if z[cut]<=high:
                break
            cut-=1
        z=z[:cut]
        x=x[:cut]
        y=y[:cut]
    else:
        pass
    ax.plot(x, y, z, **kwargs)

def draw3dPolygon(ax, n, r, z, fill=False, **kwargs):
    lt = np.linspace(0, 2*np.pi, n+1)
    x = [r * np.sin(t) for t in lt]
    y = [r * np.cos(t) for t in lt]
    dots = [[(xi, yi, z)for xi, yi in zip(x,y)]]
    if fill:
        collection = Poly3DCollection(dots, **kwargs)
        ax.add_collection3d(collection)
    else:
        ax.add_collection3d(Line3DCollection(dots, **kwargs))

fig = figure()
ax=Axes3D(fig)

off = 0.1
for i in np.linspace(0, off, 10):
    draw(ax, 0.5-i*1.732, 3, -i, c='grey')
    draw(ax, 0.5-i*1.732, 3, i, c='grey')
draw(ax, 0.5, 3, c='black', alpha=0.1)

# 封顶
draw3dPolygon(ax, 30, 0.5-off*1.732, 3, fill=True, edgecolors='grey', facecolor='grey')
# # 圆形底
# draw3dPolygon(ax, 30, 0.7, 0, fill=True, edgecolors='grey', facecolor='grey')
# draw3dPolygon(ax, 30, 0.7, -0.7, fill=True, edgecolors='grey', facecolor='grey')
# for z in np.linspace(-0.7, 0, 30):
#     draw3dPolygon(ax, 30, 0.7, z, color='grey')

# 六角形底
draw3dPolygon(ax, 6, 1, 0, fill=True, edgecolors='grey', facecolor='grey')
draw3dPolygon(ax, 6, 1, -0.7, fill=True, edgecolors='grey', facecolor='grey')
for z in np.linspace(-0.7, 0, 30):
    draw3dPolygon(ax, 6, 1, z, color='grey')

ax.grid(False)
ax.axis('off')

ax.view_init(0, 300)    # 两个旋转轴，水平平面和竖直平面内旋转


legend()

plt.xlim(-2, 2)
plt.ylim(-2, 2)

show()