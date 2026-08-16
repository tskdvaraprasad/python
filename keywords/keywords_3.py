# Trying to use Python keywords as variable names

for = 5
True = 10


# Expected errors:
# Line 3: SyntaxError: invalid syntax
# Line 4: SyntaxError: cannot assign to True

# Output:

# File "variables.py", line 3

#     for = 5
#     ^^^
# SyntaxError: invalid syntax