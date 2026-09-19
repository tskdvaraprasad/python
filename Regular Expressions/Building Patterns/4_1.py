import re

pattern = r'^[A-Za-z_][A-Za-z0-9_]*$'

names = ["_count2", "2fast", "total_sum"]

for name in names:
    if re.fullmatch(pattern, name):
        print(name, "is a valid variable name")
    else:
        print(name, "is not a valid variable name")
        