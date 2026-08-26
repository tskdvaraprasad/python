student = {
    "name": "Vara",
    "age": 20,
    "branch": "CSE"
}

removed_value = student.pop("age")

print("Removed value:", removed_value)
print(student)

value = student.get("college", "Key not found")

print(value)