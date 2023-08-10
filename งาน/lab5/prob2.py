from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        """
        prob2.py: This file illustrates the usage of an abstract class and DocStrings

        Class Animal is an abstract class that has abstract method move
        Method move is an abstract method of an abstrack class Animal
        """
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run")

class crawl(Animal):
    def move(self):
        print("I can crawl")

class bark(Animal):
    def move(self):
        print("I can bark")

def main():
    """
    The main function to demonstrate the behavior of different animal instances.
    """
    animals=[Human(), crawl(), bark()]
    for animal in animals:
        animal.move()

if __name__=="__main__":
    print(Animal.move.__doc__)  # Print the method-level documentation of the move method in Animal
    print("=== Below is the output of the code ===")
    main()
    