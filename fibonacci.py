#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

n = input("How many terms do you want to print? ")

if n.isdigit() and int(n) > 0:
    n = int(n)
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
else:
    print("Please enter a positive integer.")

