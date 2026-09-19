import re

text = "apple banana apple mango apple"

result = re.findall(r"apple", text)

print("Number of occurrences:", len(result))