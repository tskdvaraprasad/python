import re

paragraph = "NASA is working with USA scientists to explore space."

result = re.finditer(r"\b[A-Za-z]{7,}\b", paragraph)

for match in result:
    print(match.group(), match.start())