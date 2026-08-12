# Problem 30: Count Positive and Negative Numbers

# Question:
# Write a program that asks the user to enter 10 integers,
# one at a time.
#
# The program should count how many of the entered numbers
# are positive and how many are negative.
#
# Zero should not be counted as either positive or negative.
#
# Example:
#
# Input:
# Enter number 1: 5
# Enter number 2: -3
# Enter number 3: 0
# Enter number 4: 8
# Enter number 5: -2
# Enter number 6: 4
# Enter number 7: -7
# Enter number 8: 0
# Enter number 9: 6
# Enter number 10: -1
#
# Output:
# Positive numbers: 4
# Negative numbers: 4
#
#
# More examples:
#
# If all 10 numbers are positive:
#
# Output:
# Positive numbers: 10
# Negative numbers: 0
#
#
# If all 10 numbers are negative:
#
# Output:
# Positive numbers: 0
# Negative numbers: 10



positive_count = 0
negative_count = 0

for i in range(1, 11):
    num = int(input(f'Enter number {i}: '))
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1

print(f'Positive numbers: {positive_count}')
print(f'Negative numbers: {negative_count}')
