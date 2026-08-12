# Problem 13: Movie Ticket Price

# Question:
# Write a function named ticket_price that takes
# one integer (age) as input
# and returns the ticket price.

# Ticket Prices:
# - Children younger than 5 years: Free
# - Children from 5 years up to (but not including) 18 years: ₹100
# - Adults from 18 years up to (but not including) 60 years: ₹200
# - Senior citizens aged 60 years or older: ₹150

# Examples:

# Input:
# 3
# Output:
# Free

# Input:
# 10
# Output:
# 100

# Input:
# 35
# Output:
# 200

# Input:
# 65
# Output:
# 150




def ticket_price(age):

    if age < 5:
        return 'Free'
    elif age < 18:
        return 100
    elif age < 60:
        return 200
    else:
        return 150

age = int(input('Enter your age: '))

print('Ticket Price:', ticket_price(age))
