from abc import ABC,abstractmethod:
class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass
class Electric(ABC):
    @abstractmethod
    def charge(self):
        pass
class ElectricCar(Vehicle,Electric):
    def charge(self,)