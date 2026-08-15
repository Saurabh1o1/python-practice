# Problem 53: Largest Difference Between Consecutive Digits

# Question:
# Write a program that asks the user to enter a positive
# integer.
#
# The program should find the largest absolute difference
# between any two consecutive digits in the number.
#
# Examples:
#
# Input:
# Enter a number: 58321
#
# Output:
# Largest difference: 5
#
#
# Input:
# Enter a number: 24680
#
# Output:
# Largest difference: 2
#
#
# Input:
# Enter a number: 13579
#
# Output:
# Largest difference: 2
#
#
# Input:
# Enter a number: 9870
#
# Output:
# Largest difference: 7




num = int(input('Enter a number: '))
previous_digit = None
latest_diff = 0

while num > 0:
    digit = num % 10
    new_digit = digit

    if previous_digit is not None:
        diff = abs(new_digit - previous_digit)

        if diff > latest_diff:
            latest_diff = diff

    previous_digit = new_digit

    num = num // 10

print(f'Largest difference: {latest_diff}')
