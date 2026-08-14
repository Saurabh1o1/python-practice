# Problem 46: Sum of Digits Greater Than 5

# Question:
# Write a program that asks the user to enter a positive
# integer.
#
# The program should calculate the sum of all digits
# that are greater than 5.
#
# Examples:
#
# Input:
# Enter a number: 58321
#
# Output:
# Sum of digits greater than 5: 8
#
#
# Input:
# Enter a number: 24680
#
# Output:
# Sum of digits greater than 5: 14
#
#
# Input:
# Enter a number: 13579
#
# Output:
# Sum of digits greater than 5: 16
#
#
# Input:
# Enter a number: 11111
#
# Output:
# Sum of digits greater than 5: 0




num = int(input('Enter a number: '))
total = 0

while num > 0:
    digit = num % 10

    if digit > 5:
        total = total + digit

    num = num // 10

print(f'Sum of digits greater than 5: {total}')
