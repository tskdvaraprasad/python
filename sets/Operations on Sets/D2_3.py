numbers = {1, 2, 3, 4, 5}

numbers.remove(3)
print("After remove:", numbers)

numbers.discard(4)
print("After discard:", numbers)

# remove() raises an error if the element does not exist.
# discard() does not raise an error if the element does not exist.

numbers.discard(10)