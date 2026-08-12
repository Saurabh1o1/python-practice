# Problem 11: Quadrant Checker

# Question:
# Write a function named quadrant that takes
# two integers (x, y) as input
# and returns the position of the point.

# Return:
# "Quadrant I"    -> x > 0 and y > 0
# "Quadrant II"   -> x < 0 and y > 0
# "Quadrant III"  -> x < 0 and y < 0
# "Quadrant IV"   -> x > 0 and y < 0
# "Origin"        -> x == 0 and y == 0
# "X-Axis"        -> y == 0 and x != 0
# "Y-Axis"        -> x == 0 and y != 0

# Example:

# Input:
# 5
# 8
# Output:
# Quadrant I

# Input:
# -4
# 6
# Output:
# Quadrant II

# Input:
# -7
# -2
# Output:
# Quadrant III

# Input:
# 9
# -3
# Output:
# Quadrant IV

# Input:
# 0
# 0
# Output:
# Origin

# Input:
# 0
# 5
# Output:
# Y-Axis

# Input:
# 8
# 0
# Output:
# X-Axis




def quadrant(x, y):

    if x > 0 and y > 0:
        return 'Quadrant I'
    elif x < 0 and y > 0:
        return 'Quadrant II'
    elif x < 0 and y < 0:
        return 'Quadrant III'
    elif x > 0 and y < 0:
        return 'Quadrant IV'
    elif x == 0 and y == 0:
        return 'Origin'
    elif x != 0 and y == 0:
        return 'X-Axis'
    elif x == 0 and y != 0:
        return 'Y-Axis'

x = int(input('Enter the value of X: '))
y = int(input('Enter the value of Y: '))

print(quadrant(x, y))