# Basic funtion that doesnt need the print to be called twice
def greet():
    print("Hello, Welcome to Python")

greet()
greet()

#function with parameter

def greet_user(name):
    print(f"Hello {name}!")

greet_user("John")
greet_user("Thali")


#function with return value
def add(a, b):
    return a + b
result = add(5, 5)
print(f"The sum is : {result}")



#Activity

def addition(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

result = None

try:
    num1 = int(input("Fist Number"))
    num2 = int(input("Second Number: "))

    operation = input("Selec Operation +, -, *, /: ")

    if operation == "+":
        result = addition(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        result = divide(num1, num2)
    else:
        print("Invalid Operation")

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