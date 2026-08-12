# Problem 29: Sum of Even Numbers

# Question:
# Write a program that asks the user for a positive integer N.
#
# The program should calculate the sum of all even numbers
# between 1 and N, including N if it is even.
#
# Example:
#
# Input:
# Enter N: 10
#
# Output:
# Sum of even numbers: 30
#
# Because:
# 2 + 4 + 6 + 8 + 10 = 30
#
#
# More examples:
#
# Input:
# Enter N: 7
#
# Output:
# Sum of even numbers: 12
#
#
# Input:
# Enter N: 1
#
# Output:
# Sum of even numbers: 0




num = int(input('Enter N: '))
total = 0

for i in range(1, num + 1):
    if i % 2 == 0:
        total += i


print(f'Sum of even numbers: {total}')