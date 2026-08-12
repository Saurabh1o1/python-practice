# Problem 19: Loan Eligibility

# Question:
# Write a function named loan_eligibility that takes
# three values:
# age, income, and credit_score.
#
# The function should determine whether a person is
# eligible for a loan.
#
# Return:
# "Eligible" -> if the person is at least 21 years old,
#               has an income of at least ₹25,000,
#               AND has a credit score of at least 700.
#
# "Eligible" -> if the person is at least 30 years old,
#               has an income of at least ₹20,000,
#               AND has a credit score of at least 650.
#
# "Not Eligible" -> otherwise.
#
# Examples:
#
# Input:
# 25
# 30000
# 720
#
# Output:
# Eligible
#
#
# Input:
# 25
# 30000
# 650
#
# Output:
# Not Eligible
#
#
# Input:
# 35
# 22000
# 670
#
# Output:
# Eligible
#
#
# Input:
# 20
# 50000
# 800
#
# Output:
# Not Eligible




def loan_eligibility(age, income, credit_score):
    if ((age >= 21 and income >= 25000 and credit_score >= 700) or
        (age >= 30 and income >= 20000 and credit_score >= 650)):
        return 'Eligible'
    else:
        return 'Not Eligible'


age = int(input('Enter age: '))
income = int(input('Enter income: '))
credit_score = int(input('Enter credit score: '))

print(loan_eligibility(age, income, credit_score))