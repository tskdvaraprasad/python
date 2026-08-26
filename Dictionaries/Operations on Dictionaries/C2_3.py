student = {
    "name": "Vara",
    "age": 20
}

key = "age"

if key in student:
    print(key, "exists")
    print("Value:", student[key])
else:
    print(key, "does not exist")