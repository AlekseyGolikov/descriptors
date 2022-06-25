"""
    __getattribute__(self, name) будет вызван при попытке получить значение атрибута.
    Если этот метод переопределён, стандартный механизм поиска значения атрибута не будет задействован.
    Следует иметь ввиду, что вызов специальных методов (например __len__(), __str__()) через встроенные функции
    или неявный вызов через синтаксис языка осуществляется в обход __getattribute__().
"""
class Optimist:
    attr = "class attribute"

    def __getattribute__(self, name):
        print("{0} is great!".format(name))

    def __len__(self):
        print("__len__ is special")
        return 0

o = Optimist()
o.instance_attr = "instance"

o.attr          # attr is great!             __getattribute__ будет вызван
o.dark_beer     # dark_beer is great!        __getattribute__ будет вызван
o.instance_attr # instance_attr is great!    __getattribute__ будет вызван
o.__len__       # __len__ is great!          __getattribute__ будет вызван
len(o)          # __len__ is special\n 0     __getattribute__ не будет вызван
