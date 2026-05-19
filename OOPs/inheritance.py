# Inheritance
'''class Animal:
    def __init__(self,species):
        self.species = species

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.species} barks!"

dog = Dog("BUDDY")
print(dog.speak())'''

'''class Person(obj):
    def __init__(self,name,employee_id):
        self.name = name
        self.employee_id = employee_id

    def display(self):
        print(f"{self.name} {self.employee_id}")

class Employee(Person):
    def __init__(self,name,employee_id,salary,post):
        super().__init__(name,employee_id)
        self.salary = salary
        self.post = post'''


'''class Parent():
    def __init__(self):
        self.value = "Inside Parent"
    def speak(self):
        print(self.value)

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.value = "Inside Child"
    def speak(self):
        print(self.value)

obj1 = Parent()
obj2 = Child()
# obj1.speak()
obj2.speak()
''' 

# Multiple Inheritance 
# When a class is derived from more than one base class it is called multiple Inheritance

# Program to define the use of super() 
# function in multiple inheritance 
'''' class GFG1: 
	def __init__(self): 
		print('HEY !!!!!! GfG I am initialised(Class GEG1)') 
	
	def sub_GFG(self, b): 
		print('Printing from class GFG1:', b) 
	
# class GFG2 inherits the GFG1 
class GFG2(GFG1): 
	def __init__(self): 
		print('HEY !!!!!! GfG I am initialised(Class GEG2)') 
		super().__init__() 
	
	def sub_GFG(self, b): 
		print('Printing from class GFG2:', b) 
		super().sub_GFG(b + 1) 
	
# class GFG3 inherits the GFG1 ang GFG2 both 

class GFG3(GFG2): 
	def __init__(self): 
		print('HEY !!!!!! GfG I am initialised(Class GEG3)') 
		super().__init__() 
	
	def sub_GFG(self, b): 
		print('Printing from class GFG3:', b) 
		super().sub_GFG(b + 1) 
	
	
# main function 
if __name__ == '__main__': 
	
	# created the object gfg 
	gfg = GFG3() 
	
	# calling the function sub_GFG3() from class GHG3 
	# which inherits both GFG1 and GFG2 classes 
	gfg.sub_GFG(10)
'''	

# Practise of super for init method
class A:
    def __init__(self):
        print("This is classs A")

    def sub_A(self,b):
        print("priniitng the b of class A",b)

class B(A):
    def __init__(self):
        print("this is class B")
        # super().__init__()
		
    def sub_A(self,b):
        print("printing b of  class B ",b)
        super().sub_A(b+1)

class C(B):
    def __init__(self):
        print("this is class C")
        # super().__init__()
        
    def sub_A(self,b):
       
        
        print("priniting b of class C",b)
        super().sub_A(b+1)
obj = C()
obj.sub_A(10)