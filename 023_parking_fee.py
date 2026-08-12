# Problem 23: Parking Fee Calculator

# Question:
# Write a program that calculates the parking fee.
#
# The program should take three inputs:
# 1. Vehicle type
# 2. Number of hours parked
# 3. Whether it is a weekend
#
# Vehicle types:
# "bike" or "car"
#
# Rules:
#
# - A car parked for more than 5 hours costs ₹150.
#
# - A bike parked for 2 hours or less costs ₹30.
#
# - A car parked for 5 hours or less costs ₹50 per hour.
#
# - A bike parked for more than 2 hours costs ₹20 per hour.
#
# - On weekends, add an additional ₹20 to the
#   calculated parking fee.
#
# Examples:
#
# Input:
# Vehicle: bike
# Hours: 2
# Weekend: no
#
# Output:
# Parking Fee: 30
#
#
# Input:
# Vehicle: car
# Hours: 4
# Weekend: no
#
# Output:
# Parking Fee: 200
#
#
# Input:
# Vehicle: car
# Hours: 7
# Weekend: yes
#
# Output:
# Parking Fee: 170
#
#
# Input:
# Vehicle: bike
# Hours: 4
# Weekend: yes
#
# Output:
# Parking Fee: 100




vehicle = input('Enter the type: ')
hours = float(input('Enter the hours: '))
weekend = input('Weekend: ')

if vehicle == 'bike':
    if hours > 2:
        fee = 20 * hours
    else:
        fee = 30

elif vehicle == 'car':
    if hours <= 5:
        fee = 50 * hours
    else:
        fee = 150 


if weekend == 'yes':
    fee += 20


print('Parking Fee:', fee)
