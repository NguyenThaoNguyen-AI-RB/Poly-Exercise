from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption
    
    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel (self, fuel):
        pass

class Car(Vehicle):
    def drive(self, distance):
        adjusted_consumption = self.fuel_consumption + 0.9
        fuel_needed = distance*adjusted_consumption
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed
            print ('Car travelled {distance} km')
        else:
            print ('Car does not have enough fuel to travel the distance')
    def refuel(self, fuel):
        self.fuel_quantity += fuel
        print ('Carrefueled with {fuel} liters')

class Truck(Vehicle):
    def drive(self, distance):
        adjusted_consumption = self.fuel_consumption + 1.6
        fuel_needed = distance*adjusted_consumption
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed
            print('Truck travelled {distance} km')
        else:
            print('Truck does not have enough fuel to travel the distance')
    def refuel(self, fuel):
        self.fuel_quantity += fuel*0.95
        print ('Carrefueled with {fuel} liters')

car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)