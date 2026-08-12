# Problem 28: Factorial

# Question:
# Write a program that asks the user for a positive integer N.
#
# The program should calculate the factorial of N.
#
# The factorial of N means multiplying all positive integers
# from 1 up to N.
#
# Example:
#
# Input:
# Enter N: 5
#
# Output:
# Factorial: 120
#
# Because:
# 1 × 2 × 3 × 4 × 5 = 120
#
#
# More examples:
#
# Input:
# Enter N: 3
#
# Output:
# Factorial: 6
#
#
# Input:
# Enter N: 1
#
# Output:
# Factorial: 1




num = int(input('Enter N: '))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f'Factorial: {factorial}')
