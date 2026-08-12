# Problem 2: Positive, Negative or Zero

# Question:
# Write a function named check_number that takes one integer as input
# and returns:
# 1 if the number is positive,
# 0 if the number is zero,
# -1 if the number is negative.

# Example:
# Input: 10
# Output: 1

# Input: 0
# Output: 0

# Input: -5
# Output: -1



def check_number(num):

    if num > 0:
        return 1
    elif num == 0:
        return 0
    else:
        return -1

num = int(input('Enter a number: '))
print(check_number(num))