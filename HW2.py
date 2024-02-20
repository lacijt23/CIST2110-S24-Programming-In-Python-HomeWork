# HW2.py
# Author: Laci Trull


# Question 1:
# Write some code that prompts the user for their age. Depending on the input:

# If the age is less than 13, print "You are a child."
# If the age is between 13 and 19, print "You are a teenager."
# If the age is 20 or older, print "You are an adult."
number = int(input("What is your age?" ))
if number < 13:
    print("You are a child.")
if number in range(13,19):
    print("You are a teenager")
if number >= 20:
    print("You are an adult.")

    # Question 2:
    # Write some code to display the following pattern using a for or while loop:
    # 1
    # 12
    # 123
    # 1234
    # 12345
    for i in range(1, 6):
        for j in range(1, i + 1):
            print(j, end="")
        print()

# Question 3:
# Write some code that prompts the user to input 10 numbers. After all the numbers are inputted, the program should display:
total = 0
for(i) in range(10):
    number = int(input("Please enter a number. "))
    total += number
# The highest number.
highest = float('-inf')
if number > highest:
    highest = number
    print(highest)
# The lowest number.
lowest = float('inf')
if number < lowest:
    lowest = number
    print(lowest)
# The average of all the numbers.
average = total / 10
print(average)
# Hint 1: You will need to use a for loop and a counter variable to keep track of the total sum of the numbers.
# Hint 2: You will need to use an if statement to keep track of the highest and lowest numbers.


# Question 4:
# Vowel Counter - Write some code that prompts the user to enter a string. The program should then display the number of vowels in the string. IE. If the user enters "Hello World", the program should display 3.
# the vowels are a, e, i, o, u
# Hint: convert the string to lowercase and use a for loop with a counter variable and an if statement
def count_vowels(string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

user_input = input("Enter a string: ")
num_vowels = count_vowels(user_input)
print("Number of vowels:", num_vowels)