class Vehicle:
    
    def __init__(self, name, speed, mileage):
        self.name = name
        self._speed = speed
        self.mileage = mileage

    def set_speed(self, car_speed):
        self._speed = car_speed

    def __str__(self):
        return f"Name: {self.name} Speed: {self._speed}: Mileage:{self.mileage}"


class Car(Vehicle):
    def __init__(self, num_doors, name, speed, mileage):
        super().__init__(name, speed, mileage)
        self.num_doors = num_doors

    def __str__(self):
        return f"Name: {self.name} Speed: {self._speed}: Mileage: {self.mileage}: Num Doors:{self.num_doors}"


class Bus(Vehicle):
    def __init__(self, capacity, name, speed, mileage):
        super().__init__(name, speed, mileage)
        self.capacity = capacity

    def __str__(self):
        return f"Name: {self.name} Speed: {self._speed}: Mileage: {self.mileage}: Capacity:{self.capacity}"


if __name__ == '__main__':
    car = Car(4, 'Toyota Vios', 90, 150000)
    bus = Bus(100, 'School Volvo', 12, 200000)
    print(car)
    print(bus)
    bus.set_speed(30)
    print(bus)