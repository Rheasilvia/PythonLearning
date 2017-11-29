import tensorflow as tf

# 随机生成数据模拟数据集
from numpy.random import RandomState

# 定义训练集batch大小
batch_size = 8

w1 = tf.Variable(tf.random_normal([2, 3], stddev=1, seed=1))
w2 = tf.Variable(tf.random_normal([3, 1], stddev=1, seed=1))

# 在shape上使用None可以方便使用不同的batch大小，在训练时候需要吧数据集分成比较小的batch,
# 但测试时候，需要一次性使用全部数据。当数据集较小的时候这样比较方便，但是在数据集较大的时候，将大量数据放入一个batch会导致内存溢出

x = tf.placeholder(tf.float32, shape=(None, 2), name='x-input')
y_ = tf.placeholder(tf.float32, shape=(None, 1), name='y-input')

a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

# 定义损失函数和反向传播算法
cross_entryopy = -tf.reduce_mean(y_ * tf.log(tf.clip_by_value(y, 1e-10, 1.0)))
train_step = tf.train.AdamOptimizer(0.001).minimize(cross_entryopy)  # 获取最小损失函数

# 通过随机数生成一个模拟数据集
rdm = RandomState()
dataset_size = 128
X = rdm.rand(dataset_size, 2)

# 定义样本标签，x1+x2<1认为是正样本，其他为负样本,在这里0表示负样本，1表示正样本
Y = [[int(x1 + x2 < 1)] for (x1, x2) in X]

with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)
    print(sess.run(w1))
    print(sess.run(w2))

    # 设置训练论述
    STEPS = 5000
    for i in range(STEPS):
        # 每次选取batch_size个样本进行训练
        start = (i * batch_size) % dataset_size
        end = min(start + batch_size, dataset_size)

        # 通过选取样本训练神经网络并更新参数
        sess.run(train_step, feed_dict={x: X[start:end], y_: Y[start:end]})

        if i % 1000 == 0:
            # 每隔一段时间计算在所有数据上的交叉熵并输出
            total_cross_entropy = sess.run(cross_entryopy, feed_dict={x: X, y_: Y})
            print("After %d training step(s),cross entropy on all data is %g " % (i, total_cross_entropy))

        print(sess.run(w1))
        print(sess.run(w2))

