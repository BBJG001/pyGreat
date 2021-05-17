import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import platform

# 设置字体，支持中文显示
if platform.system()=='Windows':
    matplotlib.rcParams['font.family'] = 'STSong'
else:
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    # plt.rcParams['font.sans-serif'] = ['Times New Roman']



# 生成颜色
def colorBuilder():
    base = [hex(i) for i in range(40, 201, 20)]
    for i in range(1000):
        np.random.seed(i)
        color = '#{}'.format(''.join([bi[-2:] for bi in np.random.choice(base, 3)]))
        yield color

# 字体设置，好多字体无法生效
def testPlotFont():
    from matplotlib import font_manager
    for font in font_manager.fontManager.ttflist:
        # 查看字体名以及对应的字体文件名
        plt.rcParams['font.sans-serif'] = font.name
        plt.figure()
        plt.text(0.5,0.5, '{}: 中文汉字ZhongWenHanZi'.format(font.name), fontsize=20)
        plt.show()
        print(font.name, '-', font.fname)

# 生成测试数据
x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2

# 生成画布
plt.figure(facecolor='grey', dpi=200)

# figure()中的属性
'''
**num=3**
    画出来图的标题就是‘Figure 3’
    如果传一个str，eg.    num='折线图'   图的标题就是‘折线图’

**figsize=(8, 4)**
    指定绘图对象的宽度和高度，单位为英寸，一英寸=80px
    
**facecolor='blue'**
    背景颜色，默认是白色
    也可以以‘#+6位16进制数’给出，eg.   '#00ff00'
    
**edgecolor='red'**
    边框颜色，默认是白色
    
dpi: 分辨率
'''

# 画图
plt.plot(x, y1, linestyle='--', label='y1 = 2*x + 1')
plt.plot(x, y2)
# plot的属性
'''
**linewidth=3**
    线条宽度
    也可以写作   lw=3

**markersize='20'**
    线上标记的尺寸
    注意要传字符串类型的值

**marker='2'**
    线上的标记
    =============    ===============================
    character        description
    =============    ===============================
    ``'.'``          point marker
    ``','``          pixel marker
    ``'o'``          circle marker
    ``'v'``          triangle_down marker
    ``'^'``          triangle_up marker
    ``'<'``          triangle_left marker
    ``'>'``          triangle_right marker
    ``'1'``          tri_down marker
    ``'2'``          tri_up marker
    ``'3'``          tri_left marker
    ``'4'``          tri_right marker
    ``'s'``          square marker
    ``'p'``          pentagon marker
    ``'*'``          star marker
    ``'h'``          hexagon1 marker
    ``'H'``          hexagon2 marker
    ``'+'``          plus marker
    ``'x'``          x marker
    ``'D'``          diamond marker
    ``'d'``          thin_diamond marker
    ``'|'``          vline marker
    ``'_'``          hline marker
    =============    ===============================

**linestyle=':'**
    线的类型
    =============    ===============================
    character        description
    =============    ===============================
    ``'-'``          solid line style
    ``'--'``         dashed line style
    ``'-.'``         dash-dot line style
    ``':'``          dotted line style
    =============    =============================== 
    也可表示为linestyle='dashed'   

**colors='r'**

    The supported color abbreviations are the single letter codes

    =============    ===============================
    character        color
    =============    ===============================
    ``'b'``          blue
    ``'g'``          green
    ``'r'``          red
    ``'c'``          cyan
    ``'m'``          magenta
    ``'y'``          yellow
    ``'k'``          black
    ``'w'``          white
    =============    ===============================
    也可用'#ff0000'这种形式表示
    
    label: 图例显示内容，配合plt.legend()使用
'''

plt.title('graph_title')

# 显示图例
plt.legend(loc='upper right')

# 显示网格
plt.grid(True)
# ax.grid(False)    # 不显示网格
# ax.axis('off')    # 隐藏坐标轴
#
# ax.view_init(0, 300)    # 设置三维图初始显示角度，两个旋转轴，水平平面和竖直平面内旋转

# 保存图片
plt.savefig('data/demo.png')

plt.pause(0)    # 这么写画图结束后不自行退出
plt.show()  # 必须要有这一句画图才能显示