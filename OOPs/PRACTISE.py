# # from abc import ABC, abstractmethod

# # class Coffe_Machine(ABC):
# #     @abstractmethod
# #     def concentration(self):
# #         pass

# #     def get_coffee(self):
# #         print(" Click coffee button ")
# #     def stop(self):
# #         print("Coffee is made")
# # class Milk:
# #     def getmilk(self):
# #         print("milk")
    


        
# # # class Coffee(Coffe_Machine):
# # #     def __init__(self,milk,coffee):
# # #         self.coffee = coffee
# # # conc = int(input())
# # class Latte(Milk,Coffe_Machine):

# #     # def __init__(self,lattee):
# #     #    self.lattee = lattee
# #     super().getmilk()
# #     def concentration(self,conc):
# #         if conc > 30:
           
                
# #                 print("Lattee")

# # class Cappuccino(Milk):
# #     def __init__(self,cappuccino):
# #         self.cappuccino = cappuccino
# #     def concentration(self,conc):
# #         if 30<conc<50:
# #             print("cappuccino")


# # class Espresso(Milk):
# #     def __init__(self,espresso):
# #         self.espresso = espresso
# #     def concentration(self,conc):
# #         if 50<conc<70:
# #             print("espresso")


# # coffee = Latte()
# # coffee.concentration()


# # in the coffe machine i want to create a program in oops where it takes coffeee likes cppucion , lattee, espresso and concentration 
# # parameter to take which coffe should come in this all inheritacne polymorphism abraction should come

# from abc import ABC, abstractmethod

# # Abstract class for Coffee Machine
# class CoffeeMachine(ABC):
#     @abstractmethod
#     def concentration(self, conc):
#         pass

#     def get_coffee(self):
#         print("Click coffee button")

#     def stop(self):
#         print("Coffee is made")

# # Milk class for adding milk functionality
# class Milk:
#     def getmilk(self):
#         print("Adding milk")

# # Latte Class inheriting from both Milk and CoffeeMachine
# class Latte(Milk, CoffeeMachine):
    
#     def concentration(self, conc):
#         if conc > 30:
#             print("Latte Selected")
        

# # Cappuccino Class inheriting from both Milk and CoffeeMachine
# class Cappuccino(Milk, CoffeeMachine):
#     def concentration(self, conc):
#         if 30 < conc < 50:
#             print("Cappuccino Selected")
        
# # Espresso Class inheriting only from CoffeeMachine (No milk)
# class Espresso(CoffeeMachine):
#     super()
#     def concentration(self, conc):
#         if 50 < conc < 70:
#             print("Espresso Selected")
       

# #  input for concentration level
# conc = int(input("Enter coffee concentration: "))

# # Choose coffee type based on user preference
# coffee_type = input("Enter coffee type (latte/cappuccino/espresso): ").lower()

# if coffee_type == "latte":
#     coffee = Latte()
#     coffee.getmilk()
# elif coffee_type == "cappuccino":
#     coffee = Cappuccino()
#     coffee.getmilk()
# elif coffee_type == "espresso":
#     coffee = Espresso()
# else:
#     print("Invalid coffee type")
#     coffee = None

# # If coffee instance is created, get concentration and start process
# if coffee:
#     coffee.get_coffee()
#     coffee.concentration(conc)
#     coffee.stop()








# from abc import ABC, abstractmethod

# # Abstract class for Coffee Machine
# class CoffeeMachine(ABC):
#     @abstractmethod
#     def concentration(self, conc):
#         pass

#     def get_coffee(self):
#         print("Click coffee button")

#     def stop(self):
#         print("Coffee is made")

# # Milk class for adding milk functionality
# class Milk:
#     def getmilk(self):
#         print("Adding milk")

# # Latte Class
# class Latte(Milk, CoffeeMachine):
#     super().get_coffee()
#     super().getmilk()
#     def concentration(self, conc):
#         if conc > 30:
#             print("Latte Selected")
#         else:
#             print("Weak coffee concentration")
#     super().stop()
# # Cappuccino Class
# class Cappuccino(Milk, CoffeeMachine):
#     def concentration(self, conc):
#         super().get_coffee()
#         super().getmilk()
#         if 30 < conc < 50:
#             print("Cappuccino Selected")
#         else:
#             print("Concentration not suitable for Cappuccino")
#     super().stop()
# # Espresso Class (No Milk)
# class Espresso(CoffeeMachine):
#     super().get_coffee()
   
#     super().getmilk()
#     def concentration(self, conc):
#         if 50 < conc < 70:
#             print("Espresso Selected")
#         else:
#             print("Concentration not suitable for Espresso")
#     super().stop()

# obj = 

from abc import ABC, abstractmethod

# Abstract class for Coffee Machine
class CoffeeMachine(ABC):
    @abstractmethod
    def concentration(self, conc):
        pass

    def get_coffee(self):
        print("Click coffee button")

    def stop(self):
        print("Coffee is made")

# Milk class for adding milk functionality
class Milk:
    def getmilk(self):
        print("Adding milk")

# Latte Class
class Latte(Milk, CoffeeMachine):
    def concentration(self, conc):
        super().get_coffee()
        super().getmilk()
        if conc > 30:
            print("Latte Selected")

        super().stop()

