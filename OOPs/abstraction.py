from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract class
    @abstractmethod
    def make_sound(self):  # Abstract method
        pass

    def sleep(self):  # Concrete method
        print("Sleeping...")

class Dog(Animal):  # Subclass
    def make_sound(self):  # Must implement abstract method
        print("Bark!")

# Usage
dog = Dog()
dog.make_sound()  # Output: Bark!
dog.sleep()       # Output: Sleeping...


print(" ") 

from abc import ABC, abstractmethod

class Shape(ABC):  # Interface-like abstract class
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):  # Subclass implementing the interface
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Usage
rect = Rectangle(5, 10)
print(rect.area())       # Output: 50
print(rect.perimeter())  # Output: 30
