# This is the in-built csv module in python
# gives the ability to read and write a csv file (Comma Separated Values)
import csv

# Load student data from file
def load_student_data(filename):
    # sets the student variable list to an empty list which will be used later
    students = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        total_students = int(next(reader)[0])  # First line is the number of students converted to an interger. Tells the number of students in file.
        for row in reader:
            student_id = int(row[0]) # Extracts student ID from the first row
            # Extracts student name in the second row
            name = row[1]
            # Extracts course marks from columns 3-5 and converts it to integers and stores them in a list
            course_marks = list(map(int, row[2:5]))
            # Extracts the final 6th row and converts it into integer
            exam_mark = int(row[5])
            # All variables are then appended into the students list
            students.append({"id": student_id, "name": name, "course_marks": course_marks, "exam_mark": exam_mark})
    return total_students, students

# Calculate total coursework, overall percentage, and grade
# This function takes the course marks and exam mark to call inside the function
def calculate_total_and_grade(course_marks, exam_mark):
    # this gets the total values of the course marks
    total_coursework = sum(course_marks)
    # total marks adds up the total course work and exam mark
    total_marks = total_coursework + exam_mark
    # This then calculates the marks percentage and grades accordingly
    percentage = (total_marks / 160) * 100
    if percentage >= 70:
        grade = 'A'
    elif percentage >= 60:
        grade = 'B'
    elif percentage >= 50:
        grade = 'C'
    elif percentage >= 40:
        grade = 'D'
    else:
        grade = 'F'
    return total_coursework, percentage, grade

# Display all student records
def view_all_records(students):
    total_percentage = 0
    for student in students:
        total_coursework, percentage, grade = calculate_total_and_grade(student["course_marks"], student["exam_mark"])
        total_percentage += percentage
        print(f"\nName: {student['name']} \nID: {student['id']} \nCoursework: {total_coursework} \nExam: {student['exam_mark']}, "
              f"\nPercentage: {percentage:.2f}%, \nGrade: {grade}")
    avg_percentage = total_percentage / len(students)
    print(f"\nTotal students: {len(students)}, Average Percentage: {avg_percentage:.2f}%")

# View a specific student's record
def view_individual_record(students):
    search_id = int(input("\nEnter student ID: "))
    student = next((s for s in students if s['id'] == search_id), None)
    if student:
        total_coursework, percentage, grade = calculate_total_and_grade(student["course_marks"], student["exam_mark"])
        print(f"\nName: {student['name']} \nID: {student['id']} \nCoursework: {total_coursework} \nExam: {student['exam_mark']} "
              f"\nPercentage: {percentage:.2f}% \nGrade: {grade}")
    else:                                              
        print(" _____ _____ __ __ ____  _____ _____ _____    _____ _____ _____    _____ _____ __ __ _____ ____  ")
        print("|   __|_   _|  |  |    \|   __|   | |_   _|  |   | |     |_   _|  |   __|     |  |  |   | |    \ ")
        print("|__   | | | |  |  |  |  |   __| | | | | |    | | | |  |  | | |    |   __|  |  |  |  | | | |  |  |")
        print("|_____| |_| |_____|____/|_____|_|___| |_|    |_|___|_____| |_|    |__|  |_____|_____|_|___|____/ ")

# Show student with the highest score
def show_highest_score(students):
    highest_student = max(students, key=lambda s: sum(s["course_marks"]) + s["exam_mark"])
    total_coursework, percentage, grade = calculate_total_and_grade(highest_student["course_marks"], highest_student["exam_mark"])
    print(f"\nHighest Scoring Student:\nName: {highest_student['name']} \nID: {highest_student['id']} "
          f"\nCoursework: {total_coursework} \nExam: {highest_student['exam_mark']} \nPercentage: {percentage:.2f}% \nGrade: {grade}")

# Show student with the lowest score
def show_lowest_score(students):
    lowest_student = min(students, key=lambda s: sum(s["course_marks"]) + s["exam_mark"])
    total_coursework, percentage, grade = calculate_total_and_grade(lowest_student["course_marks"], lowest_student["exam_mark"])
    print(f"\nLowest Scoring Student:\nName: {lowest_student['name']} \nID: {lowest_student['id']} "
          f"\nCoursework: {total_coursework} \nExam: {lowest_student['exam_mark']} \nPercentage: {percentage:.2f}% \nGrade: {grade}")

# Main program loop
def main():                                                                                          
    print(" _____ _____ __ __ ____  _____ _____ _____    ____  _____ _____ _____ _____ _____ _____ _____ ")
    print("|   __|_   _|  |  |    \|   __|   | |_   _|  |    \|  _  |_   _|  _  | __  |  _  |   __|   __|")
    print("|__   | | | |  |  |  |  |   __| | | | | |    |  |  |     | | | |     | __ -|     |__   |   __|")
    print("|_____| |_| |_____|____/|_____|_|___| |_|    |____/|__|__| |_| |__|__|_____|__|__|_____|_____|")
    filename = "A1 - Skills Portfolio/03 - Student Manager/studentMarks.txt"
    total_students, students = load_student_data(filename)

    while True:
        print("\nMenu:")
        print("1. View all student records")
        print("2. View individual student record")
        print("3. Show student with highest total score")
        print("4. Show student with lowest total score")
        print("5. Quit")
        
        choice = input("\nSelect an option (1-5): ")

        if choice == '1':
            view_all_records(students)
        elif choice == '2':
            view_individual_record(students)
        elif choice == '3':
            show_highest_score(students)
        elif choice == '4':
            show_lowest_score(students)
        elif choice == '5':    
            print(" _____ __ __ _____ ")
            print("| __ -|_   _|   __|")
            print("| __ -|_   _|   __|")
            print("|_____| |_| |_____|")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
