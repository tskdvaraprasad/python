import re

sentence = "I have a cat and a dog. My friend has a bird."

result = re.findall(r'\b(cat|dog|bird)\b', sentence)

print(result)