import csv

with open("students.csv", "w", newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Grade"])
    writer.writerow(["Alice", 90])
    writer.writerow(["Bob", 85])




with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#Activty
with open("book.csv", "w", newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Author", "Year"])
    writer.writerow(["Atomic Habits", "Jaames Clear", 2010])
    writer.writerow(["Rich Dad, Poor Dad", "Rober Kiyosaki", 2010])
    writer.writerow(["The subtle art of not giving a fuck", "Mark Manson", 2010])

with open("book.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


with open("grades.csv", "w", newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(["Average", "Status"])
    writer.writerow([99, "Passes"])
    writer.writerow([89, "Passes"])
    writer.writerow([69, "Failed"])
 