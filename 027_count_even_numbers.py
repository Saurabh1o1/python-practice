# Problem 27: Count Even Numbers

# Question:
# Write a program that asks the user for a positive integer N.
#
# The program should count how many even numbers exist
# between 1 and N, including N.
#
# Example:
#
# Input:
# Enter N: 10
#
# Output:
# Even numbers: 5
#
# Because:
# 2, 4, 6, 8, 10
#
#
# More examples:
#
# Input:
# Enter N: 5
#
# Output:
# Even numbers: 2
#
#
# Input:
# Enter N: 1
#
# Output:
# Even numbers: 0




num = int(input('Enter N: '))
count = 0

for i in range(1, num + 1):
    if i % 2 == 0:
        count += 1

print(f'Even numbers: {count}')