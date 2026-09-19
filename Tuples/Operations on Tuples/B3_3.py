numbers = (10, 20, 30, 40)

try:
    numbers[0] = 100
except TypeError as error:
    print("Error:", error)

'''Error: 'tuple' object does not support item assignment'''    