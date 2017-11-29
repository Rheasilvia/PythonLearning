def myfunc(*argc):
    for a in argc:
        print(a, end=' ')
    if argc:
        print()


def myfunc2(**kwargs):
    for k, v in kwargs.items():
        print(k, v, sep='->', end=' ')
    if kwargs:
        print()


def myfunc3(*args, **kwargs):
    if args:
        for a in args:
            print(a, end=' ')
        print()
    if kwargs:
        for i in kwargs.items():
            for k, v in kwargs.items():
                print(k, v, sep='->', end=' ')
            print()


if __name__ == "__main__":
    myfunc3(1, 2, 3, 4, a=10, b=2)
