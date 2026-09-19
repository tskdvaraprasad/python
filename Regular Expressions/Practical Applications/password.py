import re

def check_password(pw):
    failed_rules = []

    # Rule 1: At least 8 characters
    if len(pw) < 8:
        failed_rules.append("Password must be at least 8 characters long")

    # Rule 2: At least one uppercase letter
    if not re.search(r'[A-Z]', pw):
        failed_rules.append("Password must contain at least one uppercase letter")

    # Rule 3: At least one lowercase letter
    if not re.search(r'[a-z]', pw):
        failed_rules.append("Password must contain at least one lowercase letter")

    # Rule 4: At least one digit
    if not re.search(r'\d', pw):
        failed_rules.append("Password must contain at least one digit")

    # Rule 5: At least one symbol
    if not re.search(r'[!@#$%^&*]', pw):
        failed_rules.append("Password must contain at least one symbol from !@#$%^&*")

    return failed_rules


password = "hello123"

failed = check_password(password)

if not failed:
    print("Password is strong")
else:
    print("Failed rules:")
    for rule in failed:
        print("-", rule)