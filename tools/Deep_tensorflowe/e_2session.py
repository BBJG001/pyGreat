import tensorflow as tf

# session拥有并管理TensorFlow程序运行时的所有资源，所有计算完成之后会话来帮助系统回收资源，以免资源泄露

matrix1 = tf.constant([[3, 3]])
matrix2 = tf.constant([[2], [2]])

product = tf.matmul(matrix1, matrix2)       # 矩阵乘法np.dot(m1, m2)

# method 1
sess = tf.Session()
result = sess.run(product)
print(result)
sess.close()

# method 2
with tf.Session() as sess:
    result = sess.run(product)
    print(result)
# with控制范围结束自动.close()