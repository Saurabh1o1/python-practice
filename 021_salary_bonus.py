# Problem 21: Salary Bonus

# Question:
# Write a program that calculates an employee's bonus.
#
# The program should take three inputs:
# 1. Salary
# 2. Years of service
# 3. Performance rating
#
# Bonus rules:
# - An employee gets a 10% bonus if they have worked
#   for at least 5 years AND their performance rating
#   is 4 or higher.
#
# - An employee gets a 5% bonus if they have worked
#   for at least 3 years AND their performance rating
#   is 3 or higher.
#
# - Everyone else gets no bonus.
#
# The program should calculate and print the bonus amount.
#
# Examples:
#
# Input:
# Salary: 50000
# Years: 6
# Rating: 5
#
# Output:
# Bonus: 5000.0
#
#
# Input:
# Salary: 50000
# Years: 4
# Rating: 4
#
# Output:
# Bonus: 2500.0
#
#
# Input:
# Salary: 50000
# Years: 2
# Rating: 5
#
# Output:
# Bonus: 0





salary = int(input('Enter Salary: '))
years = int(input('Enter Years: '))
rating = int(input('Enter Rating: '))

if years >= 5 and rating >= 4:
    bonus = salary * 0.10
elif years >= 3 and rating >= 3:
    bonus = salary * 0.05
else:
    bonus = 0

print('Bonus:', bonus)
