## 用元类来注解类的属性

# Field描述符基本上不需要修改
class Field():
    def __init__(self):
        # This will be assigned by the metaclass
        self.name = None
        self.internal_name = None


class Meta(type):
    def __new__(meta, name, bases, class_dict):
        for key, value in class_dict.items():
            if isinstance(value, Field):
                value.name = key
                value.internal_name = '_' + key
        cls = type.__new__(meta, name, bases, class_dict)
        return cls


# 凡是数据库里面某一行的累，都应该从基类中继承
class DatabaseRow(object, metaclass=Meta):
    pass


# 数据行
class BetterCustomer(DatabaseRow):
    first_name = Field()
    last_name = Field()
    prefix = Field()
    suffix = Field()
    age = Field()


if __name__ == '__main__':
    foo = BetterCustomer()
    print('Before:', repr(foo.first_name), foo.__dict__)
    foo.first_name = 'Euler'
    foo.age = 23
    print('After:', repr(foo.first_name), foo.__dict__)
    print('After:', repr(foo.age), foo.__dict__)
