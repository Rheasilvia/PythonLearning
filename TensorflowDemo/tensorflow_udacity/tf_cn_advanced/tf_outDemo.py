import tensorflow as tf

# 计算卷积输出大小
input = tf.placeholder(tf.float32, (None, 32, 32, 3))
filter_weights = tf.Variable(tf.truncated_normal((8, 8, 3, 20)))  # (height,width,input_dept,output_depth)
filter_bias = tf.Variable(tf.zeros(20))
strides = [1, 2, 2, 1]
padding = 'VALID'
'''
new_height = (input_height - filter_height + 2 * P)/S + 1
new_width = (input_width - filter_width + 2 * P)/S + 1
'''
conv = tf.nn.conv2d(input, filter_weights, strides, padding) + filter_bias
