# Problem 44: Second Smallest Digit

# Question:
# Write a program that asks the user to enter a positive integer.
#
# The program should find the second smallest distinct digit
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
# Second smallest digit: 2
#
#
# Input:
# Enter a number: 24680
#
# Output:
# Second smallest digit: 2
#
#
# Input:
# Enter a number: 13579
#
# Output:
# Second smallest digit: 3
#
#
# Input:
# Enter a number: 11234
#
# Output:
# Second smallest digit: 2




num = int(input('Enter a number: '))
smallest = 9
second_smallest = 9

while num > 0:
    digit = num % 10

    if digit < smallest:
        second_smallest = smallest
        smallest = digit
    elif second_smallest > digit > smallest:
        second_smallest = digit

    num //= 10

print(f'Second smallest digit: {second_smallest}')
