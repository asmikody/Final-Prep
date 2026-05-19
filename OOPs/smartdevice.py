from abc import ABC, abstractmethod
 
#  Abstraction + Base class
class SmartDevice(ABC):
    def __init__(self, name):
        self.name = name
 
    @abstractmethod
    def turn_on(self): pass
 
    @abstractmethod
    def turn_off(self): pass
 
    @abstractmethod
    def operate(self): pass
 
 
# Inheritance + Encapsulation
class Light(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.__brightness = 0  # Private attribute
 
    def turn_on(self):
        print(f" {self.name} is now ON")
 
    def turn_off(self):
        print(f"{self.name} is now OFF")
    # set private attribute 
    def set_brightness(self, level):
        if 0 <= level <= 100:
            self.__brightness = level
        else:
            print("Brightness should be between 0 and 100")
 
    def operate(self):  # Polymorphism
        self.set_brightness(75)
        print(f"{self.name} brightness set to {self.__brightness}%")
 
 
class Fan(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.__speed = 0
 
    def turn_on(self):
        print(f" {self.name} is now ON")
 
    def turn_off(self):
        print(f" {self.name} is now OFF")
 
    def set_speed(self, speed):
        if 0 <= speed <= 5:
            self.__speed = speed
        else:
            print("Speed should be between 0 and 5")
 
    def operate(self):
        self.set_speed(3)
        print(f"{self.name} speed set to {self.__speed}")
 
 
class AirConditioner(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.__temperature = 24
 
    def turn_on(self):
        print(f" {self.name} is now ON")
 
    def turn_off(self):
        print(f"{self.name} is now OFF")
 
    def set_temperature(self, temp):
        if 16 <= temp <= 30:
            self.__temperature = temp
        else:
            print("Temperature must be between 16 and 30")
 
    def operate(self):
        self.set_temperature(22)
        print(f"{self.name} temperature set to {self.__temperature}°C")

def get_device_choice():
    devices = {
        "light": Light("Light"),
        "fan": Fan("fan"),
        "ac": AirConditioner("AC")
    }
# def get_devicee():
#     devices = {
#         "light":Light("Light"),
#         "fan":Fan("fa")}
    
    try:
        choice = input("Enter device name (light/fan/ac): ").strip().lower()
        if choice in devices:
            return devices[choice]
        else:
            raise ValueError("Invalid device choice. Please select from light, fan, or ac.")
    except ValueError as e:
        print(e)
        return None

device = get_device_choice()

if device:
    device.turn_on()
    device.operate()
    device.turn_off()

 

#  Controller class using all devices
# class SmartHomeController:
#     def __init__(self):
#         self.devices = []
 
#     def add_device(self, device: SmartDevice):
#         self.devices.append(device)
 
#     def control_all(self):
#         print("\n=== Smart Home Controller ===")
#         for device in self.devices:
#             device.turn_on()
#             device.operate()
#             device.turn_off()
 
 
# #  Main Program
# controller = SmartHomeController()
 
# controller.add_device(Light("Living Room Light"))
# controller.add_device(Fan("Bedroom Fan"))
# controller.add_device(AirConditioner("Office AC"))
 
# controller.control_all()