
from abc import ABC, abstractmethod

# Abstract class for Coffee Machine
class CoffeeMachine(ABC):
    def __init__(self):
        self.__water = 100  # Private attribute for water

    # def waterr(self, amount):
    #     if self.__water >= amount:
    #         self.__water -= amount
    #         print(f"Used {amount}water. Remaining: {self.__water_level}ml")
    #     else:
    #         print("Not enough water!")

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

def get_coffee_mach():
    coffeess = {
        "latte" : Latte("latte"),
        "capuccino": Cappuccino("cappucino"),
        "espresso":Espresso("espresso")
    }
    try:
        choice = input("Enter the coffee you want(latt/cap/espre)").strip().lower()
        if choice in coffeess:
            print(f"Your {choice} is getting prepared")
        else:
            print("Enter a valid choice")

    except ValueError:
        print("Please enter a type of coffee")

# # Creating coffee object dynamically
# obj = None
# if coffee_type == "latte":
#     obj = Latte()
# elif coffee_type == "cappuccino":
#     obj = Cappuccino()
# elif coffee_type == "espresso":
#     obj = Espresso()
# else:
#     print("Invalid coffee type")

# # Using object if created
# if obj:
#     obj.concentration(conc)


hi = get_coffee_mach()
