#!/usr/bin/env python3

# Fibonacci Sequence Exercise 
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

while True:
    user_number = int(input("Enter a positive number of a term for the Fibonacci sequence"))
    

    if user_number <= 0:
        print("invalid number. Enter a positive number")
    else:  
        num1 = 0
        num2 = 1
        for i in range(user_number):
            total = num1 + num2
            print(num1)
            #print("")
            num1 = num2 
            num2 = total
        break

# your code breaks when a non-integer is entered -1
