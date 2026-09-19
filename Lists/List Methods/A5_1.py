numbers = [10, 20, 30, 20]

print("Original list:", numbers)

# append()
numbers.append(40)
print("After append:", numbers)

# insert()
numbers.insert(1, 15)
print("After insert:", numbers)

# extend()
numbers.extend([50, 60])
print("After extend:", numbers)

# remove()
numbers.remove(20)
print("After remove:", numbers)

# pop()
numbers.pop()
print("After pop:", numbers)

# sort()
numbers.sort()
print("After sort:", numbers)

# reverse()
numbers.reverse()
print("After reverse:", numbers)

# count()
print("Count of 20:", numbers.count(20))

# index()
print("Index of 30:", numbers.index(30))

'''Original list: [10, 20, 30, 20]
After append: [10, 20, 30, 20, 40]
After insert: [10, 15, 20, 30, 20, 40]
After extend: [10, 15, 20, 30, 20, 40, 50, 60]
After remove: [10, 15, 30, 20, 40, 50, 60]
After pop: [10, 15, 30, 20, 40, 50]
After sort: [10, 15, 20, 30, 40, 50]
After reverse: [50, 40, 30, 20, 15, 10]
Count of 20: 1
Index of 30: 2'''