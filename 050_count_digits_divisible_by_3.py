# Problem 50: Count Digits Divisible by 3

# Question:
# Write a program that asks the user to enter a positive
# integer.
#
# The program should count how many non-zero digits
# are divisible by 3.
#
# Examples:
#
# Input:
# Enter a number: 58321
#
# Output:
# Number of digits divisible by 3: 1
#
#
# Input:
# Enter a number: 24680
#
# Output:
# Number of digits divisible by 3: 1
#
#
# Input:
# Enter a number: 13579
#
# Output:
# Number of digits divisible by 3: 2
#
#
# Input:
# Enter a number: 10000
#
# Output:
# Number of digits divisible by 3: 0




num = int(input('Enter a number: '))
count = 0

while num > 0:
    digit = num % 10
    if digit > 0 and digit % 3 == 0 :
        count = count + 1

    num = num // 10

print(f'Number of digits divisible by 3: {count}')
