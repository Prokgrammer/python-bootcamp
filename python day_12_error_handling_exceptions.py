try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("You Can't divide by zero.")
except ValueError:
    print("Please Enter a Valid Number")
else:
    print(f"Result: {result}")
finally:
    print("This always run, no matter what")