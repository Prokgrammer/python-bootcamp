try:
    
    num = int(input("Enter a number:"))
    print(100/num)
except ValueError:
    print("That's not a number.")
except ZeroDivisionError:
    print("You can't divide by zero.")


try:
    f = open("sample.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("file not found!")
finally:
    f.close()


#Activity

try:

    num=int(input("Enter a number:"))
    print(100/num)
except ValueError:
    print("That's not a number")
except  ZeroDivisionError:
    print("You cant divide with zero!")
else:
    print("success")
finally:
    print("Thank you for using the program.")