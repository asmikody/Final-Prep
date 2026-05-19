# code
class Person:

    # Constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id

    # To check if this person is an employee
    def Display(self):
        print(self.name, self.id)
    

class Emp(Person):
    
    def __init__(self, name, id):
        super().__init__(name,id)
        # self.name_ = name

    def Print(self):
        print("Emp class called")

Emp_details = Emp("Mayank", 103)

# calling parent class function
print(Emp_details.name, Emp_details.id)

# code
# A Python program to demonstrate inheritance

class Person:

    # Constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id

    # To check if this person is an employee
    def Display(self):
        print(self.name, self.id)
    

class Emp(Person):
    
    def __init__(self, name, id):
        self.name_ = name
        super().__init__(name, id)

    def Print(self):
        print("Emp class called")

Emp_details = Emp("Mayank", 103)

# calling parent class function
print(Emp_details.name_, Emp_details.name)



# code
# A Python program to demonstrate inheritance

class Person:

    # Constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id

    # To check if this person is an employee
    def Display(self):
        print(self.name, self.id)
    

class Emp(Person):
    
    def __init__(self, name, id):
        self.name_ = name
        super().__init__(name, id)

    def Print(self):
        print("Emp class called")

Emp_details = Emp("Mayank", 103)

# calling parent class function
print(Emp_details.name_, Emp_details.name)