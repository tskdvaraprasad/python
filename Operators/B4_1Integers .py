percentage = float(input("Enter percentage: "))
attendance = float(input("Enter attendance %: "))
eligible = percentage > 75 and attendance > 90
print("Eligible for scholarship:", eligible)
# Enter percentage: 78
# Enter attendance %: 82
# Eligible for scholarship: False