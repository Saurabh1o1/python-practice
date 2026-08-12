# Problem 1: Even Number Checker

# Question:
# Write a function named is_even that takes one integer as input
# and returns True if the number is even, otherwise returns False.

# Example:
# Input: 4
# Output: True

# Input: 7
# Output: False



def is_even(n):
    return n % 2 == 0 

num = int(input('Enter a number: '))
print(is_even(num))