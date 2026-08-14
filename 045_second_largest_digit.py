# Problem 45: Second Largest Digit

# Question:
# Write a program that asks the user to enter a positive
# integer.
#
# The program should find the second largest distinct digit
# present in the number.
#
# The input will always contain at least two different digits.
#
# Examples:
#
# Input:
# Enter a number: 58321
#
# Output:
# Second largest digit: 5
#
#
# Input:
# Enter a number: 24680
#
# Output:
# Second largest digit: 6
#
#
# Input:
# Enter a number: 13579
#
# Output:
# Second largest digit: 7
#
#
# Input:
# Enter a number: 99821
#
# Output:
# Second largest digit: 8




num = int(input('Enter a number: '))
largest = 0
second_largest = 0

while num > 0:
    digit = num % 10
    if digit > largest:
        second_largest = largest
        largest = digit
    elif second_largest < digit < largest:
        second_largest = digit

    num //= 10

print(f'Second largest digit: {second_largest}')
    