# Cappuccino Class
class Cappuccino(Milk, CoffeeMachine):
    def concentration(self, conc):
        super().get_coffee()
        super().getmilk()
        if 30 < conc < 50:
            print("Cappuccino Selected")

        super().stop()

# Espresso Class (No Milk)
class Espresso(CoffeeMachine):
    def concentration(self, conc):
        super().get_coffee()
        if 50 < conc < 70:
            print("Espresso Selected")

        super().stop()

# User input
conc = int(input("Enter coffee concentration: "))
coffee_type = input("Enter coffee type (latte/cappuccino/espresso): ")

obj = None
if coffee_type == "latte":
    obj = Latte()
elif coffee_type == "cappuccino":
    obj = Cappuccino()
elif coffee_type == "espresso":
    obj = Espresso()
else:
    print("Invalid coffee type")

if obj:
    obj.concentration(conc)


from abc import ABC, abstractmethod

# Private class for machine internals
class _CoffeeInternals:
    def __init__(self):
        self.__water_level = 100  # Private attribute

    def get_water_level(self):
        return self.__water_level

    def use_water(self, amount):
        if self.__water_level >= amount:
            self.__water_level -= amount
            print(f"Used {amount}ml water. Remaining: {self.__water_level}ml")
        else:
            print("Not enough water!")

# Abstract class for Coffee Machine
class CoffeeMachine(ABC):
    def __init__(self):
        self._internals = _CoffeeInternals()  # Encapsulated object

    @abstractmethod
    def concentration(self, conc):
        pass

    def get_coffee(self):
        print("Click coffee button")

    def stop(self):
        print("Coffee is made")

# Milk class for adding milk functionality
class Milk:
    def getmilk(self):
        print("Adding milk")

# Latte Class
class Latte(Milk, CoffeeMachine):
    def concentration(self, conc):
        super().get_coffee()
        super().getmilk()
        self._internals.use_water(30)  # Using private class
        if conc > 30:
            print("Latte Selected")
        else:
            print("Weak coffee concentration")
        super().stop()

# Cappuccino Class
class Cappuccino(Milk, CoffeeMachine):
    def concentration(self, conc):
        super().get_coffee()
        super().getmilk()
        self._internals.use_water(40)  # Using private class
        if 30 < conc < 50:
            print("Cappuccino Selected")
        else:
            print("Concentration not suitable for Cappuccino")
        super().stop()

# Espresso Class (No Milk)
class Espresso(CoffeeMachine):
    def concentration(self, conc):
        super().get_coffee()
        self._internals.use_water(50)  # Using private class
        if 50 < conc < 70:
            print("Espresso Selected")
        else:
            print("Concentration not suitable for Espresso")
        super().stop()

# User input
conc = int(input("Enter coffee concentration: "))
coffee_type = input("Enter coffee type (latte/cappuccino/espresso): ").lower()

# Creating coffee object dynamically
obj = None
if coffee_type == "latte":
    obj = Latte()
elif coffee_type == "cappuccino":
    obj = Cappuccino()
elif coffee_type == "espresso":
    obj = Espresso()
else:
    print("Invalid coffee type")

# Using object if created
if obj:
    obj.concentration(conc)



from abc import ABC, abstractmethod

# Abstract class for Coffee Machine
class CoffeeMachine(ABC):
    def __init__(self):
        self.__water = 100  # Private attribute for water

    def waterr(self, amount):
      
        if self.__water >= amount:
            self.__water -= amount
            print(f"Used {amount}water. Remaining: {self.__water_level}ml")
        else:
            print("Not enough water!")

    @abstractmethod
    def concentration(self, conc):
        pass

    def get_coffee(self):
        print("Click coffee button")

    def stop(self):
        print("Coffee is made")

# Milk class for adding milk functionality
class Milk:
    def getmilk(self):
        print("Adding milk")

# Latte Class
class Latte(Milk, CoffeeMachine):
    def concentration(self, conc):
        super().get_coffee()
        super().getmilk()
        super().water(30)  # Using water method
        if conc > 30:
            print("Latte Selected")
        
        super().stop()

# Cappuccino Class
class Cappuccino(Milk, CoffeeMachine):
    def concentration(self, conc):
        super().get_coffee()
        super().getmilk()
        super().water(40)  # Using water method
        if 30 < conc < 50:
            print("Cappuccino Selected")
        else:
            print("Concentration not suitable for Cappuccino")
        super().stop()

# Espresso Class (No Milk)
class Espresso(CoffeeMachine):
    def concentration(self, conc):
        super().get_coffee()
        super().water(50)  # Using water method
        if 50 < conc < 70:
            print("Espresso Selected")
        else:
            print("Concentration not suitable for Espresso")
        super().stop()

# User input
conc = int(input("Enter coffee concentration: "))
coffee_type = input("Enter coffee type (latte/cappuccino/espresso): ").lower()

# Creating coffee object dynamically
obj = None
if coffee_type == "latte":
    obj = Latte()
elif coffee_type == "cappuccino":
    obj = Cappuccino()
elif coffee_type == "espresso":
    obj = Espresso()
else:
    print("Invalid coffee type")

# Using object if created
if obj:
    obj.concentration(conc)
