import re

string1 = "12345"
string2 = "123a5"

result1 = re.fullmatch(r"\d+", string1)

if result1:
    print("12345 consists only of digits")
else:
    print("12345 does not consist only of digits")

result2 = re.fullmatch(r"\d+", string2)

if result2:
    print("123a5 consists only of digits")
else:
    print("123a5 does not consist only of digits")