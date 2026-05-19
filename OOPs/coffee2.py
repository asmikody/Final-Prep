from abc import ABC, abstractmethod

# Abstract class for Coffee Machine
class CoffeeMachine(ABC):
    def __init__(self):
        self.__water = 100  # Private attribute for water

    def use_water(self, amount):
        if self.__water >= amount:
            self.__water -= amount
            print(f"Used {amount}ml of water. Remaining: {self.__water}ml")
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
class Latte(CoffeeMachine, Milk):
    def concentration(self, conc):
        self.get_coffee()
        self.getmilk()
        self.use_water(30)  # Using water method
        if conc > 30:
            print("Latte Selected")
        self.stop()

# Cappuccino Class
class Cappuccino(CoffeeMachine, Milk):
    def concentration(self, conc):
        self.get_coffee()
        self.getmilk()
        self.use_water(40)  # Using water method
        if 30 < conc < 50:
            print("Cappuccino Selected")
        else:
            print("Concentration not suitable for Cappuccino")
        self.stop()

# Espresso Class (No Milk)
class Espresso(CoffeeMachine):
    def concentration(self, conc):
        self.get_coffee()
        self.use_water(50)  # Using water method
        if 50 < conc < 70:
            print("Espresso Selected")
        else:
            print("Concentration not suitable for Espresso")
        self.stop()

# Function to get coffee machine object
def get_coffee_machine():
    coffees = {
        "latte": Latte(),
        "cappuccino": Cappuccino(),
        "espresso": Espresso()
    }
    
    try:
        choice = input("Enter the coffee you want (latte/cappuccino/espresso): ").strip().lower()
        if choice in coffees:
            conc = int(input("Enter coffee concentration: "))
            coffees[choice].concentration(conc)
        else:
            print("Enter a valid choice")
    except ValueError:
        print("Please enter a valid coffee concentration.")

# Run the coffee selection
get_coffee_machine()
