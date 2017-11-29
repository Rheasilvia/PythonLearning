import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# 输入节点数
INPUT_NODE = 784
OUTPUT_NODE = 10

# 配置神经网络的参数,隐藏层节点
LAYER1_NODE = 500
BATCH_SIZE = 100

# 随机梯度下降。数字越大，训练越接近梯度下降
LEARING_RATE_BASE = 0.8  # 基础学习率
LEARING_RATE_DECAY = 0.99  # 学习衰减率
REGULARIZATION_RATE = 0.0001  # 损失函数系数
TRAINING_STEPS = 30000  # 训练轮数
MOVING_AVERAGE_DECAY = 0.99  # 滑动平均衰减率


# 计算前向传播
def inference(input_tensor, avg_class, weight1, biases1, weights2, biases2):
    if avg_class == None:
        layer1 = tf.nn.relu(tf.matmul(input_tensor, weight1) + biases1)
        return tf.matmul(layer1, weights2) + biases2
    else:
        layer1 = tf.nn.relu(tf.matmul(input_tensor, avg_class.average(weight1)) + avg_class.average(biases1))
        return tf.matmul(layer1, avg_class.average(weights2)) + avg_class.average(biases2)

#训练模型
