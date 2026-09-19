prices = {
    "Laptop": 60000,
    "Mobile": 25000,
    "Headphones": 2000,
    "Keyboard": 1500
}

highest_item = max(prices, key=prices.get)
lowest_item = min(prices, key=prices.get)

print("Highest price item:", highest_item, "-", prices[highest_item])
print("Lowest price item:", lowest_item, "-", prices[lowest_item])

'''Highest price item: Laptop - 60000
Lowest price item: Keyboard - 1500'''