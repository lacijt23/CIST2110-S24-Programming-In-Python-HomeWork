# HW3.py
# Author: Laci Trull

# This Homework assignment is meant to test your ability to make functions within python as well as importing and using modules. This assignment might require you to do some research on your own. If you get stuck, try googling the problem, especially when it comes to importing and using the different modules.

# Hint you will want to enable word wrap in vscode (View -> Toggle Word Wrap) to make it easier to read the instructions.

# Question 1:
# Write a function that takes in a number and returns that number squared
# IE. If the user inputs 3, the function should return 9
num = int(input("Enter a number: "))
def square_number(num):
    """
    Returns the square of a given number.
    
    Parameters:
        num (int or float): The number to be squared.
        
    Returns:
        int or float: The square of the input number.
    """
    return num ** 2
print("That number squared is", square_number(num))
# Question 2:
# Write a function that takes in a string, a letter, and a number and returns the string with the letter replaced at the number index
# IE. If the user inputs "Hello World", "a", and 3, the function should return "Helao World"
# Hint: You will want to use the replace() function
input_string = input("Enter a string: ")
letter = input("Enter a letter: ")
number = int(input("Enter a number: "))
def replace_letter(string, letter, number):
    """
    Replaces a letter in a string at a given index.
    
    Parameters:
        string (str): The string to be modified.
        letter (str): The letter to be replaced.
        number (int): The index at which the letter will be replaced.
        
    Returns:
        str: The modified string.
    """
    return string[:number] + letter + string[number + 1:]
print(replace_letter(input_string, letter, number))
# Question 3:
# Write a function that takes in a number, a lower_bound, and an upper_bound and returns whether the number is within the bounds
# IE. If the user inputs 5, 1, and 10, the function should return True
input_number = int(input("Enter a number: "))
lower_bound = int(input("Enter a lower bound: "))
upper_bound = int(input("Enter an upper bound: "))
def within_bounds(number, lower_bound, upper_bound):
    """
    Checks if a number is within a given range.
    
    Parameters:
        number (int or float): The number to be checked.
        lower_bound (int or float): The lower end of the range.
        upper_bound (int or float): The upper end of the range.
        
    Returns:
        bool: True if the number is within the range, False otherwise.
    """
    return lower_bound <= number <= upper_bound
print(within_bounds(input_number, lower_bound, upper_bound))
# Question 4:
# write a function with parameters for a name, age, and favorite color. Return the following string using the parameters:
# "Hello, my name is <name>. I am <age> years old. My favorite color is <color>."
input_name = input("Enter your name: ")
input_age = int(input("Enter your age: "))
input_color = input("Enter your favorite color: ")
print("Hello, my name is", input_name, ". I am", input_age, "years old. My favorite color is", input_color + ".")
# Question 5:
# Write a function that asks the user for their name, age, and favorite color and then calls the function from question 4 using the user's input as the parameters.
# Hint: You will want to save the users input to variables and use them as the parameters for the function from question 4
input_name2 = input("Enter your name: ")
input_age2 = int(input("Enter your age: "))
input_color2 = input("Enter your favorite color: ")
def user_info(name, age, color):
    """
    Prints a string using the input parameters.
    
    Parameters:
        name (str): The user's name.
        age (int): The user's age.
        color (str): The user's favorite color.
        
    Returns:
        None
    """
input_name = input_name2
input_age = input_age2
input_color = input_color2
user_info(input_name, input_age, input_color)
print("Hello, my name is", input_name, ". I am", input_age, "years old. My favorite color is", input_color + ".")
# Question 6:
# import the random module and use it to generate a random number between 1 and 100
import random
random_number = random.randint(1, 100)
print("Random number:", random_number)
# Question 7:
# import the math module and use it to find the square root of 16 (hint: use the sqrt() function)
import math
number = 16
print("Square root of 16:", math.sqrt(number))
# Question 8:
# import the sys module and use it to print the version of python you are using
# this time import the module using the import "as" keyword
# hint: use the version attribute (sys.version)
import sys as s
print("Python version:", s.version)
# Question 9:
# import the os module and use it to print the current working directory. This time import the module using the from keyword
# hint: use the getcwd() function
import os
print("Current working directory:", os.getcwd())