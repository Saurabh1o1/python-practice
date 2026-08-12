# Problem 25: Movie Recommendation

# Question:
# Write a program that recommends whether a movie is
# suitable for a viewer.
#
# The program should take three inputs:
# 1. Age of the viewer
# 2. Movie rating out of 10
# 3. Whether the viewer is accompanied by an adult
#
# Rules:
#
# - A viewer aged 18 or above can watch the movie if
#   the rating is at least 6.
#
# - A viewer under 18 can watch the movie if the rating
#   is at least 8 AND they are accompanied by an adult.
#
# - A viewer aged 13 to 17 can watch the movie if the
#   rating is at least 9, even without an adult.
#
# - Everyone else gets "Not Recommended".
#
# Output:
# Print "Recommended" or "Not Recommended".
#
# Examples:
#
# Input:
# Age: 25
# Rating: 7
# Adult: no
#
# Output:
# Recommended
#
#
# Input:
# Age: 15
# Rating: 8
# Adult: yes
#
# Output:
# Recommended
#
#
# Input:
# Age: 15
# Rating: 8
# Adult: no
#
# Output:
# Not Recommended
#
#
# Input:
# Age: 15
# Rating: 9
# Adult: no
#
# Output:
# Recommended
#
#
# Input:
# Age: 10
# Rating: 9
# Adult: yes
#
# Output:
# Recommended




age = int(input('Age: '))
rating = float(input('Rating: '))
adult = input('Adult: ')

if age >= 18 and rating >= 6:
    recommendation = 'Recommended'
elif age < 18 and rating >= 8 and adult == 'yes':
    recommendation = 'Recommended'
elif age in range(13, 18) and rating >= 9:
    recommendation = 'Recommended'
else:
    recommendation = 'Not Recommended'


print(recommendation)
