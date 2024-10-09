# examples.py

# 2.1 Comments in Python
# This is a single-line comment
"""
This is a multi-line comment.
It can span multiple lines.
"""

# 2.2 Variables and Data Types
# Creating Variables
x = 5  # integer
y = "John"  # string
print("x:", x)
print("y:", y)

# Reassigning Variables
x = "Sally"  # x is now a string
print("New x:", x)

# Casting
x = str(5)  # casting integer to string
y = int("10")  # casting string to integer
z = float(5)  # casting integer to float
print("Cast x:", x, "Cast y:", y, "Cast z:", z)

# Getting the Type
print("Type of x:", type(x))
print("Type of y:", type(y))

# Case-Sensitivity
a = 10
A = 20
print("a:", a, "A:", A)  # Different variables

# 2.3 Data Types
# Checking Data Types
print("Data type of a:", type(a))
print("Data type of x:", type(x))
