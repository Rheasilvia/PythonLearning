class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)  # 保存成字典
            return value


import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('Computing ares')
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius


if __name__ == '__main__':
    c = Circle(4.0)
    print(c)

    print(c.area)
    print(c.area)  # 只打印一次

    print(c.perimeter)
    print(c.perimeter)

    print(vars(c))
