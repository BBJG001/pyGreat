import tensorflow as tf
import torch
import numpy as np

onehot_labels = [[0,0,1,0,0],
                  [0,0,0,1,0],
                  [0,1,0,0,0],
                  [1,0,0,0,0]]
labels = np.argmax(onehot_labels, axis=1)
# [2 3 1 0]
logits = [[-1.1258, -1.1524, -0.2506, -0.4339,  0.5988],
          [-1.5551, -0.3414,  1.8530,  0.4681, -0.1577],
          [ 1.4437,  0.2660,  1.3894,  1.5863,  0.9463],
          [-0.8437,  0.9318,  1.2590,  2.0050,  0.0537]]

# 转成tf可以处理的张量
tflabels = tf.constant(labels)
tflabels_oh = tf.constant(onehot_labels)
tflogits = tf.constant(logits)

tfloss = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=tflabels, logits=tflogits)
# 可以直接传入类别标号
tfloss_oh = tf.nn.softmax_cross_entropy_with_logits(labels=tflabels_oh, logits=tflogits)
# 需要传入onehot变化后的类别数据

with tf.Session() as sess:
    lossvalue = sess.run(tfloss)
    loss_oh_value = sess.run(tfloss_oh)
    print('tfloss\t\t', lossvalue)
    print('tfloss_oh\t', loss_oh_value)

# 转成pytorch可以识别的张量
ptlabels = torch.tensor(labels).int()
ptlogits = torch.tensor(logits)

ptloss = torch.nn.CrossEntropyLoss(reduce=False)(ptlogits, ptlabels.long())
ptloss2 = torch.nn.NLLLoss(reduce=False)(torch.nn.LogSoftmax(dim=-1)(ptlogits), ptlabels.long())
print('ptloss:\t\t', ptloss)
print('ptloss2:\t', ptloss2)

# tfloss		 [1.6081128 1.8093656 2.5681138 3.5499053]
# tfloss_oh	 [1.6081128 1.8093656 2.5681138 3.5499053]
# ptloss:		 tensor([1.6081, 1.8094, 2.5681, 3.5499])
# ptloss2:	 tensor([1.6081, 1.8094, 2.5681, 3.5499])