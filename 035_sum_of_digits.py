# Problem 35: Sum of Digits

# Question:
# Write a program that asks the user to enter a positive integer.
#
# The program should calculate the sum of all the digits
# in the number.
#
# Examples:
#
# Input:
# Enter a number: 58321
#
# Output:
# Sum of digits: 19
#
#
# Input:
# Enter a number: 1000
#
# Output:
# Sum of digits: 1
#
#
# Input:
# Enter a number: 7
#
# Output:
# Sum of digits: 7




num = int(input('Enter a number: '))
total = 0

while num > 0:
    total += num % 10
    num //= 10

print(f'Sum of digits: {total}')
