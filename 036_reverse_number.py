# Problem 36: Reverse a Number

# Question:
# Write a program that asks the user to enter a positive integer.
#
# The program should reverse the number.
#
# Examples:
#
# Input:
# Enter a number: 58321
#
# Output:
# Reversed number: 12385
#
#
# Input:
# Enter a number: 1000
#
# Output:
# Reversed number: 1
#
#
# Input:
# Enter a number: 12345
#
# Output:
# Reversed number: 54321




num = int(input('Enter a number: '))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print(f'Reversed number: {reverse}')
