import sys

print(sys.path)

with open("C:/Users/Tou/Desktop/School/OOP/Python Stuff/Multiline/mylife.txt") as line_output:

    # Create a function to add initial line
    line_input =  input("PLease write the line you desire: ")
    line_output.write(line_input + "\n")
