num = int(input("Enter a number: "))

temp = num
sum_digits = 0
count = 0

while temp > 0:
    digit = temp % 10
    sum_digits += digit
    count += 1
    temp //= 10

average = sum_digits / count

print("Sum =", sum_digits)
print("Average =", average)