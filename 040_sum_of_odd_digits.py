# Problem 40: Sum of Odd Digits

# Question:
# Write a program that asks the user to enter a positive integer.
#
# The program should calculate the sum of all the odd digits
# in the number.
#
# Examples:
#
# Input:
# Enter a number: 58321
#
# Output:
# Sum of odd digits: 9
#
#
# Input:
# Enter a number: 24680
#
# Output:
# Sum of odd digits: 0
#
#
# Input:
# Enter a number: 13579
#
# Output:
# Sum of odd digits: 25




num = int(input('Enter a number: '))
total = 0

while num > 0:
    digit = num % 10

    if digit % 2 != 0:
        total += digit

    num //= 10

print(f'Sum of odd digits: {total}')
