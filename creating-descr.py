"""
    Создание свойства с помощью дескриптора
"""
class Descriptor:
    def __get__(self, obj, type):
        print("getter used")
    def __set__(self, obj, val):
        print("setter used")
    def __delete__(self, obj):
        print("deleter used")

class MyClass:
    prop = Descriptor()
    print(prop)     # <__main__.Descriptor object at 0x7f5a8bf93df0>