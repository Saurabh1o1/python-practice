# Problem 51: Difference Between Largest and Smallest Digit

# Question:
# Write a program that asks the user to enter a positive
# integer.
#
# The program should find the largest digit and the smallest
# digit in the number, then calculate their difference.
#
# Examples:
#
# Input:
# Enter a number: 58321
#
# Output:
# Difference: 7
#
#
# Input:
# Enter a number: 24680
#
# Output:
# Difference: 8
#
#
# Input:
# Enter a number: 13579
#
# Output:
# Difference: 8
#
#
# Input:
# Enter a number: 7777
#
# Output:
# Difference: 0




num = int(input('Enter a number: '))
largest = 0
smallest = 9

while num > 0:
    digit = num % 10

    if digit > largest:
        largest = digit

    if digit < smallest:
        smallest = digit

    num = num // 10

diff = largest - smallest
print(f'Difference: {diff}')
