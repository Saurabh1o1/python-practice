# Problem 52: Sum of Digits Between 3 and 7

# Question:
# Write a program that asks the user to enter a positive
# integer.
#
# The program should calculate the sum of all digits
# that are between 3 and 7, inclusive.
#
# Examples:
#
# Input:
# Enter a number: 58321
#
# Output:
# Sum of digits between 3 and 7: 8
#
#
# Input:
# Enter a number: 24680
#
# Output:
# Sum of digits between 3 and 7: 10
#
#
# Input:
# Enter a number: 13579
#
# Output:
# Sum of digits between 3 and 7: 15
#
#
# Input:
# Enter a number: 11111
#
# Output:
# Sum of digits between 3 and 7: 0




num = int(input('Enter a number: '))
total = 0

while num > 0:
    digit = num % 10

    if digit >= 3 and digit <=7:
        total = total + digit

    num = num // 10

print(f'Sum of digits between 3 and 7: {total}')
