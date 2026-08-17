# Problem 59: Count Number Occurrences
#
# Question:
# Write a program that asks the user to enter 5 integers
# and stores them in a list.
#
# Then ask the user to enter another integer to search for.
#
# The program should count how many times the search number
# appears in the list.
#
# Finally, print the number of occurrences.
#
# Examples:
#
# Input:
# Enter a number 1: 10
# Enter a number 2: 20
# Enter a number 3: 20
# Enter a number 4: 30
# Enter a number 5: 20
# Enter number to search: 20
#
# Output:
# Number of occurrences: 3
#
#
# Input:
# Enter a number 1: 5
# Enter a number 2: 8
# Enter a number 3: 12
# Enter a number 4: 15
# Enter a number 5: 20
# Enter number to search: 7
#
# Output:
# Number of occurrences: 0
#
#
# Input:
# Enter a number 1: 4
# Enter a number 2: 4
# Enter a number 3: 4
# Enter a number 4: 4
# Enter a number 5: 4
# Enter number to search: 4
#
# Output:
# Number of occurrences: 5




my_list = []


for i in range(1, 6):
    num = int(input(f'Enter a number {i}: '))
    my_list.append(num)

search = int(input('Enter number to search: '))
count = 0

for j in my_list:
    if j == search:
        count = count + 1

print(f'Number of occurrences: {count}')
