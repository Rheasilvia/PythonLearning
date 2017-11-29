#  -*- coding: utf-8 -*-
import numpy as np
class Network(object):
    def __init__(self,sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.rand(y,1) for y in sizes[1:]] #随机从正态分布（均值0，方差1）中生成
        self.weights = [np.random.rand(y,x)
                        for x,y in zip(sizes[:1],sizes[1:])]# 存储连接第二层和第三层的权重

