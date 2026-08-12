# Problem 4: Absolute Value

# Question:
# Write a function named absolute_value that takes one integer as input
# and returns its absolute value.
#
# Rules:
# - If the number is positive or zero, return it as it is.
# - If the number is negative, return its positive value.
# - Do NOT use Python's built-in abs() function.

# Example:
# Input: 5
# Output: 5

# Input: -8
# Output: 8

# Input: 0
# Output: 0




def absolute_value(n):

    if n >= 0:
        return n
    else:
        return -n

value = int(input('Enter the number: '))

print(absolute_value(value))
