
class NonNegative:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Cannot be negative")
        return instance.__dict__[self.name]

class Object:

    name = NonNegative('name')

    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    c = Object(-10)