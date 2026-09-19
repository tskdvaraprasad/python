s = input("Enter a string: ")

for char in s:
    if s.count(char) > 1:
        print(char, ":", s.count(char))