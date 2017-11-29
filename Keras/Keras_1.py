from keras.models import Sequential
from keras.layers import Dense, Activation

# 方式一通过sequential模型传递 layer构造模型
# model = Sequential([
#     Dense(32, units=784),
#     Activation('rule'),
#     Dense(10),
#     Activation('softmax'),
# ])

# 方式二，通过add()
# model = Sequential()
# model.add(Dense(32, input_shape=(784,)))
# model.add(Activation('rule'))


# 指定shape，会自动推导中间数据的shape
model = Sequential()
model.add(Dense(32, input_dim=784))

model = Sequential()
model.add(Dense(32, input_shape=(784,)))

# 编译需要设置

model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

# 训练
model = Sequential()
model.add(Dense(32, activation='relu', input_dim=100))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])

#generate dummy data
import numpy as np
data = np.random.random((1000,100))
labels = np.random.randint(2,size=(1000,1))

#训练模型，迭代数据，batch为32个样本
model.fit(data,labels,epochs=10,batch_size=32)
