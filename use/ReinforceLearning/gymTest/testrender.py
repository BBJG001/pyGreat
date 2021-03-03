# gym环境类renderenderingng画图
import gym
from gym.envs.classic_control import rendering
import numpy as np
import time


class RenderTestEnv(gym.Env):
    # 如果你不想改参数，下面可以不用写
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 2
    }

    def __init__(self):
        self.viewer = rendering.Viewer(600, 400)  # 600x400 是画板的长和框

    def render(self, mode='human'):
        # 在gym的画布中，向右为x轴正方向，向上为y轴正方向，左下角为坐标原点
        # 默认颜色：黑色
        # 默认坐标：原点（左下角）

        # --------------------- 画线
        # 方式一
        # 定义一根线
        aline = rendering.Line((100, 30), (500, 30))  # 1
        # 把图形元素添加到画板中
        self.viewer.add_geom(aline)

        # 方式二
        transform0 = rendering.Transform(translation=(50, 100))  # 相对偏移
        self.viewer.draw_line((0, 0), (0, 300), color=(0, 0, 1)).add_attr(transform0)  # 2
        # color：gym中的这个color，我的观察结果它的色域并不是255*255*255的，而是2*2*2的，每一位上可以是0/其他
        # 比如在第一位上，出现1、111、211都是无差别的红色

        # ----------------------- 画圆
        # 方式一
        acircle = rendering.make_circle(50, 10, filled=False)  # 3 *注意下面还做了平移操作
        # radius=10 半径
        # res=30    说是画圆，其实是画正多边形，res指定多边形的边数
        # filled=True   是否填充
        acircle.set_color(0, 1, 0)
        acircle.set_linewidth(5)  # 设置线宽

        # 添加一个平移操作
        transform1 = rendering.Transform(translation=(100, 200))  # 相对偏移
        # 让圆添加平移这个属性
        acircle.add_attr(transform1)

        self.viewer.add_geom(acircle)

        # 方式二
        transform2 = rendering.Transform(translation=(200, 200))  # 相对偏移
        self.viewer.draw_circle(20, 30, False).add_attr(transform2)  # 4

        # -------------------- 画多边形
        # 方式一
        apolygon = rendering.make_polygon([(30, 30), (50, 30), (50, 80), (30, 80)], filled=True)  # 5 *注意下面做了偏移
        # 依次传入各个顶点

        apolygon.set_color(0, 0, 0)
        transform3 = rendering.Transform(translation=(50, 200))  # 相对偏移
        apolygon.add_attr(transform3)
        self.viewer.add_geom(apolygon)
        # 方式二
        transform4 = rendering.Transform(translation=(50, 50))  # 相对偏移
        self.viewer.draw_polygon([(60, 30), (80, 30), (80, 80), (60, 80)], False).add_attr(transform4)  # 6

        # 画非方形的时候，可以借助三角函数找坐标
        transform4 = rendering.Transform(translation=(250, 300))  # 相对偏移，即设定中心
        # 这里打算就像上面画圆似的，找一个中心，根据半径圆心角依次获得各个点的坐标
        radius = 100
        res = 5  # 5边形
        points = [(np.cos(2 * np.pi * i / res) * radius, np.sin(2 * np.pi * i / res) * radius) for i in range(res)]
        self.viewer.draw_polygon(points, False).add_attr(transform4)  # 7 *注意偏移

        # 改变一下顶点的顺序
        transform5 = rendering.Transform(translation=(450, 300))  # 相对偏移，即设定中心
        new_points = [points[0], points[2], points[4], points[1], points[3]]
        self.viewer.draw_polygon(new_points, False).add_attr(transform5)  # 8

        # ----------------------- 画空多边形
        # 方式一
        apolyline1 = rendering.make_polygon([(60, 30), (80, 30), (80, 80), (60, 80)], False)
        '''后续省略，没有在图中出现'''

        # 方式二
        apolyline2 = rendering.make_polyline([(60, 30), (80, 30), (80, 80), (60, 80)])
        # 其内部实现方式就是方式一
        '''后续省略，没有在图中出现'''

        # 方式三
        transform6 = rendering.Transform(translation=(300, 50))  # 相对偏移
        self.viewer.draw_polyline([(60, 30), (80, 30),
                                   (80, 80), (60, 80), (60, 30)]).add_attr(transform6)  # 9
        # 在我这里这种方式下需要最后传入起始点，也就是四边形要传入5个点

        # 那么，也就可以用它来画曲线了
        transform7 = rendering.Transform(translation=(0, 200))  # 相对偏移
        points2 = [(x, 100 * np.sin(0.02 * x)) for x in np.linspace(1, 600, 600)]
        self.viewer.draw_polyline(points2, color=(0, 0, 255), linewidth=5).add_attr(transform7)  # 10

        # 胶囊形状
        acapsule = rendering.make_capsule(10, 20)  # 11
        # length, width, 默认中心画在原点
        acapsule.add_attr(rendering.Transform(translation=(70, 100)))
        self.viewer.add_geom(acapsule)

        return self.viewer.render(return_rgb_array=mode == 'rgb_array')

    def close(self):
        if self.viewer:
            self.viewer.close()


if __name__ == '__main__':
    env = RenderTestEnv()
    while True:
        env.render()
        time.sleep(3)
        break
    env.close()
