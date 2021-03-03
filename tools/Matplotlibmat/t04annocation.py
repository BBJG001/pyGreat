import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 2*x + 1

plt.figure(num=1, figsize=(8, 5),)
plt.plot(x, y,)

ax = plt.gca()
# 把右边和上面的轴设置为白色，就相当于隐藏了
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# 设置刻度的位置
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# 设置轴的偏移
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

# 做线上一个点的坐标
x0 = 1
y0 = 2*x0 + 1

# 画垂线，x轴的区间[x0, x0], y轴的区间[0, y0]
plt.plot([x0, x0,], [0, y0,], 'k--', linewidth=2.5)

# 设置一个点
plt.scatter([x0, ], [y0, ], s=50, color='b')
# s 代表size


plt.annotate(s=r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30),
             textcoords='offset pixels', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))
# s                 标记的是标记的内容
# xy                标记点的坐标
# xycoords='data'   是说基于数据的值来选位置(默认），可不设置
'''
              =================   =============================================
              Value               Description
              =================   =============================================
              'figure points'     Points from the lower left of the figure
              'figure pixels'     Pixels from the lower left of the figure
              'figure fraction'   Fraction of figure from lower left
              'axes points'       Points from lower left corner of axes
              'axes pixels'       Pixels from lower left corner of axes
              'axes fraction'     Fraction of axes from lower left
              'data'              Use the coordinate system of the object being
                                  annotated (default)
              'polar'             *(theta,r)* if not native 'data' coordinates
              =================   =============================================
'''
# xytext=(+30, -30) 设点标注相对于点的位置
# textcoords='offset points'
'''
            =================   =========================================
            Value               Description
            =================   =========================================
            'offset points'     Offset (in points) from the *xy* value
            'offset pixels'     Offset (in pixels) from the *xy* value
            =================   =========================================
'''
# fontsize=16       字体颜色
# arrowprops        是对图中箭头类型的一些设置
'''
其中'arrowstyle'are:
            ============   =============================================
            Name           Attrs
            ============   =============================================
            ``'-'``        None
            ``'->'``       head_length=0.4,head_width=0.2
            ``'-['``       widthB=1.0,lengthB=0.2,angleB=None
            ``'|-|'``      widthA=1.0,widthB=1.0
            ``'-|>'``      head_length=0.4,head_width=0.2
            ``'<-'``       head_length=0.4,head_width=0.2
            ``'<->'``      head_length=0.4,head_width=0.2
            ``'<|-'``      head_length=0.4,head_width=0.2
            ``'<|-|>'``    head_length=0.4,head_width=0.2
            ``'fancy'``    head_length=0.4,head_width=0.4,tail_width=0.4
            ``'simple'``   head_length=0.5,head_width=0.5,tail_width=0.2
            ``'wedge'``    tail_width=0.3,shrink_factor=0.5
            ============   =============================================
'''

plt.show()