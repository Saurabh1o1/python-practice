# Problem 49: Sum of Digits Less Than 5

# Question:
# Write a program that asks the user to enter a positive
# integer.
#
# The program should calculate the sum of all digits
# that are less than 5.
#
# Examples:
#
# Input:
# Enter a number: 58321
#
# Output:
# Sum of digits less than 5: 6
#
#
# Input:
# Enter a number: 24680
#
# Output:
# Sum of digits less than 5: 6
#
#
# Input:
# Enter a number: 13579
#
# Output:
# Sum of digits less than 5: 4
#
#
# Input:
# Enter a number: 555
#
# Output:
# Sum of digits less than 5: 0




num = int(input('Enter a number: '))
total = 0

while num > 0:
    digit = num % 10

    if digit < 5:
        total = total + digit

    num = num // 10

print(f'Sum of digits less than 5: {total}')
