# coding=gbk
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

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# number 1 to 10
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)   # one_hot 独热编码（源于弹幕）


def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases

    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs

# 计算准确率
def compute_accuracy(v_xs, v_ys):
    # global prediction # 这一步没有能不能行，目测没什么问题，下面的其中的sess对象也没有这步操作，前面的RL对象也是在定义的方法中直接就用了
    y_pre = sess.run(prediction, feed_dict={xs: v_xs, keep_prob: 0.5})
    correct_prediction = tf.equal(tf.arg_max(y_pre, 1), tf.arg_max(v_ys, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))  # 预测对了就是1，错了就是0，求平均值就是准确率
    result = sess.run(accuracy, feed_dict={xs: v_xs, ys: v_ys})
    return result

# 随机初始化权重矩阵
def weight_variable(shape):
    inital = tf.truncated_normal(shape, stddev=0.1) # 随机生成
    return tf.Variable(inital)

def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

def conv2d(x, W):
    # must have strides[0]=1, strides[1]=1
    return tf.nn.conv2d(x, W, strides=[1,1,1,1], padding='SAME') # strides 步长[各个维度的步长], padding=SAME(就是有padding)/VALID

def max_pool_2x2(x):
    # must have strides[0]=1, strides[1]=1
    return tf.nn.max_pool(x, ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME')


# 定义data_x和data_y的格式/位置（通过placeholder）
xs = tf.placeholder(tf.float32, [None, 784])  # 28*28
ys = tf.placeholder(tf.float32, [None, 10])
keep_prob = tf.placeholder(tf.float32)
x_image = tf.reshape(xs, [-1, 28, 28, 1])   # [样例数，长，宽，厚（channel）

# conv1 layer(conv and pooling)
W_conv1 = weight_variable([5, 5, 1, 32])   # patch 5x5（filter size）, in size 1（channel吧）, out size 32(这意思是说用32个卷积核去卷么）
b_conv1 = bias_variable([32])
h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)    # 激活函数激活    # output size 28x28x32
h_pool1 = max_pool_2x2(h_conv1)                                             # output size 14x14x32  because of stride

# conv2 layer
## 定义参数形状，并为其初始化，这两个参数是要学习的
W_conv2 = weight_variable([5, 5, 32, 64])   # patch 5x5（filter size）, in size 32（上一层的输出channel）, out size 64(64个卷积核?）
b_conv2 = bias_variable([64])

## 定义计算（处理）方式——卷积 和 池化
h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)    # 激活函数激活    # output size 14x14x64
h_pool2 = max_pool_2x2(h_conv2)                                             # output size 7x7x32  because of stride


# func1 layer（全连接层）
## 定义参数形状，并为其初始化，这两个参数是要学习的
W_fc1 = weight_variable([7*7*64, 1024]) # 直接将卷积结果拼接加长
b_fc1 = bias_variable([1024])

h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])    # [n_samples, 7, 7, 64] ->> [n_samples, 7*7*64]
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1)+b_fc1)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

# func2 layer, 最后一层了，就当做输出层
W_fc2 = weight_variable([1024, 10]) # 直接将卷积结果拼接加长
b_fc2 = bias_variable([10])

prediction = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2)+b_fc2)   # 因为是最后一层了，就用了prediction
# h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)  # 可选


# 定义损失函数
cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction), reduction_indices=[1]))  # 交叉熵

# 定义每一轮训练的有效动作——do最优（小）化损失函数
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)   # 优化器传的参数是learning rate

# 定义一个产品经理（进行协同调配的）
sess = tf.Session()

# 初始化所有变量
sess.run(tf.global_variables_initializer())

for step in range(10000):
    batch_xs, batch_ys = mnist.train.next_batch(100)  # 随机梯度下降，选一份
    sess.run(train_step, feed_dict={xs: batch_xs, ys: batch_ys, keep_prob: 0.5})
    if step % 50 == 0:
        print(compute_accuracy(mnist.test.images, mnist.test.labels))