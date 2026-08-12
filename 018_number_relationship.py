# Problem 18: Number Relationship

# Question:
# Write a function named number_relationship that takes
# two integers as input.
#
# The function should determine the relationship between
# the two numbers based on their signs.
#
# Return:
# "Both Positive"   -> if both numbers are positive.
# "Both Negative"   -> if both numbers are negative.
# "Opposite Signs"  -> if one number is positive and the
#                       other is negative.
# "Contains Zero"   -> if either number is zero.
#
# Examples:
#
# Input:
# 5
# 10
#
# Output:
# Both Positive
#
#
# Input:
# -5
# -10
#
# Output:
# Both Negative
#
#
# Input:
# 5
# -10
#
# Output:
# Opposite Signs
#
#
# Input:
# -5
# 10
#
# Output:
# Opposite Signs
#
#
# Input:
# 0
# 10
#
# Output:
# Contains Zero
#
#
# Input:
# -5
# 0
#
# Output:
# Contains Zero




def number_relationship(num1, num2):
    if num1 > 0 and num2 > 0:
        return 'Both Positive'
    elif num1 < 0 and num2 < 0:
        return 'Both Negative'
    elif (num1 > 0 and num2 < 0) or (num2 > 0 and num1 < 0):
        return 'Opposite Signs'
    else:
        return 'Contains Zero'


num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

print(number_relationship(num1, num2))
