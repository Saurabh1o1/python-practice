# Problem 9: Simple Calculator

# Question:
# Write a function named calculate that takes
# three parameters:
# 1. First number
# 2. Operator (+, -, *, /)
# 3. Second number
#
# Return the result of the operation.
#
# If the operator is not one of +, -, *, /,
# return "Invalid Operator".

# Example:
# Input:
# 10
# +
# 5
# Output:
# 15

# Input:
# 8
# *
# 4
# Output:
# 32

# Input:
# 20
# /
# 5
# Output:
# 4.0

# Input:
# 7
# %
# 2
# Output:
# Invalid Operator




def calculator(first_number, operator, second_number):

    if operator == '+':
        return first_number + second_number
    elif operator == '-':
        return first_number - second_number
    elif operator == '*':
        return first_number * second_number
    elif operator == '/':
        if second_number == 0:
            return 'Cannot divide by zero'
        else:
            return first_number / second_number
    else:
        return 'Invalid Operator'

first_number = int(input('Enter first number: '))
operator = input('Enter a operator: ')
second_number = int(input('Enter second number: '))

print(calculator(first_number, operator, second_number))
