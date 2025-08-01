
#parameters and return values
def multiply(a, b):
    result = a * b
    print(result)

multiply(5,5)


def add(a, b):
    return a + b

result = add(5, 10)
print(result)


#mini activity
def greeting(name, age):
    return (f"Hi {name}, you are {age} years old")

message = greeting("John", 25)
print(message)

def divide (x, y):
    return x / y
result = divide(10, 2)
print(result)



#default parameters and variable scope. This is useful when you want to make your function flexible.

def greet(name="Guest"):
    print(f"Hello, {name}")
greet("Alice")
greet()

#variable scope

message = "I am global" #global variable

def show_message():
    message = "I am local"
    print(message)

show_message() #Output: I am local
print(message) #Output: I am global


# 2 quick task

def introduce(name="Stranger"):
    print(f"Nice to meet you , {name}!")
introduce("John")
introduce()

topic = "Python"

def print_topic():
    topic = "Functions"
    print(topic)

print_topic()
print(topic)