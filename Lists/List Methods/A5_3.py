numbers = [10, 5, 25, 3, 18]

maximum = numbers[0]
minimum = numbers[0]
total = 0

for num in numbers:
    if num > maximum:
        maximum = num

    if num < minimum:
        minimum = num

    total += num

print("Maximum:", maximum)
print("Minimum:", minimum)
print("Sum:", total)