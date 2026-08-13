# Problem 42: Find Largest Digit

# Question:
# Write a program that asks the user to enter a positive integer.
#
# The program should find the largest digit
# present in the number.
#
# Examples:
#
# Input:
# Enter a number: 58321
#
# Output:
# Largest digit: 8
#
#
# Input:
# Enter a number: 24680
#
# Output:
# Largest digit: 8
#
#
# Input:
# Enter a number: 13579
#
# Output:
# Largest digit: 9



# Best Solution for this question.

num = int(input('Enter a number: '))
largest = 0  # Start with 0 because every digit is between 0 and 9.

while num > 0:
    digit = num % 10

    if digit > largest:
        largest = digit

    num //= 10

print(f'Largest digit: {largest}')



# Alternate Solution 1.

# num = int(input('Enter a number: '))
# largest = float('-inf')

# while num > 0:
#     digit = num % 10

#     if digit > largest:
#         largest = digit

#     num //= 10

# print(f'Largest digit: {largest}')



# Alternate Solution 2.

# num = int(input('Enter a number: '))
# largest = None

# while num > 0:
#     digit = num % 10

#     if largest is None:
#         largest = digit
#     elif digit > largest:
#         largest = digit

#     num //= 10

# print(f'Largest digit: {largest}')


# Alternate Solution 3.

# num = int(input('Enter a number: '))
# largest = None

# while num > 0:
#     digit = num % 10

#     if largest is None or digit > largest:
#         largest = digit

#     num //= 10

# print(f'Largest digit: {largest}')
