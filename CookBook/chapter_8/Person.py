class Person:
    def __init__(self, name):
        self.name = name

    #getter
    @property
    def name(self):
        return self._name

    #setter
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    #deleter
    @name.deleter
    def name(self):
        raise  AttributeError("Can't delete attr")

class SubPerson(Person):
    """扩展name属性"""
    #只使用property属性是不够的
    # @property
    # def name(self):
    #     print('Getting name')
    #     return super().name
    #
    # @name.setter
    # def name(self,value):
    #     print('Setting name to',value)
    #     super(SubPerson,SubPerson).name.__set__(self,value)
    #
    # @name.deleter
    # def name(self):
    #     print('Deleting name')
    #     super(SubPerson,SubPerson).name.__delete__(self)

    #只扩展一个方法
    # @Person.name.getter
    # def name(self):
    #     print('Getting name')
    #     return super().name

    #之扩展setting
    # @Person.name.setter
    # def name(self,value):
    #     print('Setting name to',value)
    #     super(SubPerson,SubPerson).name.__set__(self,value)

    @Person.name.getter
    def name(self):
        print('Getting name')
        return super().name


if __name__ == '__main__':
    s = SubPerson('Guido')
    s.name
    # s.name = 'Larry'
    # s.name = 32