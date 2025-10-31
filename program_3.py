# Program #3: Average Numbers
# Henry Forst
# 10/31/25
# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all of the numbers stored in the file and calculates their total.  

# The program should handle the following exceptions: 

# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file 
# are converted to a number.
def sum_numbers_from_file():
    try:
        with open("numbers.txt","r") as file:
            number = [line.strip() for line in file]
        total = 0
        count = 0
        for line in number:
            try:
                total += int(line.strip())
                count += 1
            except ValueError:
                print(f"ValueError: Could not convert line to a number.")
        print("The sum of the numbers in the file is:", total)
    except IOError:
        print("IOError: There was a problem when executing the code.")

# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()