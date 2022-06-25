"""
    __getattr__(self, name) будет вызван в случае, если запрашиваемый атрибут не найден обычным механизмом
    (в __dict__ экземпляра, класса и т.д.):
"""
class SmartyPants:
    def __getattr__(self, attr):
        print("Yep, I know", attr)
    tellme = "It's a secret"

smarty = SmartyPants()
smarty.name = "Smartinius Smart"

smarty.quicksort    # Yep, I know quicksort        __getattr__ будет вызван
smarty.python       # Yep, I know python           __getattr__ будет вызван
smarty.tellme       # "It's a secret"              __getattr__ не будет вызван
smarty.name         # "Smartinius Smart"           __getattr__ не будет вызван
