import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Request failed with status", response.status_code)