import requests

name = input("Input your name: ")
response = requests.get(f"https://api.agify.io/?name={name}")
person_info = response.json()
age = person_info.get("age")
print(age)
