try:
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    operation = input("Choose Operation (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    else:
        print("Invalid Operation!")
        result = None
    
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
    result = None
except ValueError:
    print("Error: Please enter a valid numbers.")
    result = None
else:
    if result is not None:
        print(f"Result: {result}")
finally:
    print("Thanks for using the calculator!")