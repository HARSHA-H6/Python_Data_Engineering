# Step1: Setting constants 
SCHOOL_NAME = "CARMEL JYOTHI HIGH SCHOOL"
CLASS_NAME = "CLASS X"
TOTAL_SUBJECT_MARKS = 50
TOTAL_MARKS = TOTAL_SUBJECT_MARKS*3
NUMBER_STUDENTS = 3

# Step2: Enter the students name, and there marks in the specific subject
student1 = input("Enter name of Student 1: ")
student1_phys_marks = int(input("Enter Physics marks out of 50 for Student 1: "))
student1_chem_marks = int(input("Enter Chemistry marks out of 50 for Student 1: "))
student1_math_marks = int(input("Enter Maths marks out of 50 for Student 1: " ))
student1_obtained_marks=student1_math_marks+student1_chem_marks+student1_phys_marks

# Step3: Convert the marks to percentage
student1_phys_perc = round((student1_phys_marks/TOTAL_SUBJECT_MARKS)*100,2)
student1_chem_perc = round((student1_chem_marks/TOTAL_SUBJECT_MARKS)*100,2)
student1_math_perc = round((student1_math_marks/TOTAL_SUBJECT_MARKS)*100,2)
student1_obtained_perc = round((student1_obtained_marks/TOTAL_MARKS)*100,2)

# Step4: Print the marks sheet
print(f"\n {SCHOOL_NAME} - {CLASS_NAME} - {student1}")

print(f"{'-'*75}")
print(f"| {'Subject':^10} | {'Total Marks':^10} | {'Marks Obtained':^10} | {'Percentage ':^10}|")
print(f"{'-'*75}")

print(f"| {'Physics':^10} | {TOTAL_SUBJECT_MARKS:^10} | {student1_phys_marks:^10} | {student1_phys_perc:^10} |")
print(f"| {'Chemistry':^10} | {TOTAL_SUBJECT_MARKS:^10} | {student1_chem_marks:^10} | {student1_chem_perc:^10} |")
print(f"| {'Maths':^10} | {TOTAL_SUBJECT_MARKS:^10} | {student1_math_marks:^10} | {student1_math_perc:^10} |")

print(f"{'-'*75}")
print(f"| {'Total':^10} | {TOTAL_MARKS:^10} | {student1_obtained_marks:^10} | {student1_obtained_perc:^10} |")
print(f"{'-'*75}")