# Problem 48: Count Digits Greater Than 5

# Question:
# Write a program that asks the user to enter a positive
# integer.
#
# The program should count how many digits are greater
# than 5 in the number.
#
# Examples:
#
# Input:
# Enter a number: 58321
#
# Output:
# Number of digits greater than 5: 1
#
#
# Input:
# Enter a number: 24680
#
# Output:
# Number of digits greater than 5: 2
#
#
# Input:
# Enter a number: 13579
#
# Output:
# Number of digits greater than 5: 2
#
#
# Input:
# Enter a number: 11111
#
# Output:
# Number of digits greater than 5: 0




num = int(input('Enter a number: '))
count = 0

while num > 0:
    digit = num % 10
    if digit > 5:
        count = count + 1

    num = num // 10

print(f'Number of digits greater than 5: {count}')
