import math
def hypotenuse(a,b):
    try:
        return math.sqrt(math.pow(a,2)+math.pow(b,2))
    except TypeError:
        return None
print(f'hypotenuse(3,4)is {hypotenuse(3.0,4.0)}')
print(f"hypotenuse('3','4') is {hypotenuse('3','4')}")
print(f"hypotenuse(3,'4.0') is {hypotenuse(3,'4.0')}")
