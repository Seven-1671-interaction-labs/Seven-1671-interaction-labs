text = input("Enter the text: ")
pattern = input("Enter the pattern: ")

position = text.find(pattern)

if position != -1:
    print(f"Found '{pattern}' in '{text}' at position {position}.")
else:
    print(f"Cannot find '{pattern}' in '{text}'.")
