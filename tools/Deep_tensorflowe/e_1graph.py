import tensorflow as tf
# Graph()框出一个范围，用来隔离张量和计算，还可以通过tf.Graph.device指定设备，与其他graph下的变量隔离
# collection属于计算图

g1 = tf.Graph()
with g1.as_default():
    v = tf.get_variable('v', shape=[1], initializer=tf.ones_initializer)

with g1.device('/cpu:0'):
    result = v * 3

with tf.Session(graph=g1) as sess:
    tf.global_variables_initializer().run()
    print(sess.run(result)) # 必须得run才能获得值
    with tf.variable_scope('', reuse=True):
        print(sess.run(tf.get_variable('v')))