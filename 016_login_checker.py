# Problem 16: Login Checker

# Question:
# Write a function named login_check that takes
# two strings: username and password.
#
# The login is successful only when BOTH the username
# and password are correct.
#
# Return:
# "Login Successful" -> if the username is "admin"
#                       AND the password is "python123"
#
# "Invalid Login"    -> otherwise.
#
# Examples:
#
# Input:
# admin
# python123
#
# Output:
# Login Successful
#
#
# Input:
# admin
# hello123
#
# Output:
# Invalid Login
#
#
# Input:
# user
# python123
#
# Output:
# Invalid Login




def login_check(username, password):
    if username == 'admin' and password == 'python123':
        return 'Login Successful'
    else:
        return 'Invalid Login'


username = input('Enter username: ')
password = input('Enter password: ')

print(login_check(username, password))