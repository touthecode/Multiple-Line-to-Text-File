import sys

print(sys.path)

with open("C:/Users/Tou/Desktop/School/OOP/Python Stuff/Multiline/mylife.txt") as line_output:

    # Create a function to add initial line
    line_input = input("PLease write the line you desire: ")
    line_output.write(line_input + "\n")

    print("Would you like to continue? y/n?")

    # Setup decision input for the loop function later
    decision = input(str("y for yes, n for no: "))
    decision = decision.lower()

    while decision == "y":
        if decision == "y":
            line_input = input("PLease write the line you desire: ")
            line_output.write(line_input + "\n")
            print("Would you like to continue? y/n?")
            decision = input(str("y for yes, n for no: "))
            decision = decision.lower()
        else:
            break