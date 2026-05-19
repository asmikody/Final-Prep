# class Outer:
#     def __init__(self,name,rollno):
#         self.name = name
#         self.rollno = rollno
#         self.lap = self.Laptop()

#     def show(self):
#         print(self.name,self.rollno)

#     class Laptop:

#         def __init__(self):
#             self.brand = "HP"
#             self.cpu = "i5"
#             self.ram = "8gb"  

# s1 = Outer('asmi',10)
# s2 = Outer("adi",23)

# s1.show()

# lap1 = s1.lap
# lap2 = s2.lap 
'''If an object is created using child class means inner class then the object can also be used by parent class or root class. A parent class can have one or more inner classes but generally inner classes are avoided.

We can make our code even more object-oriented by using an inner class. A single object of the class can hold multiple sub-objects. We can use multiple sub-objects to give a good structure to our program.'''

class Color:
    def __init__(self):
        self.name = 'Green'
        # inner class object is being created here 
        self.lg = self.lightgreen()     
    def show(self):
        print("Name",self.name)
    # inner class is created

    class lightgreen:
        def __init__(self):
            self.name = 'lightgreen'
            self.shade = "light"
        def display(self):
            print("name",self.name)
            print("shade",self.shade)

#creating classs object
outer =  Color()
outer.show()
# creatin the lightgreen inner class object
g = outer.lg
g.display()