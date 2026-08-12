# Problem 41: Count Zeros

# Question:
# Write a program that asks the user to enter a positive integer.
#
# The program should count how many zero digits
# are present in the number.
#
# Examples:
#
# Input:
# Enter a number: 508020
#
# Output:
# Number of zeros: 3
#
#
# Input:
# Enter a number: 12345
#
# Output:
# Number of zeros: 0
#
#
# Input:
# Enter a number: 1000
#
# Output:
# Number of zeros: 3




num = int(input('Enter a number: '))
count = 0

while num > 0:
    digit = num % 10

    if digit == 0:
        count += 1

    num //= 10

print(f'Number of zeros: {count}')
