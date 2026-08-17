# Problem 60: Replace Number Occurrences
#
# Question:
# Write a program that asks the user to enter 5 integers
# and stores them in a list.
#
# Then ask the user to enter two more integers:
# 1. The number to replace
# 2. The replacement number
#
# The program should replace every occurrence of the first
# number with the second number.
#
# Finally, print the modified list.
#
# Examples:
#
# Input:
# Enter a number 1: 10
# Enter a number 2: 20
# Enter a number 3: 10
# Enter a number 4: 30
# Enter a number 5: 10
# Enter number to replace: 10
# Enter replacement number: 5
#
# Output:
# [5, 20, 5, 30, 5]
#
#
# Input:
# Enter a number 1: 4
# Enter a number 2: 7
# Enter a number 3: 9
# Enter a number 4: 2
# Enter a number 5: 6
# Enter number to replace: 9
# Enter replacement number: 0
#
# Output:
# [4, 7, 0, 2, 6]
#
#
# Input:
# Enter a number 1: 3
# Enter a number 2: 5
# Enter a number 3: 7
# Enter a number 4: 8
# Enter a number 5: 2
# Enter number to replace: 10
# Enter replacement number: 0
#
# Output:
# [3, 5, 7, 8, 2]




my_list = []

for i in range(1, 6):
    num = int(input(f'Enter a number {i}: '))
    my_list.append(num)

number = int(input('Enter number to replace: '))
replace = int(input('Enter replacement number: '))

for j in range(len(my_list)):
    if number == my_list[j]:
        my_list[j] = replace

print(my_list)
