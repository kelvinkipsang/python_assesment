# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# Hints:
# Use __init__ method to construct some parameters

# Solution:
class InputOutString(object):
    # code goes here
<<<<<<< HEAD

    def printer(x):
        x = raw_input("enter text")
        print str(x)
    printer()
=======
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = raw_input("Write Down Any Word : ")

>>>>>>> f6ef550329a1affe6fcc15ab6406c12c7cf1b8a6
