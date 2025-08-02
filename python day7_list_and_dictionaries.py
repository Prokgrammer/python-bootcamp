fruits = ["Apple", "Orange", "Banana"]
fruits.append("duhat")
fruits.insert(1, "langka")
fruits.remove("langka")
fruits.pop()
print(fruits[1])

numbers = [4, 2, 7, 1]
numbers.append(9)       # [4, 2, 7, 1, 9]
numbers.sort()          # [1, 2, 4, 7, 9]
numbers.remove(4)       # [1, 2, 7, 9]
print(numbers[2])

#Activity

movies = ["intersellar", "the green mile", "American Pie", "Heneral luna", "Avengers"]
movies.append("Iron Man")
movies.sort()
movies.pop(1)
print(movies)

#Dictionaries

student = {
    "name": "John",
    "age": 21,
    "grade": "A"
}
print(student["name"])      # Output: John

student["age"] = 22         # Update age
student["major"] = "CS"     # Add new key


#Activity
book = {
    "title": "Atomic Habits",
    "author": "Japanese",
    "year": 2010
}
book["year"] = 2020
book["pages"] = 120
book.pop("author")
print(book)