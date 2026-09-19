import re

sentence = "1024 requests were served in 3 seconds"

result = re.search(r"served", sentence)

if result:
    print("Start position:", result.span()[0])
    print("End position:", result.span()[1])