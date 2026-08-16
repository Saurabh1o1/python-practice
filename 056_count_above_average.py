# Problem 56: Count Numbers Greater Than the Average

# Question:
# Write a program that asks the user to enter 5 integers.
#
# Store the 5 numbers in a list.
#
# The program should:
# 1. Calculate the average of all 5 numbers.
# 2. Count how many numbers in the list are greater
#    than the average.
#
# Examples:
#
# Input:
# Enter number 1: 10
# Enter number 2: 20
# Enter number 3: 30
# Enter number 4: 40
# Enter number 5: 50
#
# Output:
# Average: 30.0
# Numbers greater than average: 2
#
#
# Input:
# Enter number 1: 5
# Enter number 2: 5
# Enter number 3: 5
# Enter number 4: 5
# Enter number 5: 5
#
# Output:
# Average: 5.0
# Numbers greater than average: 0




my_list = []
total = 0
count = 0
counter = 0

for i in range(1, 6):
    num = int(input('Enter a number: '))
    my_list.append(num)

for j in my_list:
    total = total + j
    count = count + 1

average = total / count

for k in my_list:
    if k > average:
        counter = counter + 1

print(f'Average: {average}')
print(f'Number greater than average: {counter}')
