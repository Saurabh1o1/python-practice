# Problem 14: Discount Calculator

# Question:
# Write a function named discount that takes
# one integer (amount) as input
# and returns the discount percentage.

# Discount Rules:
# - If the purchase amount is less than ₹1000,
#   return 0.
#
# - If the purchase amount is at least ₹1000
#   but less than ₹5000,
#   return 10.
#
# - If the purchase amount is at least ₹5000
#   but less than ₹10000,
#   return 20.
#
# - If the purchase amount is ₹10000 or more,
#   return 30.

# Examples:

# Input:
# 750
# Output:
# 0

# Input:
# 2500
# Output:
# 10

# Input:
# 7000
# Output:
# 20

# Input:
# 15000
# Output:
# 30




def discount(amt):

    if amt < 1000:
        return 0
    elif amt < 5000:
        return 10
    elif amt < 10000:
        return 20
    else:
        return 30

amount = int(input('Enter the amount: '))

print('Discount:', discount(amount),'%')
