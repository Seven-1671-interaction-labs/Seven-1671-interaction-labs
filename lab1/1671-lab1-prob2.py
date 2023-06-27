s = float(input("Enter s number: "))
e = float(input("Enter s number: "))
v = s + e 

print(f"{s} + {e} = {v}")

print("writing to flie number.txt")
print("Reading from flie number.txt")

with open('number.txt', 'w') as file:
    file.write(f"{s} + {e} = {v}")
    
with open('number.txt' ,'r') as file:
            data = file.read()
            print(data)