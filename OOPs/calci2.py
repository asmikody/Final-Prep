from abc import ABC,abstractmethod
class Calculate(ABC):
    @abstractmethod
    def calculate(self,a,b):
        pass
class BasicCal(Calculate):
    def __init__(self):
        self.__history = []

    def _add_to_history(self,operation,a,b):
        self.__history.append(f"{a} {operation} {b} : {result}")

    def calculate(self,a,b,operation):
        if operation == '+':
            result = a + b
        if operation == '-':
            result = a - b
        if operation == '*':
            result = a * b
        if operation == '/':
            result = a / b if b!=0 else "error:division by 0"
        else:
            return "invalid Operation"
        

        
        
        