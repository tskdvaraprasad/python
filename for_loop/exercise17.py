start = int(input("Enter starting limit: "))
end = int(input("Enter ending limit: "))

for n in range(start, end + 1):
    if n < 2:
        continue

    prime = True

    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    if prime:
        print(n, end=" ")
# Enter starting limit: 3
# Enter ending limit: 10
# 3 5 7 