import keyword

s = input("Enter a string: ")

if s.isidentifier() and not keyword.iskeyword(s):
    print("Valid Identifier")
else:
    print("Invalid Identifier")