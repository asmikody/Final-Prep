# Que 1: Write a program to manage a shopping cart using functions. 
# Include a global cart_total variable and show how local and global variables work when 
# adding items

class Shopping_cart:
    cart_total = 0 
    def __init__(self,items):
        self.items = items
    def additems(self):
        additems += 1
    def removeitems(self):


'''Que 4: Build a calculator that performs addition, subtraction, multiplication, or division 
based on user input. 
Handle division by zero and invalid operations'''

class Calculator:
    def __init__(self,a,b):
        self.a = a 
        self.b = b


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
        

        
        
        