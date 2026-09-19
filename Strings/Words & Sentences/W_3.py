s = input("Enter a sentence: ")

words = s.split()

words.reverse()

result = " ".join(words)

print(result)