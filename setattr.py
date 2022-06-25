"""
    __setattr__(self, name, value) будет вызван при попытке установить значение атрибута экземпляра. Аналогично __getattribute__(), если этот метод переопределён,
    стандартный механизм установки значения не будет задействован:
    __delattr__(self, name) — аналогичен __setattr__(), но используется при удалении атрибута.
"""
class NoSetters:
    attr = "class attribute"
    def __setattr__(self, name, val):
        print("not setting {0}={1}".format(name,val))

no_setters = NoSetters()
no_setters.a = 1            # not setting a=1        __setattr__ будет вызван
no_setters.attr = 1         # not setting attr=1     __setattr__ будет вызван
no_setters.__dict__         # {}
no_setters.attr             # "class attribute"
no_setters.a                # AttributeError
