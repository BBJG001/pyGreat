# [Graphviz Tutorial 1.0 文档](https://graphviztutorial.readthedocs.io/zh_CN/latest/index.html)
# ![Node, Edge and Graph Attributes](http://www.graphviz.org/doc/info/attrs.html)
from graphviz import Digraph
from graphviz import Source

# 需要在本地安装，配置环境变量
# import os
# os.environ["PATH"] += os.pathsep + r'C:\Program Files\graphviz\bin'
# 或许是需要重启的，我这里首次配置了环境变量之后在pycharm中并没有生效，就需要在页面内手动再次设置

dot = Digraph(
    name='Graphtest',
    comment='添加到源码第一行的注释',
    filename=None,
    directory=None,
    format="png",
    engine=None,
    encoding='utf8',
    graph_attr={'rankdir':'TB'},
    node_attr={'color':'black','fontcolor':'black','fontname':'FangSong','fontsize':'12','style':'rounded','shape':'box'},
    edge_attr={'color':'#999999','fontcolor':'#888888','fontsize':'10','fontname':'FangSong'},
    body=None,
    strict=False
)
# name: 图的名字，打开时显示的图的名字.
# comment: 添加的源码第一行的注释.
# filename: 指定.
# directory: (Sub)directory for source saving and rendering.
# format: 输出图片的格式 (``'pdf'``, ``'png'``, ...).
# engine: Layout command used (``'dot'``, ``'neato'``, ...).
# encoding: 图的编码方式，such as ‘utf8’.
# graph_attr: 图属性，属性字典的形式.
# node_attr: 节点属性，属性字典的形式.
#   shape可以是oval（椭圆）、circle（圆）、box（圆角矩形）、
# edge_attr: 边（连线）属性，属性字典的形式.
# body: Iterable of verbatim lines to add to the graph ``body``.
# strict (bool): 如果设置了多条A->B，渲染时多条合并.

# 执行view就会保存，指定filename以filename为准，不指定用name
# save()    保存源码，可以指定文件名，文件名取 指定名>filename>name
# render()  保存图片，可以指定文件名，文件名取 指定名>filename>name

# 添加圆点A,A的标签是Dot A
dot.node('A', 'this is A', {'shape':'circle','color':'blue','fontcolor':'blue'})
# shape 节点形状
# color 颜色
# fontcolor 字体颜色
# 也可以在声明Digraph()对象时进行全局指定，在这里设置了就以这里为准，就近原则
dot.node('B', 'this is B')
dot.node('C', 'this is C')
dot.node('D', 'this is D')
dot.node('E', 'this is E')
dot.node('F', 'this is F')
# dot.view()

# 在创建两圆点之间创建一条边
dot.edge('A', 'B', 'test', _attributes={'style':'dotted', 'dir':'both'})
# style 线的类型，实线，虚线等
# dir   线（箭头）的方向，单向、双向等

# 创建一堆边，即连接AB的两条边，连接AC的一条边。
dot.edges(['AC', 'BD', 'BE', 'EF'])
dot.view()


# 获取DOT source源码的字符串形式，可以通过命令行执行该文件画图
print(dot.source)
# // 添加到源码第一行的注释
# digraph Graphtest {
# 	graph [rankdir=TB]
# 	node [color=black fontcolor=black fontname=FangSong fontsize=12 shape=box style=rounded]
# 	edge [color="#999999" fontcolor="#888888" fontname=FangSong fontsize=10]
# 	A [label="this is A" color=blue fontcolor=blue shape=circle]
# 	B [label="this is B"]
# 	C [label="this is C"]
# 	D [label="this is D"]
# 	E [label="this is E"]
# 	F [label="this is F"]
# 	A -> B [label=test dir=both style=dotted]
# 	A -> C
# 	B -> D
# 	B -> E
# 	E -> F
# }


# 保存source到文件，并提供Graphviz引擎
# dot.save(filename='source.gv', directory='data')    # 保存源码，可以指定文件名，文件名取 指定名>filename>name
# dot.render(directory='data')  # 保存图片，可以指定文件名，文件名取 指定名>filename>name
# dot.view()  # 显示



# 从保存的文件读取并显示
dot_ = Source.from_file('data/source.gv')
print(dot_.source)  # 打印代码
# // 添加到源码第一行的注释
# digraph Graphtest {
# 	graph [rankdir=TB]
# 	node [color=black fontcolor=black fontname=FangSong fontsize=12 shape=box style=rounded]
# 	edge [color="#999999" fontcolor="#888888" fontname=FangSong fontsize=10]
# 	A [label="this is A" color=blue fontcolor=blue shape=circle]
# 	B [label="this is B"]
# 	C [label="this is C"]
# 	D [label="this is D"]
# 	E [label="this is E"]
# 	F [label="this is F"]
# 	A -> B [label=test dir=both style=dotted]
# 	A -> C
# 	B -> D
# 	B -> E
# 	E -> F
# }
dot_.view()  # 显示