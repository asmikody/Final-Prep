from abc import ABC, abstractmethod

# Abstract class for Coffee Machine
class CoffeeMachine(ABC):
    def __init__(self, coffee_type):
        self.__coffee_type = coffee_type  # Private attribute for coffee type
       
        self.__water_level = 100  # Private attribute for water level



    def water(self, amount):
        """Method to manage water levels"""
        if self.__water_level >= amount:
            self.__water_level -= amount
            print(f"Used {amount}ml water. Remaining: {self.__water_level}ml")
        else:
            print("Not enough water!")

    @abstractmethod
    def concentration(self, conc):
        pass

    def get_coffee(self):
        print(f"Click coffee button for {self.__coffee_type}")

    def stop(self):
        print(f"{self.__coffee_type} is ready!")

# Milk class for adding milk functionality
class Milk:
    def getmilk(self):
        print("Adding milk")

# Latte Class
class Latte(Milk, CoffeeMachine):
    def __init__(self):
        super().__init__("Latte")

    def concentration(self, conc):
        super().get_coffee()
        super().getmilk()
        super().water(30)
      
        if conc > 30:
            print(f"{self._CoffeeMachine__coffee_type} Selected")
        else:
            print("Weak coffee concentration")
        super().stop()

# Cappuccino Class
class Cappuccino(Milk, CoffeeMachine):
    def __init__(self):
        super().__init__("Cappuccino")

    def concentration(self, conc):
        super().get_coffee()
        super().getmilk()
        super().water(40)
       
        if 30 < conc < 50:
            print(f"{self._CoffeeMachine__coffee_type} Selected")
        else:
            print("Concentration not suitable for Cappuccino")
        super().stop()

# Espresso Class (No Milk)
class Espresso(CoffeeMachine):
    def __init__(self):
        super().__init__("Espresso")

    def concentration(self, conc):
        super().get_coffee()
        super().water(50)
       
        if 50 < conc < 70:
            print(f"{self._CoffeeMachine__coffee_type} Selected")
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
