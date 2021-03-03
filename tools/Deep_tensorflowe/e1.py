import tensorflow as tf

# 必须有个计算图，有一个默认的，不同的计算图隔绝其中的张量和运算
# 用tf.Graph
a = tf.constant([1, 2], name='a')
b = tf.constant([2, 3], name='b')


v = tf.get_variable('v', [1], initializer=tf.zeros_initializer)

with tf.Session(graph=tf.get_default_graph()) as sess:
    tf.global_variables_initializer().run()
    with tf.variable_scope('', reuse=True):
        print(sess.run(tf.get_variable('v')))

print(a)
print(a.graph)  # a所在的计算图
print(tf.get_default_graph())     # 默认的计算图

# ---------- tf.Graph() collection
# tf.Graph()框出一个范围，用来隔离张量和计算，还可以通过tf.Graph.device指定设备，与其他graph下的变量隔离
# collection属于计算图

# ---------- tf.Session()
# tf.Session拥有并管理TensorFlow程序运行时的所有资源，所有计算完成之后会话来帮助系统回收资源，以免资源泄露
# with tf.Session() as sess:

#---------- initialize run()
# 所有的操作生效都需要特意做一个“动作”，操作才会执行
# 变量的声明需要 initialize 初始化
# 操作的执行需要 run()

# ------------ tf.variable() tf.constant()
# tf.variable() tf声明变量
# v = tf.get_variable('v', shape=[1], initializer=tf.ones_initializer)
# tf.constant() tf声明常量
# matrix1 = tf.constant([[3, 3]])

# ------------ tf.placeholder()
# 即使程序中只有一个常量tf.constant()，不断的迭代也会让计算图存储大量的常量
# 于是就有了placeholder这种机制，x = tf.placeholder(tf.float32)
# 它只是提供存放 量的位置，其数据在程序执行的时候再指定（通过feed_dict={x:3,,,}的方式）


# ------------- 激活函数
# 一个非线性函数，以线性部分的结果为自变量，激活函数作为外层函数进行非线性化
# y = f（W（x））   其中W（x）就是线性部分的函数
# 可以自己写激励函数，必须保证激励函数是可以微分的，这样才可以保证能进行误差反向传递
# 线性可以理解为均匀的变化，激励（非线性）就是不均匀的变了，对可以让网络对某些特征反应强烈，变化快；对某些特征反应迟钝，变化慢
'''
激励函数选择： 层次比较少时，可以选择多种
            卷积网络中，多用relu
            循环神经网络中，多有relu或tanh
tf.nn.relu(features, name=None)
tf.nn.relu6(features, name=None)
tf.nn.softplus(features, name=None)
tf.nn.dropout(x, keep_prob, noise_shape=None, seed=None, name=None)
tf.nn.bias_add(value, bias, name=None)
tf.sigmoid(x, name=None)
tf.tanh(x, name=None)
'''

# --------------- 可视化
# 显示真实数据
# fig = plt.figure()  # 画个框
# ax = fig.add_subplot(1, 1, 1)
# ax.scatter(x_data, y_data)  # 画离散的
# plt.ion()   # plt能动态画图的关键 关键 关键
## 动态显示：Seeting->Tools->Python Scientific->取消勾选“Show plots in tool window”
# plt.show()  # show()了之后，会把画面停住，用上一行语句然plt取消‘停住’
    # try:
    #     ax.lines.remove(lines[0])  # 莫大推荐先清除上一轮花的线，再重新画这一次的，效果好一些，但是第一轮没有“上一轮”，就try catch一下，在第一轮pass
    # except Exception:
    #     pass
    # prediction_value = sess.run(prediction, feed_dict={xs: x_data})  # 获得y_predict
    # lines = ax.plot(x_data, prediction_value, 'r-', lw=5)  # 画连续的
    # ax.lines.remove(lines[0])
# 下面两步实现把画面停在桌面上，而不是一闪而过（注：这样同时是相当于停住了程序的运行）
# plt.ioff()
# plt.show()      # 放在最后可以把画面停住


