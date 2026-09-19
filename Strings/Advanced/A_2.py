s = input("Enter a string: ")

if s.isdigit():
    print("Contains only digits")

elif s.isalpha():
    print("Contains only alphabets")

elif s.isalnum():
    print("Alphanumeric")

else:
    print("Contains special characters or spaces")