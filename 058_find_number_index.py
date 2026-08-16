# Problem 58: Find the Index of a Number
#
# Question:
# Write a program that asks the user to enter 5 integers
# and stores them in a list.
#
# Then ask the user to enter another integer to search for.
#
# The program should find the first occurrence of that number
# in the list and print its index.
#
# If the number is not present in the list, print:
# "Number not found"
#
# Examples:
#
# Input:
# Enter number 1: 10
# Enter number 2: 20
# Enter number 3: 30
# Enter number 4: 20
# Enter number 5: 50
# Enter number to search: 20
#
# Output:
# Number found at index: 1
#
#
# Input:
# Enter number 1: 5
# Enter number 2: 8
# Enter number 3: 12
# Enter number 4: 15
# Enter number 5: 20
# Enter number to search: 7
#
# Output:
# Number not found
#
#
# Input:
# Enter number 1: 4
# Enter number 2: 9
# Enter number 3: 4
# Enter number 4: 7
# Enter number 5: 4
# Enter number to search: 4
#
# Output:
# Number found at index: 0



my_list = []

for i in range(1, 6):
    num = int(input(f'Enter a number {i}: '))
    my_list.append(num)

search = int(input('Enter number to search: '))

for j in range(len(my_list)):
    if search == my_list[j]:
        found = True
        break
    else:
        found = False

if found:
    print(f'Number found at index: {j}')
else:
    print('Number not found')
