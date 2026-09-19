student = {
    "name": "Vara",
    "age": 20,
    "branch": "CSE"
}

print("Keys:")
for key in student.keys():
    print(key)

print("\nValues:")
for value in student.values():
    print(value)

print("\nKey-Value pairs:")
for key, value in student.items():
    print(key, ":", value)


'''Keys:
name
age
branch


Values:
Vara
20
CSE

Key-Value pairs:
name : Vara
age : 20
branch : CSE'''