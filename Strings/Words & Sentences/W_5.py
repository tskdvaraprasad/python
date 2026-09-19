s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

s1 = s1.replace(" ", "").lower()
s2 = s2.replace(" ", "").lower()
print(s1)
print(s2)

if sorted(s1) == sorted(s2):
    print("Anagrams")
else:
    print("Not Anagrams")