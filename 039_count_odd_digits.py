# Problem 39: Count Odd Digits

# Question:
# Write a program that asks the user to enter a positive integer.
#
# The program should count how many odd digits are present
# in the number.
#
# Examples:
#
# Input:
# Enter a number: 58321
#
# Output:
# Odd digits: 3
#
#
# Input:
# Enter a number: 24680
#
# Output:
# Odd digits: 0
#
#
# Input:
# Enter a number: 13579
#
# Output:
# Odd digits: 5




num = int(input('Enter a number: '))
count = 0

while num > 0:
    digit = num % 10

    if digit % 2 != 0:
        count += 1

    num //= 10

print(f'Odd digits: {count}')
