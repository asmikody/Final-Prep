# Public Members
'''
class Public:
    def __init__(self):
        self.name = "Asmi"

    def display_name(self):
        print(self.name)

obj = Public()
# obj.display_name()
# print(obj.name)
'''
# Proected members:
'''
class Protected:
    def __init__(self):
        self._age = 40
class Subclass(Protected):
    def display(self):
        print(self._age)

obj = Subclass()
obj.display()
obj1 = Protected()
print(obj1._age)
'''
# Private Members
class Private:
    def __init__(self):
        self.__salary = 50000  # Private attribute

    def salary(self):
        return self.__salary  # Access through public method

obj = Private()
print(obj.salary())  # Works
print(obj.__salary)  # Raises AttributeError