import re

def is_valid_email(s):
    pattern = r'^[\w.]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}$'
    return re.fullmatch(pattern, s) is not None


valid_emails = [
    "john@gmail.com",
    "user.name@yahoo.com",
    "abc123@test.in",
    "first.last@example.org"
]

invalid_emails = [
    "a@b.c",          # TLD is only 1 letter
    "no-at-sign.com", # Missing @
    "john@gmail",     # Missing .TLD
    "a@b.cdefghi"     # TLD is longer than 6 letters
]

for email in valid_emails:
    print(email, "->", is_valid_email(email))

for email in invalid_emails:
    print(email, "->", is_valid_email(email))