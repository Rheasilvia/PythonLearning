def apply_async(func, args, *, callback):
    # computer the result
    result = func(*args)
    # invoke the callback with the result
    callback(result)


def print_result(result):
    print('Got:', result)


def add(x, y):
    return x + y


def make_handler():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))


class SequenceNo:
    def __init__(self):
        self.sequence = 0


def handler1(result, seq):
    seq.sequence += 1
    print('[{}] Got:{}'.format(seq.sequence, result))


if __name__ == '__main__':
    # callback函数回调
    apply_async(add, (2, 3), callback=print_result)

    print('-' * 20)

    apply_async(add, ('hello', 'world'), callback=print_result)

    print('-' * 20)
    # 利用协程完成回调
    handler = make_handler()
    next(handler)
    apply_async(add, (2, 3), callback=handler.send)

    print('-' * 20)
    # 利用额外参数回调
    seq = SequenceNo()
    from functools import partial

    apply_async(add, (2, 3), callback=partial(handler1, seq=seq))

    print('-' * 20)
    # 利用lambda回调
    apply_async(add, (2, 3), callback=lambda r: handler1(r, seq))
