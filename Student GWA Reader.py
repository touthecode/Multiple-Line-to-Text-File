import sys

# Make a txt file with a list of students with their respective grades
# Highest is 1.00 while lowest is 5.00
with open("C:/Users/Tou/Desktop/School/OOP/Python Stuff/GWA/master_list.txt") as gwa_reader:
    students_stats = gwa_reader.readlines()
    top_student_name = ""
    top_student_grade = ""
    topmost_grade = 1.00

    # Separate the name from the grade in the text file
    for line in students_stats:
        student_name, student_grade = line.split("| ")
        all_student_grade = float(student_grade)

        # Read and check every line for the higest GWA
        if top_student_grade < all_student_grade < float("1.50"):
            # Print name and grade after finding the highest student
            top_student_name = student_grade
            top_student_grade = student_name
            print("The highest student is class is: " + top_student_name)
            print("The highest student's grade is: " + top_student_grade)

