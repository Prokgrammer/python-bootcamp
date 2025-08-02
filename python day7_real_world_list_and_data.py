students = [
    {"name": "Alice", "grade": 90},
    {"name": "Bob", "grade": 85},
    {"name": "Charlie", "grade": 92}
]

print(students[0]["name"])   # Output: Alice


classroom = {
    "Math": ["Alice", "Bob"],
    "Science": ["Charlie", "David"]
}

print(classroom["Math"][1])  # Output: Bob

user = {
    "name": "Emerson",
    "stats": {
        "posts": 34,
        "followers": 150
    }
}

print(user["stats"]["followers"])  # Output: 150


#Activity

books =[
    {"title": "Ibong adarna","Author": "Pedro", "Year": "1990"},
    {"title": "rich dad, poor dad", "Author": "Rober Kiosaki", "Year": "2010"},
    {"title": "Atomic Habits","Author": "Japanese", "Year": "2010"}
]
print(books[1]["title"])

for book in books:
    print(f'{book["title"]} by {book["Author"]} ({book["Year"]})')


 #Mini Project
students = []

num = int(input("How many students? "))

for _ in range(num):
    name = input("Student name: ")
    grades = []

    for i in range(3):
        grade = float(input(f"Enter grade #{i+1} for {name}: "))
        grades.append(grade)

    average = sum(grades) / len(grades)

    student = {
        "name": name,
        "grades": grades,
        "average": average
    }

    students.append(student)

# Print the report
print("\n📋 Student Report:")
for s in students:
    print(f'{s["name"]} - Grades: {s["grades"]} - Average: {s["average"]:.2f}')
   