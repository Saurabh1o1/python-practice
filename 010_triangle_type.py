# Problem 10: Triangle Type

# Question:
# Write a function named triangle_type that takes
# three integers (side1, side2, side3)
# as input and returns the type of triangle.

# Return:
# "Equilateral"  -> All three sides are equal.
# "Isosceles"    -> Exactly two sides are equal.
# "Scalene"      -> All three sides are different.

# Example:
# Input:
# 5
# 5
# 5
# Output:
# Equilateral

# Input:
# 5
# 5
# 8
# Output:
# Isosceles

# Input:
# 3
# 4
# 5
# Output:
# Scalene




def triangle_type(side1, side2, side3):

    if side1 == side2 and side2 == side3 and side3 == side1:
        return 'Equilateral'
    elif side1 != side2 and side2 != side3 and side3 != side1:
        return 'Scalene'
    else:
        return 'Isosceles'

side1 = int(input('Enter first side: '))
side2 = int(input('Enter second side: '))
side3 = int(input('Enter third side: '))

print(triangle_type(side1, side2, side3))
