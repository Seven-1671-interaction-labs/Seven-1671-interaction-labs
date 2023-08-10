def flexible_calculator(operation, output_type, *numbers):
    if len(numbers) == 0:
        raise ValueError("At least one number must be provided.")
    
    result = numbers[0]
    for num in numbers[1:]:
        
        if operation == "ADD":
            result += num
            
        elif operation == "SUB":
            result -= num
            
        elif operation == "MUL":
            result *= num
            
        elif operation == "DIV":
            if num == 0:
                
                raise ValueError("Cannot divide by zero.")
            result /= num
    
    if output_type == "int":
        result = int(result)
    
    return result

if __name__ == '__main__':
    try:
        print(f"flexible_calculator(ADD, int, 1) = {flexible_calculator('ADD', 'int', 1)}")
        print(f"flexible_calculator(ADD, int, 1, 2) = {flexible_calculator('ADD', 'int', 1, 2)}")
        print(f"flexible_calculator(ADD, int, 1, 2, 3, 4) = {flexible_calculator('ADD', 'int', 1, 2, 3, 4)}")
        print(f"flexible_calculator(MUL, int, 2, 3, 4) = {flexible_calculator('MUL', 'float', 2, 3, 4)}")
        print(f"flexible_calculator(DIV, float, 10, 5, 2) = {flexible_calculator('DIV', 'float', 10, 5, 2)}")
        print(f"flexible_calculator(DIV, float, 5, 0) = {flexible_calculator('DIV', 'float', 5, 0)}")
    except ValueError as e:
        print(str(e))
