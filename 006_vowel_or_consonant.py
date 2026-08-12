# Problem 6: Vowel or Consonant

# Question:
# Write a function named vowel_or_consonant that takes one character
# as input and returns:
# "Vowel" if the character is a vowel (a, e, i, o, u)
# "Consonant" otherwise.

# Rules:
# - Assume the user enters only one alphabet.
# - Ignore uppercase letters for now (use lowercase only).
# - Use if-else statements.
# - Do not use loops.
# - Take input from the user.
# - Print the function's return value.

# Example:
# Input: a
# Output: Vowel

# Input: e
# Output: Vowel

# Input: z
# Output: Consonant

# Input: m
# Output: Consonant




def vowel_or_consonant(char):

    if char == 'a':
        return 'Vowel'
    elif char == 'e':
            return 'Vowel'
    elif char == 'i':
            return 'Vowel'
    elif char == 'o':
            return 'Vowel'
    elif char == 'u':
            return 'Vowel'
    else:
        return 'Consonant'

char = input('Enter an alphabet: ')

print(vowel_or_consonant(char))
