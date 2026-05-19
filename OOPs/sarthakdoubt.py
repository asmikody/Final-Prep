#parent class or base class
class Person:
    def __init__ (self,name,age):
       
        self.name=name
        self.age=age
       
     #method to be over-ridden
    def details(self):    
                                       
        print(f'Student Name: {self.name}, Age: {self.age}')
 
#inherited class student
class Student(Person):
    def __init__ (self,name,age,enrollment_number):

        Person.__init__(self,name,age)
        super().__init__(name,age)
        #encapsulation (private)
        self.enrollment_number = enrollment_number
   
    #method override(polymorphism)
    def details(self):
        super().details()
        print(f'Enrollment_number: {self.enrollment_number}')
       
       
    #inherited class professor  
class Professor(Person):
    def __init__(self,name,age,subject,designation):
        Person.__init__(self,name,age)
        self.subject =subject
        self.designation=designation
       
    def details(self):
        super().details()
        print(f' Subject: {self.subject}, Designation: {self.designation}')
 
#object creation
obj1= Student('Sarthak',20,"EN21CS301695")
obj1.details()        #details function call
 
obj2=Professor("Ramprasad",34,"physics","assistant professor")
obj2.details()
 