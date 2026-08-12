# Problem 7: Leap Year

# Question:
# Write a function named is_leap_year that takes one integer (year)
# as input and returns:
# True if the year is a leap year.
# False otherwise.

# Rules:
# A year is a leap year if:
# - It is divisible by 4, and
# - It is not divisible by 100,
#   OR
# - It is divisible by 400.

# Example:
# Input: 2024
# Output: True

# Input: 2023
# Output: False

# Input: 1900
# Output: False

# Input: 2000
# Output: True




def is_leap_year(year):

    if year % 4 == 0:
        if year % 100 != 0:
            return True
        else:
            if year % 400 == 0:
                return True
            else:
                return False    
    else:
        return False

year = int(input('Enter the year: '))

print(is_leap_year(year))