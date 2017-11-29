from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets(".", one_hot=True, reshape=False)


import tensorflow as tf

# 参数 Parameters
learning_rate = 0.001
training_epochs = 20
batch_size = 128  # 如果没有足够内存，可以降低 batch size
display_step = 1

n_input = 784  # MNIST data input (img shape: 28*28)
n_classes = 10  # MNIST total classes (0-9 digits)

n_hidden_layer = 256 # layer number of features 特征的层数


# Store layers weight & bias
# 层权重和偏置项的储存
weights = {
    'hidden_layer': tf.Variable(tf.random_normal([n_input, n_hidden_layer])),
    'out': tf.Variable(tf.random_normal([n_hidden_layer, n_classes]))
}
biases = {
    'hidden_layer': tf.Variable(tf.random_normal([n_hidden_layer])),
    'out': tf.Variable(tf.random_normal([n_classes]))
}


# tf Graph input
x = tf.placeholder("float", [None, 28, 28, 1])
y = tf.placeholder("float", [None, n_classes])

x_flat = tf.reshape(x, [-1, n_input])


# Hidden layer with RELU activation
# ReLU作为隐藏层激活函数
layer_1 = tf.add(tf.matmul(x_flat, weights['hidden_layer']),\
    biases['hidden_layer'])
layer_1 = tf.nn.relu(layer_1)
# Output layer with linear activation
# 输出层的线性激活函数
logits = tf.add(tf.matmul(layer_1, weights['out']), biases['out'])


# Define loss and optimizer
# 定义误差值和优化器
cost = tf.reduce_mean(\
    tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)\
    .minimize(cost)


# Initializing the variables
# 初始化变量
init = tf.global_variables_initializer()

# Launch the graph
# 启动图
with tf.Session() as sess:
    sess.run(init)
    # Training cycle
    # 训练循环
    for epoch in range(training_epochs):
        total_batch = int(mnist.train.num_examples/batch_size)
        # Loop over all batches
        # 遍历所有 batch
        for i in range(total_batch):
            batch_x, batch_y = mnist.train.next_batch(batch_size)
            # Run optimization op (backprop) and cost op (to get loss value)
            # 运行优化器进行反向传导、计算 cost（获取 loss 值）
            sess.run(optimizer, feed_dict={x: batch_x, y: batch_y})