age = int(input("Enter your age: "))

if age < 13:
    print("You're a kid.")
elif age <= 19:
    print("You're a teenager.")
else:
    print("You're an adult.")

number = int(input("Enter a Number "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


username = input("Enter Username: ")
password = input("Enter Password: ")

if username == "admin" and password == "1234":
    print("Access Granted")
else:
    print("Access Denied")


grade = int(input("Enter your grade: "))

if grade >= 90:
    print("A")

elif grade == 80 and grade <= 89:
    print("B") 

elif grade == 70 and grade <= 79:
    print("C")

elif grade == 60 and grade <= 69:
    print("D")

else:
    print("F")

secret_number = int(input("Guess the number: "))

if secret_number == 7:
    print("You Guess it right")

elif secret_number < 7:
    print("Too low")

else:
    print("Try Again")