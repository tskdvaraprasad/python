s = input("Enter the main string: ")
sub = input("Enter the substring: ")

first_index = -1
count = 0

for i in range(len(s) - len(sub) + 1):

    match = True

    for j in range(len(sub)):
        if s[i + j] != sub[j]:
            match = False
            break

    if match:
        if first_index == -1:
            first_index = i

        count += 1

print("First occurrence index:", first_index)
print("Total occurrences:", count)