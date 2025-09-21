
def simpleCalculator(num1: int, num2: int, operation: str) -> str:
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by Zero."
            
    elif operation == "*":
        result = num1 * num2
    elif operation == "%":
        result = num1 % num2
    else:
        result = "Not a Valid Operation"

    return result

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
operation = str(input("Enter the operation to do"))

result = simpleCalculator(num1, num2, operation) 
print("Result :", result)