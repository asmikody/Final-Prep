
from abc import ABC, abstractmethod

# Abstraction: Abstract base class for Calculator
class Calculator(ABC):
    @abstractmethod
    def calculate(self, a, b):
        pass

# Encapsulation: Base class with private attributes and methods
class BasicCalculator(Calculator):
    def __init__(self):
        self.__history = []  # Private attribute to store calculation history

    def __add_to_history(self, operation, a, b, result):  # Private method
        self.__history.append(f"{a} {operation} {b} = {result}")

    def calculate(self, a, b, operation):
        if operation == '+':
            result = a + b
        elif operation == '-':
            result = a - b
        elif operation == '*':
            result = a * b
        elif operation == '/':
            result = a / b if b != 0 else "Error: Division by zero"
        else:
            return "Invalid operation"
        
        self.__add_to_history(operation, a, b, result)
        return result

    def get_history(self):  # Public method to access private history
        return self.__history

# Inheritance: AdvancedCalculator inherits from BasicCalculator
class AdvancedCalculator(BasicCalculator):
    def calculate(self, a, b, operation):
        if operation == '**':  # Power operation
            result = a ** b
        elif operation == '%':  # Modulus operation
            result = a % b
        else:
            # Polymorphism: Calls the parent class's calculate method
            result = super().calculate(a, b, operation)
        return result

# Polymorphism: Unified interface for different calculator types
def perform_calculation(c1, a, b, operation):
    return c1.calculate(a, b, operation)

# Example Usage
if __name__ == "__main__":
    basic_calc = BasicCalculator()
    advanced_calc = AdvancedCalculator()

    print("Basic Calculator:")
    print(perform_calculation(basic_calc, 10, 5, '+'))  # 15
    print(perform_calculation(basic_calc, 10, 5, '-'))  # 5
    print(basic_calc.get_history())  # View history

    print("\nAdvanced Calculator:")
    print(perform_calculation(advanced_calc, 2, 3, '**'))  # 8
    print(perform_calculation(advanced_calc, 10, 3, '%'))  # 1
    print(perform_calculation(advanced_calc, 10, 5, '*'))  # 50
    print(advanced_calc.get_history())  # View history

# Explanation of OOP Concepts:

# Encapsulation:

# The __history attribute and __add_to_history method in BasicCalculator are private, ensuring data is hidden and only accessible through public methods like get_history.

# Abstraction:

# The Calculator class is an abstract base class with an abstract method calculate, forcing derived classes to implement it.

# Inheritance:

# AdvancedCalculator inherits from BasicCalculator and extends its functionality with additional operations like power (**) and modulus (%).

# Polymorphism:

# The perform_calculation function works with both BasicCalculator and AdvancedCalculator, demonstrating polymorphism by using a unified interface.

# This program is modular, reusable, and demonstrates all the core OOP principles effectively.