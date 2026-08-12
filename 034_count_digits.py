# Problem 34: Count Digits

# Question:
# Write a program that asks the user to enter a positive integer.
#
# The program should count how many digits the number contains.
#
# Example:
#
# Input:
# Enter a number: 58321
#
# Output:
# Number of digits: 5
#
#
# More examples:
#
# Input:
# Enter a number: 7
#
# Output:
# Number of digits: 1
#
#
# Input:
# Enter a number: 1000
#
# Output:
# Number of digits: 4




num = int(input('Enter a number: '))
count = 0

while num > 0:
    count += 1
    num //= 10

print(f'Number of digits: {count}')
