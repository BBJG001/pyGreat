# coding=gbk
# ------------ convolution
## ���Ե�Ļ�Ľ���
# һ������˶�Ӧһ�㣬���ٸ�����˶�Ӧ���ٲ�
# һ��������� kernelSzie * height * width * inputDepth * outputDepth, �����ĸı���ͨ��outputDepth���ı��
# һ����������õ��ü�������ˣ�ÿ������ˣ�����������һ�飬�м�������˾�Ĺ��̣�����ͻᱻ���ӳɼ��㣬���Ծͺ���
# stride������������Ĳ�����һ�ָ��ֵ�������ȡ��Ҳ��ӿ�������ȡ�Ĺ��̣����ܻ���ʧ��һЩ��Ϣ
# padding������䣬Ϊ���þ��������ͼƬ�ߴ�
# pooling�����ػ���
## my word
# ԭʼ�ľ��ֻ�ܰ�ͼ���С���ⶪʧ�˱�Ե��Ϣ���������ܶ࣬ͼ����ܾ;�û��
# Valid and Same(need padding) convolutions
# һ�ξ���Ƕ����в���С�����һ������˵�һ�־�����������ݵĺ��ѹ����һ��
# �ػ�ֻҪ���α������в���гػ����ػ��Ĺ�����ֻ��һ�㣬���Գػ��������ı����ݲ��������/channel��

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# number 1 to 10
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)   # one_hot ���ȱ��루Դ�ڵ�Ļ��


def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases

    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs

# ����׼ȷ��
def compute_accuracy(v_xs, v_ys):
    # global prediction # ��һ��û���ܲ����У�Ŀ��ûʲô���⣬��������е�sess����Ҳû���ⲽ������ǰ���RL����Ҳ���ڶ���ķ�����ֱ�Ӿ�����
    y_pre = sess.run(prediction, feed_dict={xs: v_xs, keep_prob: 0.5})
    correct_prediction = tf.equal(tf.arg_max(y_pre, 1), tf.arg_max(v_ys, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))  # Ԥ����˾���1�����˾���0����ƽ��ֵ����׼ȷ��
    result = sess.run(accuracy, feed_dict={xs: v_xs, ys: v_ys})
    return result

# �����ʼ��Ȩ�ؾ���
def weight_variable(shape):
    inital = tf.truncated_normal(shape, stddev=0.1) # �������
    return tf.Variable(inital)

def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

def conv2d(x, W):
    # must have strides[0]=1, strides[1]=1
    return tf.nn.conv2d(x, W, strides=[1,1,1,1], padding='SAME') # strides ����[����ά�ȵĲ���], padding=SAME(������padding)/VALID

def max_pool_2x2(x):
    # must have strides[0]=1, strides[1]=1
    return tf.nn.max_pool(x, ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME')


# ����data_x��data_y�ĸ�ʽ/λ�ã�ͨ��placeholder��
xs = tf.placeholder(tf.float32, [None, 784])  # 28*28
ys = tf.placeholder(tf.float32, [None, 10])
keep_prob = tf.placeholder(tf.float32)
x_image = tf.reshape(xs, [-1, 28, 28, 1])   # [����������������channel��

# conv1 layer(conv and pooling)
W_conv1 = weight_variable([5, 5, 1, 32])   # patch 5x5��filter size��, in size 1��channel�ɣ�, out size 32(����˼��˵��32�������ȥ��ô��
b_conv1 = bias_variable([32])
h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)    # ���������    # output size 28x28x32
h_pool1 = max_pool_2x2(h_conv1)                                             # output size 14x14x32  because of stride

# conv2 layer
## ���������״����Ϊ���ʼ����������������Ҫѧϰ��
W_conv2 = weight_variable([5, 5, 32, 64])   # patch 5x5��filter size��, in size 32����һ������channel��, out size 64(64�������?��
b_conv2 = bias_variable([64])

## ������㣨������ʽ������� �� �ػ�
h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)    # ���������    # output size 14x14x64
h_pool2 = max_pool_2x2(h_conv2)                                             # output size 7x7x32  because of stride


# func1 layer��ȫ���Ӳ㣩
## ���������״����Ϊ���ʼ����������������Ҫѧϰ��
W_fc1 = weight_variable([7*7*64, 1024]) # ֱ�ӽ�������ƴ�Ӽӳ�
b_fc1 = bias_variable([1024])

h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])    # [n_samples, 7, 7, 64] ->> [n_samples, 7*7*64]
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1)+b_fc1)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

# func2 layer, ���һ���ˣ��͵��������
W_fc2 = weight_variable([1024, 10]) # ֱ�ӽ�������ƴ�Ӽӳ�
b_fc2 = bias_variable([10])

prediction = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2)+b_fc2)   # ��Ϊ�����һ���ˣ�������prediction
# h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)  # ��ѡ


# ������ʧ����
cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction), reduction_indices=[1]))  # ������

# ����ÿһ��ѵ������Ч��������do���ţ�С������ʧ����
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)   # �Ż������Ĳ�����learning rate

# ����һ����Ʒ��������Эͬ����ģ�
sess = tf.Session()

# ��ʼ�����б���
sess.run(tf.global_variables_initializer())

for step in range(10000):
    batch_xs, batch_ys = mnist.train.next_batch(100)  # ����ݶ��½���ѡһ��
    sess.run(train_step, feed_dict={xs: batch_xs, ys: batch_ys, keep_prob: 0.5})
    if step % 50 == 0:
        print(compute_accuracy(mnist.test.images, mnist.test.labels))