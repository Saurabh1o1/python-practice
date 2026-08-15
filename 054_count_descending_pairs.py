# Problem 54: Count Descending Adjacent Pairs

# Question:
# Write a program that asks the user to enter a positive
# integer.
#
# The program should count how many times a digit is greater
# than the digit immediately to its right.
#
# In other words, count the adjacent digit pairs where the
# left digit is greater than the right digit.
#
# Examples:
#
# Input:
# Enter a number: 58321
#
# Output:
# Descending pairs: 3
#
#
# Input:
# Enter a number: 24680
#
# Output:
# Descending pairs: 0
#
#
# Input:
# Enter a number: 13579
#
# Output:
# Descending pairs: 0
#
#
# Input:
# Enter a number: 987654
#
# Output:
# Descending pairs: 5
#
#
# Input:
# Enter a number: 554321
#
# Output:
# Descending pairs: 4




num = int(input('Enter a number: '))
previous_digit = None
count = 0

while num > 0:
    digit = num % 10
    new_digit = digit

    if previous_digit is not None:
        if new_digit > previous_digit:
            count = count + 1

    previous_digit = new_digit

    num = num // 10

print(f'Descending pairs: {count}')
