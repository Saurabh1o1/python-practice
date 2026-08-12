# Problem 17: Electricity Bill Calculator

# Question:
# Write a function named electricity_bill that takes
# one integer (units) as input and returns the total bill.
#
# The electricity charges are:
# - First 100 units: ₹5 per unit
# - Next 100 units: ₹7 per unit
# - Units above 200: ₹10 per unit
#
# The bill should be calculated progressively.
#
# Example:
#
# Input: 80
# Output: 400
#
# Input: 150
# Output: 850
#
# Input: 250
# Output: 1700




def electricity_bill(units):
    if units <= 100:
        bill = units * 5
        return bill
    elif units <= 200:
        bill = 500 + (units - 100) * 7
        return bill
    else:
        bill = 500 + 700 + (units - 200) * 10
        return bill


units = int(input('Enter Units: '))

print('Total Bill: ', electricity_bill(units))