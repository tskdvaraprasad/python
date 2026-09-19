a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Not a valid triangle")
elif a == b and b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
# Enter first side: 5
# Enter second side: 3
# Enter third side: 4
# Scalene triangle