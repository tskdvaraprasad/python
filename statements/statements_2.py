# Using line continuation character (\)
sum1 = 10 + 20 + 30 + \
       40 + 50 + 60

print("Sum using line continuation:", sum1)

# Using implicit continuation with parentheses ()
sum2 = (
    10 + 20 + 30 +
    40 + 50 + 60
)

print("Sum using parentheses:", sum2)
# Sum using line continuation: 210
# Sum using parentheses: 210
# PS D:\python> # Using line continuation character (\)
# >> sum1 = 10 + 20 + 30 + \
# >>        40 + 50 + 60