# Problem 57: Replace Negative Numbers
#
# Question:
# Write a program that asks the user to enter 5 integers.
#
# The program should store all 5 numbers in a list.
#
# Then, replace every negative number in the list with 0.
#
# Finally, print the modified list.
#
# Examples:
#
# Input:
# Enter a number: 10
# Enter a number: -5
# Enter a number: 8
# Enter a number: -2
# Enter a number: 15
#
# Output:
# [10, 0, 8, 0, 15]
#
#
# Input:
# Enter a number: -4
# Enter a number: -7
# Enter a number: 3
# Enter a number: 0
# Enter a number: 9
#
# Output:
# [0, 0, 3, 0, 9]
#
#
# Input:
# Enter a number: 5
# Enter a number: 10
# Enter a number: 15
# Enter a number: 20
# Enter a number: 25
#
# Output:
# [5, 10, 15, 20, 25]




my_list = []

for i in range(1, 6):
    num = int(input(f'Enter a number {i}: '))
    my_list.append(num)

for j in range(len(my_list)):
    if my_list[j] < 0:
        my_list[j] = 0

print(my_list)
