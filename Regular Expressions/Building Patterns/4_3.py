import re

text = "Colors are #FFAA00, #000, and #12AB."

result = re.findall(r'#[A-Fa-f0-9]{3}(?:[A-Fa-f0-9]{3})?', text)

print(result)