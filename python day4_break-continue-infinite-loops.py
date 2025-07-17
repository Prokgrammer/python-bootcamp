while True:
    number = int(input("Guess: "))
    if number == 2:
        print("Right!")
        break
    print("Wrong", number)  # <- this line runs no matter what if it's not indented under else


for i in range(1, 10, 2):
    if i % 2 == 0:
        continue
    print(i)


for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
