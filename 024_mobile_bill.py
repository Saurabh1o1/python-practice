# Problem 24: Mobile Bill Calculator

# Question:
# Write a program that calculates a customer's monthly mobile bill.
#
# The program should take three inputs:
# 1. Plan type
# 2. Data used in GB
# 3. Whether the customer has a loyalty membership
#
# Plan types:
# "basic" or "premium"
#
# Rules:
#
# - A loyalty member gets a ₹100 discount if the monthly
#   bill is ₹1000 or more.
#
# - A premium plan costs ₹699 for up to 20 GB.
#
# - A basic plan costs ₹399 for up to 10 GB.
#
# - If a basic-plan customer uses more than 10 GB,
#   charge ₹30 for every GB above 10 GB.
#
# - If a premium-plan customer uses more than 20 GB,
#   charge ₹20 for every GB above 20 GB.
#
# Examples:
#
# Input:
# Plan: basic
# Data: 8
# Loyalty Member: no
#
# Output:
# Bill: 399
#
#
# Input:
# Plan: basic
# Data: 13
# Loyalty Member: no
#
# Output:
# Bill: 489
#
#
# Input:
# Plan: premium
# Data: 25
# Loyalty Member: yes
#
# Output:
# Bill: 799




plan = input('Plan: ')
data = float(input('Data: '))
loyalty = input('Loyalty Member: ')

if plan == 'premium':
    if data > 20:
        extra_data = data - 20
        bill = 699 + (20 * extra_data)
    else:
        bill = 699

elif plan == 'basic':
    if data > 10:
        extra_data = data - 10
        bill = 399 + (30 * extra_data)
    else:
        bill = 399

if loyalty == 'yes' and bill >= 1000:
    bill -= 100


print('Bill:', bill)
