"""
    Встроенный класс property представляет собой дескриптор данных
    Вывод:
        <property object at 0x7f8ab8b78180>
        12
"""
class MyClass:

    def _getter(self):
        print("getter used")
    def _setter(self, val):
        print("setter used")
    def _deleter(self):
        print("deleter used")

    pty = property(_getter, _setter, _deleter, "doc string")

o = MyClass
print(o.pty)    # <property object at 0x7f8ab8b78180>
o.pty = 12
print(o.pty)    # 12