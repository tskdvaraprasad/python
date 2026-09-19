import re

sentence = "1024 requests were served in 3 seconds"

result = re.match(r"\d", sentence)

if result:
    print("The sentence starts with a digit")
else:
    print("The sentence does not start with a digit")