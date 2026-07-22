num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operator = input("Enter the operator (+, -, *, /): ")

if operator == "+":
    result = num1 + num2
    print("The result is: " + str(result))
elif operator == "-":
    result = num1 - num2
    print("The result is: " + str(result))
elif operator == "*":
    result = num1 * num2
    print("The result is: " + str(result))
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print("The result is: " + str(result))
    else:
        print("Error: Division by zero is not allowed.")


