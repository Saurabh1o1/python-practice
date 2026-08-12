# Problem 12: BMI Category

# Question:
# Write a function named bmi_category that takes
# one decimal number (bmi) as input
# and returns the BMI category.

# Return:
# "Underweight" -> if the BMI is less than 18.5
# "Normal"      -> if the BMI is at least 18.5 but less than 25
# "Overweight"  -> if the BMI is at least 25 but less than 30
# "Obese"       -> if the BMI is 30 or greater

# Examples:

# Input:
# 17.2

# Output:
# Underweight


# Input:
# 22.8

# Output:
# Normal


# Input:
# 27.4

# Output:
# Overweight


# Input:
# 31.6

# Output:
# Obese




def bmi_category(bmi):

    if bmi < 18.5:
        return 'Underweight'
    elif bmi < 25:
        return 'Normal'
    elif bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'

bmi = float(input('Enter your BMI: '))

print(bmi_category(bmi))
