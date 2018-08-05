# 方式一(简单)
# class A:
#     def spam(self, x):
#         pass
#
#     def foo(self):
#         pass
#
#
# class B:
#     def __init__(self):
#         self._a = A()
#
#     def spam(self, x):
#         return self._a.foo()
#
#     def foo(self):
#         return self._a.foo()
#
#     def bar(self):
#         pass

# 方式二
# class A:
#     def spam(self, x):
#         pass
#
#     def foo(self):
#         pass
#
#
# class B:
#     def __init__(self):
#         self._a = A()
#
#     def bar(self):
#         pass
#
#     def __getattr__(self, name):
#         return getattr(self._a, name)
#
#
# if __name__ == '__main__':
#     b = B()
#     b.bar()
#     b.spam(32)

# 方式3
class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        print('getattr:', name)
        return getattr(self._obj, name)

    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            print('setattr:', name, value)
            setattr(self._obj, name, value)

    def __delattr__(self, item):
        if item.startswith('_'):
            super().__delattr__(item)
        else:
            print('delattr:', item)
            delattr(self._obj, item)


# 使用
class Spam:
    def __init__(self, x):
        self.x = x

    def bar(self, y):
        print('Spam.bar', self.x, y)


if __name__ == '__main__':
    s = Spam(2)
    p = Proxy(s)

    print(p.x)
    print('*' * 20)
    print(p.bar(3))
    print('*' * 20)
    p.x = 37
    print(p.x)
