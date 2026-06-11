import csv
def load_students(filepath):
    data_student = []
    try:
        with open(filepath, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data_student.append(row)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return[]
    return data_student
            #data_student.append(row)
data_student = load_students("data/students.csv")            
print(f"loaded {len(data_student)} students records...\n")  
print(f"Generating report.... \n")

#print("data/students.csv")

#      


def calculate_average(grades):
    
    valid_grades = []

    for grade in grades:
        if grade not in ("", None):
            try:
                valid_grades.append(float(grade))
            except ValueError:
                continue

    if not valid_grades:
        return None

    average = sum(valid_grades) / len(valid_grades)
    return round(average, 1)

def get_letter_grade(average):
    if average is None:
        return 'N/A'
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F' 
    
#print(get_letter_grade(0))


#get_letter_grade(90)

    


def generate_report(students):
    student_results = []
    all_averages = []
    grade_distribution ={
         
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0,
        'F': 0,
        'N/A': 0
    }
    for student in students:
        grades = [
              student["math"],
              student["science"],
              student["english"],
              student["history"]
        #print(student_results)

        ]
    


        average = calculate_average(grades)
        letter_grade = get_letter_grade(average)

    

        if average is not None:
            all_averages.append(average)

        grade_distribution[letter_grade] += 1
    
        student_results.append({
        "student_name": student["student_name"],
        "average": average,
        "letter_grade": letter_grade

    })
    if all_averages:

        class_average = sum(all_averages) / len (all_averages) 
        highest_average = max(all_averages)
        lowest_average = min(all_averages)
    
    else:
        class_average = None
        highest_average = None
        lowest_average = None

    return {
        
    "total_students": len(students),
    "class_average": class_average,
    "highest_average": highest_average,
    "lowest_average": lowest_average,
     "grade_distribution": grade_distribution,
    "student_results": student_results
        
    }
    
    #return report
#generate_report("student_results")
         

def write_report(report, filepath):
    try:
        with open(filepath, mode='w', newline='') as file:
            
            file.write( "=" * 40 + "\n")
            file.write(f"Generating report.... \n")
            file.write("---- Summary ---- \n")
            file.write(f"Total Students: {report['total_students']}\n")
            file.write(f"Class Average: {report['class_average']:.2f}\n")
            file.write(f"Highest Average: {report['highest_average']:.2f}\n")
            file.write(f"Lowest Average: {report['lowest_average']:.2f}\n")
            #file.write("-" * 40 + "\n")
            file.write("-" * 40 + "\n")
            file.write("Grade Distribution:\n")
            #file.write("-" * 40 + "\n")

        
            #file.write("Grade_distribution\n")

        #for grade, count in report["grade_distribution"].items():
            #file.write(f"Grade: {grade}, Count: {len(count)}\n")
            for grade, count in report["grade_distribution"].items():
                    file.write(f"Grade: {grade} = {count}\n")
                    #file.write("\n")

            file.write("-" * 40 + "\n")
            file.write("Top 5 Students:\n")
            #file.write("-" * 40 + "\n")
            top_students = sorted(
                report["student_results"], 
                key=lambda x: x["average"] if x["average"] is not None else 0, reverse=True
            )[:5]

            
            for i, student in enumerate(top_students, start=1):
                print(f"{i}. {student['student_name']}: {student['average']} ({student['letter_grade']})")
                file.write(f"{i}. {student['student_name']}: {student['average']} ({student['letter_grade']})\n")


            file.write("-" * 40 + "\n")
            file.write("\nIndividual Student Results:\n")
            #file.write("-" * 40 + "\n")
            for student in report["student_results"]:
                average =(
                 
                    student["average"] 
                    if student["average"] is not None 
                    else "N/A"
                )
                file.write(f"Student Name: {student['student_name']}\n")
                file.write(f"Average Score: {average}\n")
                file.write(f"Letter Grade: {student['letter_grade']}\n")
                file.write("-" * 40 + "\n")
            print("Report written to grade_report.txt")                
    except Exception as e:
        print(f"Error writing report to '{filepath}': {e}")

                   
#
# print(write_report)


students = load_students("data/students.csv")
#report = generate_report(students)
#write_report("report", "grade_report.txt")


def main():

    input_file = "data/students.csv"

    output_file = "grade_report.txt"

    students = load_students(input_file)

    if len(students) == 0:
        print("No student data available.")
        return

    report = generate_report(students)


    write_report(report, output_file)

students = load_students("data/students.csv")
report = generate_report(students)
#---------- Summary ----------
print("---------- Summary ----------")
print(f"Total Students: {report['total_students']}")
print(f"class average: {report['class_average']:.2f}")
print(f"highest average: {report['highest_average']}")
print(f"lowest average: {report['lowest_average']}")

print("\nGrade Distribution")
for grade, count in report["grade_distribution"].items():
    print(f"  {grade} = {count}")



print("\nTop 5 Students")
print("-" * 40)
top_students = []
for i, student in enumerate(top_students, start=1):
                print(
                    f"{i}. {student['student_name']} "
        f"({student['average']:.1f}) - {student['letter_grade']}"
    )
                    
                
           
if __name__ == "__main__":
    main()




        
 
        