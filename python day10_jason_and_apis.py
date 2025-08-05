import json

data = {"name": "Alice", "age": 25, "skills": ["Python", "Git"]}

with open("data.json", "w") as file:
    data=json.dump(data, file, indent=4)

json_string = '{"name": "Bob", "age": 30}'
data = json.loads(json_string)  # JSON ➜ dict

print(data["name"])

new_json = json.dumps(data)     # dict ➜ JSON string
print(new_json)


with open("data.json", "r") as file:
    data = json.load(file)
    print(data)

#Activity
student = {"name": "Bornok","age": 25, "subjects": "History", "GPA": 96}

with open("student.json", "w") as file:
    student=json.dump(student, file, indent=4)

with open("student.json", "r") as file:
    loaded_student = json.load(file)
    print(loaded_student)