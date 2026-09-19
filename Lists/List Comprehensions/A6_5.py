numbers = [10, -5, 20, -3, 0, 15, -8]

result = [0 if num < 0 else num for num in numbers]

print(result)

#[10, 0, 20, 0, 0, 15, 0]