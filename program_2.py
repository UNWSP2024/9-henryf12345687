# Program #2: Random Number File Writer
# Henry Forst
# 10/31/25
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).
import random
def random_number_file():
    amt_numbers = int(input("How many random numbers would you like to write (max 1000)? "))
    with open ("rannumber.txt","w") as file:
       for _ in range(amt_numbers):
           file.write(str(random.randint(1, 500)) + "\n")
random_number_file()