'''
Ask the user for his or her favorite number and double it.
For example: if my favorite number is 7, output an integer value of 14
'''


# VARIABLES ----------------------------------------------------------------------------------------------------

num = input("What is you favorite number: ")

# FUNCTIONS ----------------------------------------------------------------------------------------------------

def userInput(ctx):
    return int(ctx) * 2

# MAINSETUP ----------------------------------------------------------------------------------------------------

userInput(num)