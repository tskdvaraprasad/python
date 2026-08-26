numbers = [1, 2, 2, 3, 4, 3, 5, 1]

result = []

for num in numbers:
    if num not in result:
        result.append(num)

print(result)