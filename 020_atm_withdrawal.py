# Problem 20: ATM Withdrawal

# Question:
# Write a function named atm_withdrawal that takes
# two values:
# balance and amount.
#
# The function should determine whether the withdrawal
# can be completed.
#
# Rules:
# - The withdrawal amount must be greater than 0.
# - The withdrawal amount must be a multiple of 100.
# - The withdrawal amount must not be greater than the balance.
# - If all three conditions are satisfied, return the
#   remaining balance.
# - If the amount is not valid, return "Invalid Amount".
# - If the amount is valid but greater than the balance,
#   return "Insufficient Balance".
#
# Examples:
#
# Input:
# Balance = 5000
# Amount = 1200
#
# Output:
# 3800
#
#
# Input:
# Balance = 5000
# Amount = 1250
#
# Output:
# Invalid Amount
#
#
# Input:
# Balance = 5000
# Amount = 6000
#
# Output:
# Insufficient Balance




def atm_withdrawal(balance, amount):
    if amount > 0 and amount % 100 == 0 and amount <= balance:
        return balance - amount
    elif amount <= 0 or amount % 100 != 0:
        return 'Invalid Amount'
    elif amount > balance:
        return 'Insufficient Balance'


balance = int(input('Enter the balance: '))
amount = int(input('Enter the amount: '))

print(atm_withdrawal(balance, amount))
