# Program #1: Item Counter
# Henry Forst
# 10/31/25
# Program 1
# Assume a file containing a series of names (as strings) is named names.txt 
# (Use the included example file names.txt) and exists on the computer's disk.
# Write a program that displays the number of names that are stored in the file.

def count_file_lines():
    with open("names.txt","r") as file:
        names = [line.strip()for line in file ]
        name_count = len(names)
        print(f"There are {name_count} names in the file." )




# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()