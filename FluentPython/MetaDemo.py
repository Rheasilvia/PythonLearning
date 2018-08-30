# 利用元类来验证子类

class ValidatePolygon(type):  ##必须继承自type
    def __new__(meta, name, bases, class_dict):
        # Don't validate the abstract Polygon class
        if bases != (object,):
            if class_dict['sides'] < 3:
                raise ValueError('Polygons need 3+ sides')
        return type.__new__(meta, name, bases, class_dict)


class Polygon(object, metaclass=ValidatePolygon):
    sides = None  # specified by subclasses

    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180


class Triangle(Polygon):
    sides = 3

if __name__ == '__main__':
    print('Before class')
    class Line(Polygon):
        print('before sides')
        sides = 1
        print('After sides')
