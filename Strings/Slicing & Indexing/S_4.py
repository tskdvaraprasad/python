s = input("Enter a string: ")
char = input("Enter a character: ")

first = s.find(char)
last = s.rfind(char)

print("First occurrence:", first)
print("Last occurrence:", last)