# class Car:
#     def __init__(self,color,model,year):
#         self.color = color
#         self.model = model
#         self.year = year
#         self.mileage = 130
#     def drive(self,distance):
#         self.mileage += distance 
# a = Car("black","bmw" ,2023)  
# print(f"{a.year} {a.color} {a.model}")

# a.drive(100)        
# print(a.mileage)

class Bank:
    def __init__(self,name,bal=0):
        self.name = name
        self.__bal = bal

    def deposit(self,amt):
        if amt>0: self.__bal += amt

    def withdraw(self,amt):
        if 0 <amt<= self.__bal: self.__bal -= amt

    def get_bal(self):
        return self.__bal
ac = Bank("asmi",500)       
ac.deposit(1000)
ac.withdraw(200)
print(ac.get_bal())