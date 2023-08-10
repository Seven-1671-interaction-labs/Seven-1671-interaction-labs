correct_input = False

while not correct_input:
    try:
        celcius = float(input("Enter a temperature in Celsius: "))
        formula = (9/5)*celcius+32
        print(f"{celcius:.2f} in Celsius is {formula:.2f} Fahrenheit")
    except ValueError:
        print('Please enter a valid flooating point for the temperature')
        break
    else:
        correct_input = True