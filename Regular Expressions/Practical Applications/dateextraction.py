import re

text = "Important dates are 15/06/2024 and 25/12/2025."

# Extract dates using groups
pattern = r'(\d{2})/(\d{2})/(\d{4})'

dates = re.findall(pattern, text)

print("Extracted dates:")
for date in dates:
    print(date)

# Convert DD/MM/YYYY -> YYYY-MM-DD
result = re.sub(pattern, r'\3-\2-\1', text)

print("Reformatted text:")
print(result)