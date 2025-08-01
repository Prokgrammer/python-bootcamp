import helper
import tools
import calc_tools

#day6 task
message = helper.greet("Emerson")
print(message)


num_square = tools.square(5)
print(num_square)

num_cube = tools.cube(4)
print(num_cube)

print("Welcome to the Calculator!")

# Get user input
num1 = float(input("Enter first number: "))
op = input("Enter operation (+, -, *, /, **): ")
num2 = float(input("Enter second number: "))

# Perform operation
if op == "+":
    result = calc_tools.add(num1, num2)
elif op == "-":
    result = calc_tools.subtract(num1, num2)
elif op == "*":
    result = calc_tools.multiply(num1, num2)
elif op == "/":
    result = calc_tools.divide(num1, num2)
elif op == "**":
    result = calc_tools.power(num1, num2)
else:
    result = "Invalid operation."

print("Result:", result)