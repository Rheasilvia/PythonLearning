# 抽象类demo
from abc import ABCMeta, abstractmethod


class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbyte=1):
        pass

    @abstractmethod
    def write(self, data):
        pass


class StreanImp(IStream):

    def read(self, maxbyte=1):
        pass

    def write(self, data):
        pass


# abs必须要保持合适的顺序才能正常运行
class A(metaclass=ABCMeta):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    @classmethod
    @abstractmethod
    def method1(cls):
        pass

    @staticmethod
    @abstractmethod
    def method2(self):
        pass


if __name__ == '__main__':
    b = StreanImp()
    # a = IStream()# 抽象类不能实例化
