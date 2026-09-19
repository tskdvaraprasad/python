import re

text = "Wait!!! What??? Really!!!"

result, count = re.subn(r'([!?])\1+', r'\1', text)

print(result)
print("Number of replacements:", count)