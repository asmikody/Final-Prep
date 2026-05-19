# init method is never called
'''class  A:
    def __new__(cls):
        print("Creating class")
        return "Hello,World"
    def __init__(self):
        print("Initialzing class")
print(A())'''

# Returning an instances of another class
'''class A:
    def __str__(self):
        return "classA is called by classB as it returned it"
class B:
    def __new__(cls):
        print(":__new__ method of Geek returns an instance of A instead of B")
        return A()
    def __init__(self):
        print("Inside init")

print(B())'''

# Returning the values of new and init 
# '''
class A(object):
    def __new__(cls):
        print("Creating instance")
        return "GeeksforGeeks"

class B(object):
    def __init__(self):
        print("Initializing instance")
        return "GeeksforGeeks"

print(A())
print(B())
