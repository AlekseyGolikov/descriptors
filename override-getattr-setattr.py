"""
    При переопределении __getattribute__(), __setattr__() и __delattr__() следует иметь ввиду,
    что стандартный способ получения доступа к атрибутам можно вызвать через object
"""
class GentleGuy:
    def __getattribute__(self, name):
        if name.endswith("_please"):
            return object.__getattribute__(self, name.replace("_please", ""))
        raise AttributeError("And the magic word!?")

gentle = GentleGuy()

gentle.coffee = "some coffee"
gentle.coffee           # AttributeError
gentle.coffee_please    # "some coffee"
