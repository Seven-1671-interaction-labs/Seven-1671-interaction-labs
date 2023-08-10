class Vehicle:
    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage
        self._speed = 0 
    
    def set_speed(self, speed):
        self._speed = speed
    
    def __str__(self):
        return f"Vehicle: {self.name}, Speed: {self._speed}, Mileage: {self.mileage}"

class Car(Vehicle):
    def __init__(self, name, mileage, num_doors):
        super().__init__(name, mileage)
        self._num_doors = num_doors
    
    def __str__(self):
        return super().__str__() + f", Num Doors: {self._num_doors}"

class Bus(Vehicle):
    def __init__(self, name, mileage, capacity):
        super().__init__(name, mileage)
        self._capacity = capacity
    
    def __str__(self):
        return super().__str__() + f", Capacity: {self._capacity}"

car = Car("Sedan", 30, 4)
bus = Bus("School Bus", 15, 40)

car.set_speed(60)
bus.set_speed(50)

print(car)
print(bus)