# 画螺丝
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from pylab import *
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

class Screw:
    def __init__(
            self,
            in_r=0.7,
            out_r=0.9,
            high=3,
    ):
        self.in_r = in_r
        self.out_r = out_r
        self.high = high

        self.fig = figure()
        self.ax = Axes3D(self.fig)

    def draw(self, r, offset=0., **kwargs):
        t = np.linspace(0, self.high, self.high*100)
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
                if z[cut]<=self.high:
                    break
                cut-=1
            z=z[:cut]
            x=x[:cut]
            y=y[:cut]
        else:
            pass
        self.ax.plot(x, y, z, zorder=10, **kwargs)

    def draw3dPolygon(self, n, r, z, fill=True, point=False, **kwargs):
        lt = np.linspace(0, 2*np.pi, n+1)
        x = [r * np.sin(t) for t in lt]
        y = [r * np.cos(t) for t in lt]
        dots = [[(xi, yi, z)for xi, yi in zip(x,y)]]
        if point:
            self.ax.scatter(x, y, [z]*(n+1), s=1, color='black', alpha=0.5)  # 画出8个顶点
        if fill:
            collection = Poly3DCollection(dots, **kwargs)
            self.ax.add_collection3d(collection)
        else:
            self.ax.add_collection3d(Line3DCollection(dots, **kwargs))

    # def draw3dPolygon(self, n, r, z, fill=True, **kwargs):
    #     lt = np.linspace(0, 2*np.pi, n+1)
    #     if fill:
    #         for i in np.linspace(0, r, int(r*50)):
    #             xi = [i * np.sin(t) for t in lt]
    #             yi = [r * np.cos(t) for t in lt]
    #             self.ax.plot(xi, yi, [z]*(n+1), **kwargs)
    #     else:
    #         x = [r * np.sin(t) for t in lt]
    #         y = [r * np.cos(t) for t in lt]
    #         self.ax.plot(x,y,[z]*(n+1), **kwargs)

    def draw3dPolyline(self, n, r, z, **kwargs):
        self.draw3dPolygon(n, r, z, fill=False, **kwargs)

    def draw3dCircle(self, r, z, n=30, **kwargs):
        self.draw3dPolygon(n, r, z, fill=True, **kwargs)

    def draw3dCirline(self, r, z, n=30, **kwargs):
        self.draw3dPolygon(n, r, z, fill=False, **kwargs)

    def drawWhole(self):
        off = 0.1
        # 画螺纹
        for i in np.linspace(0, off, 10):
            self.draw(0.5 - i * 1.732, -i, c='grey', alpha=1)
            self.draw(0.5 - i * 1.732, i, c='grey', alpha=1)
        self.draw(0.5, c='black', alpha=0.3)

        # 封顶
        self.draw3dCircle(0.5-off*1.732, self.high,edgecolors='grey', facecolor='grey') # 面封顶
        # self.draw3dCircle(0.5-off*1.732, self.high,color='grey') # 多线封顶
        # 封底
        # self.draw3dCirline(0.5, 0, color='black')

        # 圆形底
        # self.draw3dCircle(0.7, 0, edgecolors='grey', facecolor='grey')
        # self.draw3dCircle(0.7, -0.7, edgecolors='grey', facecolor='grey')
        # for z in np.linspace(-0.7, 0, 30):
        #     self.draw3dCirline(0.7, z, color='grey')

        # 六角形底_线围成面版本
        self.draw3dPolygon(6, self.out_r, 0, edgecolors='black', facecolor='grey')
        self.draw3dPolygon(6, self.out_r, -0.7, edgecolors='black', facecolor='grey')
        for z in np.linspace(-0.7, 0, 30):
            self.draw3dPolyline(6, self.out_r, z, color='grey', point=True)

        # 六角形底，一层层画线版本
        # self.draw3dPolygon(6, self.out_r, 0, color='grey')
        # self.draw3dPolygon(6, self.out_r, -0.7, color='grey')
        # for z in np.linspace(-0.7, 0, 30):
        #     self.draw3dPolyline(6, self.out_r, z, color='grey')

        self.ax.grid(False)
        self.ax.axis('off')

        self.ax.view_init(0, 300)    # 两个旋转轴，水平平面和竖直平面内旋转


        plt.xlim(-2, 2)
        plt.ylim(-2, 2)

        plt.show()

if __name__ == '__main__':
    obj = Screw()
    obj.drawWhole()