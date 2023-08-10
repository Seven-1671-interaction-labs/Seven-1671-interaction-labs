def robust_calculator(op1, op2, operator='+', output_format='float'):
    if not isinstance(op1, (float,int)) or not isinstance(op2, (float,int)):
        raise ValueError('Invalid operands. Operands must be numbers.')

    if operator not in ['+', '-', '*', '/']:
        raise ValueError("Operator must be +, -, *, or /")
    
    if operator=="+":
        result=op1 + op2
    elif operator=="-":
        result=op1-op2
    elif operator=="*":
        result=op1*op2
    elif operator=="/":
        if op2==0:
            raise ValueError("Division by zero is not allowed.")
        result=op1/op2
    
    if output_format=="integer":
        result=round(result)
    
    return result

def get_operand(message):
    operand=input(message)
    if operand.lower()=="q":
        exit()
    try:
        return float(operand)
    except ValueError:
        raise ValueError("Invalid operand. Operand must be a number.")

def get_operator():
    operator = input("Enter an operation ('+', '-', '*', or '/'):")
    if operator.lower()=="q":
        exit()
    if operator not in ["+", "-", "*", "/"]:
        raise ValueError("Operator must be +, -, *, or /")
    return operator

def get_format():
    format_input = input("Enter an output format (float, int):")
    if format_input.lower() == "q":
        exit()

def calculator():
    while True:
        try:
            op1 = get_operand("Enter the first operand ('q' to quit):")
            op2 = get_operand("Enter the second operand ('q' to quit):")
            operator = get_operator()
            requested_format = get_format()
            output = robust_calculator(op1, op2, operator, requested_format)
            if op1==0:
                print('Cannot divide by zero')
                print('We cannot perform your requested calculation')
            if op2==0:
                print('Cannot divide by zero')
                print('We cannot perform your requested calculation')
            if operator=='':
                operator='+'
            print("{} {} {} = {:.1f}".format(op1, operator, op2, output))
        except ValueError as e:
            print("Error:", str(e))

if __name__ == "__main__":
    calculator()