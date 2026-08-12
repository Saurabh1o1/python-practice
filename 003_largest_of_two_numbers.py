# Problem 3: Largest of Two Numbers

# Question:
# Write a function named larger_number that takes two integers as input
# and returns the larger number.

# Example:
# Input: 10 20
# Output: 20

# Input: 15 5
# Output: 15




def larger_number(num1, num2):

    if num1 >= num2:
        return num1
    else:
        return num2

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

print(larger_number(num1, num2))