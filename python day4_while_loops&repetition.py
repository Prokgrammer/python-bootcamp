# Practice 1: Print numbers from 1 to 10
num = 1

while num <= 10:
    print(num)
    num += 1



# Practice 2: Countdown from 5 to 1
count = 5

while count >= 1:
    print(count)
    count -= 1


user_name = ""
while user_name == "":
    user_name = input("What is your username: ")
print ("Hello ", user_name + "!")


command = ""

while command.lower() != "exit":
    command = input("Type 'exit' to quit: ")

print("Loop Ended, bye bye")