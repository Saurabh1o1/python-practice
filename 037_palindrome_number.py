# Problem 37: Palindrome Number

# Question:
# Write a program that asks the user to enter a positive integer.
#
# The program should check whether the number is a palindrome.
#
# A palindrome reads the same forward and backward.
#
# Examples:
#
# Input:
# Enter a number: 121
#
# Output:
# Palindrome
#
#
# Input:
# Enter a number: 12321
#
# Output:
# Palindrome
#
#
# Input:
# Enter a number: 12345
#
# Output:
# Not a palindrome




num = int(input('Enter a number: '))
forward = num
backward = 0

while num > 0:
    digit = num % 10
    backward = backward * 10 + digit
    num = num // 10

if forward == backward:
    number = 'Palindrome'
else:
    number = 'Not a palindrome'

print(number)
