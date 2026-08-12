# Problem 5: Smallest of Two Numbers

# Question:
# Write a function named smaller_number that takes two integers as input
# and returns the smaller number.

# Example:
# Input: 10 20
# Output: 10

# Input: 15 5
# Output: 5

# Input: -5 -2
# Output: -5

# Input: 7 7
# Output: 7




def smaller_number(num1, num2):

    if num1 <= num2:
        return num1
    else:
        return num2

num1 = int(input('Enter first number: ')) 
num2 = int(input('Enter second number: '))

print(smaller_number(num1, num2))