# --------- 优化器
# Stochastic Gradient Descent(SGD)随机梯度下降
# 每次随机抽取一小波数据来进行训练
# 是收敛最慢的一种优化方式（在莫大列出的几种方式中SGD、Monmentum、NAG、Adagrad、Adadelta、Rmsprop）
# 传统的更新方式 W += -下降效率*下降步伐——摇摇晃晃下山
# Momentum方式 沿着下坡更新
# AdaGrad方式  在学习率上下功夫，限制其沿着下降最快的方向走？
# RMSProp方式  上面两种方式的结合
# Adam方式     上一种方式的完善，实验证明又快又好
'''
tf的优化器：
class tf.train.GradientDescentOptimizer # 最重要、最基础
class tf.train.AdadeltaOptimizer        # ？不知道有没有
class tf.train.AdagradOptimizer         #
class tf.train.MomentumOptimizer        # 也常用
class tf.train.AdamOptimizer            # 也常用
class tf.train.FtrlOptimizer            #
class tf.train.RMSPropOptimizer         # AlphaGo用的
'''
# 比较快的优化器，有的会用到上一步的优化方向，在加速了步伐的同时，也带大了方向偏差，收敛可能会变快，但所走的路径不一定是最短的（步数会不会变少还不好说）


# ---------- 可视化tensorboard
#
# scalar标量？（比如loss），貌似tensorboard中必须有一个
# loss = ****
# tf.summary.scalar('loss/', loss)    # 在event中显示，看loss很重要
#
# graph框架图 && distribution分配分布？
# with tf.name_scope('x'):  # 这个scope会在显示的时候生成一个框，把这个with范围内的内容框在这个框下，name_scope会在tensorboard中生成一层目录
#   x = jfalji(fjaoef, name = 'x_show') # 这里的name是实际显示出来的name
#
# histograms直方图/柱状图，貌似tensorboard中必须有一个
# outputs = *****
# tf.summary.histogram(layer_name+'/outputs', outputs)
#
# tf.summary下面的一些列方法xxx('name', value)会记录一些键值，
# writer = tf.summary.FileWriter('log/', sess.graph)进行保存？
# 这样可以在tensorboard中显示折线图，某个量随步进的变化 
# train_writer.add_summary(train_result, i)
# test_writer.add_summary(test_result, i)
# writer.add_summary(result, step)
#
# tensorboard --logdir=log  # 前提需要进入log所在的目录下
# tensorboard --logdir=绝对路径  # 无需log所在的目录下
#
# 在cmd下这么搞的时候，要进入anconda环境下，路径需要加单引号（目前我还没搞成功）
#
#
# ----------------classification
# prediction = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2)+b_fc2)
#
#
# ----------- overfit
# 1.增加数据量
# 2.正则化（把f（参数）加入损失函数）
# 3.dropout正则化——神经网络中的正则化，在训练的时候， 每一轮随 机 忽略掉一些神经元和神经连接，
#   其实就是在计算完这一层的输出后，按概率随机扔掉一些值，然后再传给下一层
#   使神经网络变的不完整，这样就使得训练结果不会过分依赖于某部分特定的神经元
#
#   Wx_plus_b = tf.matmul(inputs, Weights) + biases
#   # dropout，减少原本这一层的输出的维度，保留keep_prob（一项概率值eg.80%）
#   Wx_plus_b = tf.nn.dropout(Wx_plus_b, keep_prob)
#
#
# ------------ convolution
## 来自弹幕的解释
# 一个卷积核对应一层，多少个卷积核对应多少层
# 一个卷积核是 kernelSzie * height * width * inputDepth * outputDepth, 层数的改变是通过outputDepth来改变的
# 一个卷积过程用到好几个卷积核，每个卷积核（过滤器）卷一遍，有几个卷积核卷的过程，结果就会被叠加成几层，所以就厚了
# stride——步长，大的步长是一种更粗的特征提取，也会加快特征提取的过程，可能会损失掉一些信息
# padding——填充，为了让卷积不减少图片尺寸
# pooling——池化，
## my word
# 原始的卷积只能把图像卷小，这丢失了边缘信息，如果隐层很多，图像可能就卷没了
# Valid and Same(need padding) convolutions
# 一次卷积是对所有层进行“卷”，一个卷积核的一轮卷积把整个数据的厚度压缩到一层
# 池化只要依次遍历所有层进行池化，池化的过滤器只有一层，是以池化操作不改变数据层数（厚度/channel）