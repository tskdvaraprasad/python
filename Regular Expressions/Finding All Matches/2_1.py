import re

paragraph = "NASA is working with USA scientists to explore space. The ISRO team is also involved."

result = re.findall(r"\b[A-Z]{2,}\b", paragraph)

print(result)