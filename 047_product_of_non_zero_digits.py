# Problem 47: Product of Non-Zero Digits

# Question:
# Write a program that asks the user to enter a positive
# integer.
#
# The program should calculate the product of all
# non-zero digits in the number.
#
# Examples:
#
# Input:
# Enter a number: 58321
#
# Output:
# Product of non-zero digits: 240
#
#
# Input:
# Enter a number: 1023
#
# Output:
# Product of non-zero digits: 6
#
#
# Input:
# Enter a number: 7005
#
# Output:
# Product of non-zero digits: 35
#
#
# Input:
# Enter a number: 11111
#
# Output:
# Product of non-zero digits: 1




num = int(input('Enter a number: '))
product = 1

while num > 0:
    digit = num % 10

    if digit > 0:
        product = product * digit

    num = num // 10

print(f'Product of non-zero digits: {product}')
