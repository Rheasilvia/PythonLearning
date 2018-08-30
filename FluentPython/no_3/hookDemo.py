##hook demo
## 简单的接口应该接受函数，而不是类的实例。
import collections


# if __name__ == '__main__':
#     names = ['Socrates', 'Archimedes', 'Plato', 'Aristotle']
#     names.sort(key=lambda x: len(x))  # 根据长度排序
#     print(names)


class BetterCountMissing(object):
    def __init__(self):
        self.added = 0

    def __call__(self, *args, **kwargs):
        self.added += 1
        return 0


if __name__ == '__main__':
    current = {'green': 12, 'blue': 3}
    increments = [
        ('red', 5),
        ('blue', 17),
        ('orange', 9),
    ]
    """
    像这样修改后，defaultdict仍然无需关注__call__方法得到调用时的效果，
    而是只要求使用者传入一个用来生成默认值的挂钩函数即可。
    """
    counter = BetterCountMissing()
    result = collections.defaultdict(counter, current)

    for key, amount in increments:
        result[key] += amount
    print(counter.added == 2)
