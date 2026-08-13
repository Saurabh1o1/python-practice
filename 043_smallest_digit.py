# Problem 43: Smallest Digit
#
# Question:
# Write a program that asks the user to enter a positive
# integer.
#
# The program should find the smallest digit
# present in the number.
#
# Examples:
#
# Input:
# Enter a number: 58321
#
# Output:
# Smallest digit: 1
#
#
# Input:
# Enter a number: 24680
#
# Output:
# Smallest digit: 0
#
#
# Input:
# Enter a number: 13579
#
# Output:
# Smallest digit: 1




num = int(input('Enter a number: '))
smallest = 9

while num > 0:
    digit = num % 10

    if digit < smallest:
        smallest = digit

    num //= 10

print(f'Smallest digit: {smallest}')
