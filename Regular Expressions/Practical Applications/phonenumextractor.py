import re

text = """
Call 555-123-4567 or (555) 123-4567.
You can also reach us at 555.123.4567.
"""

pattern = r'(?:\(\d{3}\)[ .-]|\d{3}[.-])\d{3}[.-]\d{4}'

numbers = re.findall(pattern, text)

for number in numbers:
    # Remove brackets and spaces
    number = re.sub(r'[()\s.]', '', number)

    # Replace remaining hyphen-separated format consistently
    parts = re.split(r'-', number)

    if len(parts) == 3:
        number = '-'.join(parts)

    print(number)