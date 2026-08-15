# Problem 55: Check Whether Digits Are in Ascending Order

# Question:
# Write a program that asks the user to enter a positive
# integer.
#
# The program should check whether the digits of the number
# are arranged in ascending order from left to right.
#
# Equal consecutive digits are allowed.
#
# Examples:
#
# Input:
# Enter a number: 12345
#
# Output:
# Digits are in ascending order
#
#
# Input:
# Enter a number: 13579
#
# Output:
# Digits are in ascending order
#
#
# Input:
# Enter a number: 11234
#
# Output:
# Digits are in ascending order
#
#
# Input:
# Enter a number: 54321
#
# Output:
# Digits are not in ascending order
#
#
# Input:
# Enter a number: 12354
#
# Output:
# Digits are not in ascending order




num = int(input('Enter a number: '))
right_digit = None
is_ascending = True

while num > 0:
    digit = num % 10
    left_digit = digit

    if right_digit is not None:
        if right_digit < left_digit:
           is_ascending = False
           break

    right_digit = left_digit
    num = num // 10

if is_ascending:
    print('Digits are in ascending order')
else:
    print('Digits are not in ascending order')
