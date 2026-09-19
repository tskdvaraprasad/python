import re

def redact_emails(text):
    return re.sub(r'\b[\w.-]+@[\w.-]+\.\w+\b', '[EMAIL HIDDEN]', text)

text = "Contact john@gmail.com or admin@example.com for more information."

print(redact_emails(text))