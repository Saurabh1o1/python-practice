# Problem 22: Delivery Charge

# Question:
# Write a program that calculates the delivery charge
# for an online order.
#
# The program should take three inputs:
# 1. Order amount
# 2. Delivery distance in km
# 3. Whether the customer is a member
#
# Rules:
#
# - If the customer is a member AND the order amount
#   is at least ₹500, delivery is FREE.
#
# - Otherwise, if the order amount is at least ₹500
#   AND the distance is 5 km or less, the delivery
#   charge is ₹40.
#
# - Otherwise, if the order amount is at least ₹500,
#   the delivery charge is ₹60.
#
# - If the order amount is less than ₹500,
#   the delivery charge is ₹80.
#
# Examples:
#
# Input:
# Order amount: 700
# Distance: 3
# Member: yes
#
# Output:
# Delivery Charge: 0
#
#
# Input:
# Order amount: 700
# Distance: 3
# Member: no
#
# Output:
# Delivery Charge: 40
#
#
# Input:
# Order amount: 700
# Distance: 8
# Member: no
#
# Output:
# Delivery Charge: 60
#
#
# Input:
# Order amount: 300
# Distance: 2
# Member: yes
#
# Output:
# Delivery Charge: 80




amount = float(input('Enter the amount: '))
distance = float(input('Enter the distance: '))
membership = input('Enter the membership detail: ')

if amount >= 500 and membership == 'yes':
    charges = 0
elif amount >= 500 and distance <= 5:
    charges = 40
elif amount >= 500:
    charges = 60
else:
    charges = 80


print('Delivery Charge:', charges)