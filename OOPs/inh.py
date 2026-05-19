# # Python program to demonstrate
# # super()

# class Class1:
#     def m(self):

#         print("In Class1")

# class Class2(Class1):
#     def m(self):
     
#         print("In Class2")
#         super().m()
      

# class Class3(Class1):
#     def m(self):
    
#         print("In Class3")
#         super().m()
      

# class Class4(Class2, Class3):
#     def m(self):
     
#         print("In Class4")   
#         super().m()

       

     
# obj = Class4()
# obj.m()
# print(Class4.__mro__)

# Python program to show the order
# in which methods are resolved

class A:
    def rk(self):
        print("In class A")

class B:
    def rk(self):
        print("In class B")

# classes ordering
class C(A, B):
    def __init__(self):
        print("Constructor C")

r = C()

# it prints the lookup order 
print(C.__mro__)
print(C.mro())