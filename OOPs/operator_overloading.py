'''
class A:
    def __init__(self,a):
        self.a = a 
    def __add__(self,o):
        return self.a - o.a
ob1 = A(6.6)
ob2 = A(2)
ob3 = A("geeks")
ob4 = A("for")

print(ob1 + ob2)
# print(ob3 + ob4)

print(A.__add__(ob1,ob2))
print(ob1.__add__(ob2))'''

#Complex Number
# class Complex:
#     def __init__(self,A,B):
#         self.A = A
#         self.B = B 
#     def __add__(self,other):
#         return self.A + other.A , self.B + other.B
# obj1 = Complex(3,5)
# obj2 = Complex(2,3)
# obj3 = obj1 + obj2
# print(obj3)

# Python Program to perform addition 
# of two complex numbers using binary 
# + operator overloading.
'''
class complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

     # adding two objects 
    def __add__(self, other):
        return self.a + other.a, self.b - other.b

Ob1 = complex(3, 5)
Ob2 = complex(2, 3)
Ob3 = Ob1 + Ob2
print(Ob3)'''

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"({self.x}, {self.y})"

#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Point(x, y)

# p1 = Point(1, 2)
# p2 = Point(2, 3)
# print(p1 + p2)  # Output: (3, 5)

# class complex:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#      # adding two objects 
#     def __add__(self, other):
#         return self.a + other.a, self.b + other.b

# Ob1 = complex(1, 2)
# Ob2 = complex(2, 3)
# Ob3 = Ob1 + Ob2
# print(Ob3)

# class A:
#     def __init__(self, a):
#         self.a = a

#     # adding two objects 
#     def __add__(self, o):
#         return self.a + o.a 
# ob1 = A(1)
# ob2 = A(2)
# ob3 = A("Geeks")
# ob4 = A("For")

# print(ob1 + ob2)
# print(ob3 + ob4)

# Python program to demonstrate 
# Defining parent class 
class Parent(): 
	
	# Constructor 
	def __init__(self): 
		self.value = "Inside Parent"
		
	# Parent's show method 
	def show(self): 
		print(self.value) 
		
# Defining child class 
class Child(Parent): 
	
	# Constructor 
	def __init__(self): 
		# super().__init__()  # Call parent constructor
		self.value = "Inside Child"
		
	# Child's show method 
	def show(self): 
		print(self.value) 
		
# Driver's code 
obj1 = Parent() 
obj2 = Child() 

obj1.show()  # Should print "Inside Parent"
obj2.show()  # Should print "Inside Child"