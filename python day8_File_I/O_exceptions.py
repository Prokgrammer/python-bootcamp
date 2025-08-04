with open("notes.txt", "w") as file:
    file.write("This is a note. \n")
    file.write("Another line. \n")


with open("notes.txt", "r") as file:
    content = file.read()
    print(content)

with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())

#Activity

with open("sample.txt", "w") as file:
    file.write("This is another note. \n")
    file.write("Hello Python \n")

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)