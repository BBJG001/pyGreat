

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
