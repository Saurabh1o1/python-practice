# Problem 32: Find the Smallest Number

# Question:
# Write a program that asks the user to enter 10 integers,
# one at a time.
#
# The program should find and print the smallest number
# among the 10 numbers.
#
# Example:
#
# Input:
# Enter number 1: 12
# Enter number 2: 5
# Enter number 3: 27
# Enter number 4: 9
# Enter number 5: 3
# Enter number 6: 18
# Enter number 7: 41
# Enter number 8: 6
# Enter number 9: 22
# Enter number 10: 15
#
# Output:
# Smallest number: 3
#
#
# More examples:
#
# If the numbers are:
# 4, 8, 2, 15, 7, 3, 9, 1, 6, 5
#
# Output:
# Smallest number: 1
#
#
# If all 10 numbers are negative:
# -5, -12, -3, -20, -8, -1, -7, -15, -4, -9
#
# Output:
# Smallest number: -20




smallest_number = None

for i in range(1, 11):
    num = int(input(f'Enter number {i}: '))
    if smallest_number is None:
        smallest_number = num
    elif num < smallest_number:
        smallest_number = num


print(f'Smallest number: {smallest_number}')
