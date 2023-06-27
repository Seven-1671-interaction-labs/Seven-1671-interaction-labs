import math
r=float(input('Enter radius:'))
if r<0:
    print('please enter a positive number for radius')
else:
    h=float(input('Enter height:'))
    if h<0:
        print('please enter a positive number for radius')
    else:
        a=2*math.pi*r*(r+h)
        print(f'The surface area of a cylinder with radius {r} and height {h} is {a}')  