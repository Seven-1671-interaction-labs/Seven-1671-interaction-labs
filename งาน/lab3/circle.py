import math


class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return round(math.pi * math.pow(self.radius, 2), 2)
    
    def circumference(self):
        return round(2 * math.pi * self.radius, 2)
    
    @staticmethod
    def get_valid_radius():
        while True:
            try:
                radius = float(input("Enter a radius: "))
                return radius
            except ValueError:
                print("Please enter a valid decimal number.")


if __name__ == "__main__":
    radius = Circle.get_valid_radius()
    circle = Circle(radius)
    area = circle.area()
    circumference = circle.circumference()
    print(f"The circle with radius {radius} has the area as {area} and the circumference as {circumference}.")
