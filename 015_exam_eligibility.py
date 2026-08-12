# Problem 15: Exam Eligibility

# Question:
# Write a function named exam_eligibility that takes
# two values:
# marks and attendance.
#
# The function should determine whether a student
# is eligible to take the final exam.
#
# Return:
# "Eligible"     -> if the student has marks of 40 or more
#                   AND attendance of 75% or more.
#
# "Not Eligible" -> otherwise.
#
# However, a student with marks of 80 or more is eligible
# even if their attendance is below 75%.

# Examples:

# Input:
# 60
# 80

# Output:
# Eligible


# Input:
# 60
# 70

# Output:
# Not Eligible


# Input:
# 85
# 60

# Output:
# Eligible


# Input:
# 35
# 90

# Output:
# Not Eligible




def exam_eligibility(marks, attendance):

    if (marks >= 40 and attendance >= 75) or marks >= 80:
        return 'Eligible'
    else:
        return 'Not Eligible'

marks = int(input('Enter your marks: '))
attendance = int(input('Enter your attendance: '))

print(exam_eligibility(marks, attendance), 'for final exam.')
