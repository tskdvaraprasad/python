import re

def double_number(match):
    number = int(match.group())
    return str(number * 2)

text = "I have 3 apples and 5 oranges."

result = re.sub(r'\d+', double_number, text)

print(result)