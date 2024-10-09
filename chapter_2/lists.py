# lists.py

# 2.3 E. List (list)
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]

# List Methods
# Append
fruits.append("orange")
print("After append:", fruits)

# Remove
fruits.remove("banana")
print("After remove:", fruits)

# Pop
popped_item = fruits.pop(1)  # pops the second item
print("After pop:", fruits, "Popped item:", popped_item)

# Sort
numbers.sort()
print("Sorted numbers:", numbers)

# Index
index_of_cherry = fruits.index("cherry")
print("Index of cherry:", index_of_cherry)
