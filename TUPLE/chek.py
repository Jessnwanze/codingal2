# Get the user's input
num = int(input("Enter a number: "))

# Find the number of digits in the number
num_str = str(num)
num_digits = len(num_str)

# Calculate the sum of the digits raised to the power of the number of digits
sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)

# Check if the number is an Armstrong number
if sum_of_powers == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
