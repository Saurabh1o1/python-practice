# Problem 26: Sum of Numbers

# Question:
# Write a program that asks the user for a positive integer N.
#
# The program should calculate the sum of all numbers from
# 1 to N.
#
# Example:
#
# Input:
# Enter N: 5
#
# Output:
# Sum: 15
#
# Because:
# 1 + 2 + 3 + 4 + 5 = 15
#
#
# More examples:
#
# Input:
# Enter N: 1
#
# Output:
# Sum: 1
#
#
# Input:
# Enter N: 10
#
# Output:
# Sum: 55



num = int(input('Enter N: '))
total = 0

for i in range(1, num + 1):
    total = total + i

print('Sum:', total)