# 描述一种类型检查属性
class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected ' + str(self.expected_type))
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


# 类装饰器来选择属性
def typeassert(**kwargs):
    """type info"""

    def decorate(cls):
        for name, expected_type in kwargs.items():
            # 附加类型描述给类
            setattr(cls, name, Typed(name, expected_type))
        return cls

    return decorate


# 实例
@typeassert(name=str, shares=int, price=float)
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


if __name__ == '__main__':
    s = Stock('haha', 23, 11.3)
    print(s)
