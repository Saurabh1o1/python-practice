# Problem 8: Grade Calculator

# Question:
# Write a function named get_grade that takes one integer (marks)
# as input and returns the corresponding grade.

# Rules:
# Marks >= 90  -> 'A'
# Marks >= 75  -> 'B'
# Marks >= 60  -> 'C'
# Marks >= 40  -> 'D'
# Marks < 40   -> 'F'

# Example:
# Input: 95
# Output: A

# Input: 80
# Output: B

# Input: 65
# Output: C

# Input: 45
# Output: D

# Input: 30
# Output: F




def get_grade(marks):

    if marks < 0 or marks > 100:
        return "Invalid Marks"
    else:
        if marks >= 90:
            return 'A'
        elif marks >= 75:
            return 'B'
        elif marks >= 60:
            return 'C'
        elif marks >= 40:
            return 'D'
        else:
            return 'F'

marks = int(input('Enter your marks: '))

print(get_grade(marks))
