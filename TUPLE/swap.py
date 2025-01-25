# Get input from the user
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

# Display original values
print(f"Before swapping: a = {a}, b = {b}, c = {c}")

# Swap the values
a, b, c = b, c, a

# Display swapped values
print(f"After swapping: a = {a}, b = {b}, c = {c}")
