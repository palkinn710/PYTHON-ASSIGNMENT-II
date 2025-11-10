# =========================================================
# Project: GradeBook Analyzer
# Author: Palkin Jain
# Roll No: 2501410045
# =========================================================

import csv

def calculate_average(marks_dict):
    #Calculating average marks
    total = sum(marks_dict.values())
    count = len(marks_dict)
    return total / count if count > 0 else 0


def calculate_median(marks_dict):
    #Calculating median marks
    marks = sorted(marks_dict.values())
    n = len(marks)
    if n == 0:
        return 0
    mid = n // 2
    if n % 2 == 0:
        return (marks[mid - 1] + marks[mid]) / 2
    else:
        return marks[mid]


def find_max_score(marks_dict):
#Return the maximum marks.
    return max(marks_dict.values()) if marks_dict else None


def find_min_score(marks_dict):
    #Return the minimum marks.
    return min(marks_dict.values()) if marks_dict else None


#Assigning grades based on marks

def assign_grades(marks_dict):
    """Assign grades based on marks."""
    grades = {}
    for name, marks in marks_dict.items():
        if marks >= 90:
            grade = 'A'
        elif marks >= 80:
            grade = 'B'
        elif marks >= 70:
            grade = 'C'
        elif marks >= 60:
            grade = 'D'
        else:
            grade = 'F'
        grades[name] = grade
    return grades


def grade_distribution(grades_dict):
    """Count number of students per grade."""
    dist = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    for grade in grades_dict.values():
        dist[grade] += 1
    return dist


# ------------------- PASS/FAIL FILTER -------------------

def pass_fail_lists(marks_dict):
    """Separate passed and failed students using list comprehension."""
    passed = [name for name, marks in marks_dict.items() if marks >= 40]
    failed = [name for name, marks in marks_dict.items() if marks < 40]
    return passed, failed


#CSV File Load Function

def load_from_csv(filename):
    # Load student marks from a CSV file
    marks = {}
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row if exists
            for row in reader:
                if len(row) == 2:
                    name = row[0].strip()
                    try:
                        marks[name] = float(row[1])
                    except ValueError:
                        print(f"Invalid mark for {name}. Skipping.")
        if len(marks) == 0:
            print("No valid data found in file.")
        else:
            print(f"\n✅ Loaded {len(marks)} records from '{filename}' successfully.")
    except FileNotFoundError:
        print("❌ File not found. Please check the filename.")
    return marks


#Function to display results in tabular form

def display_table(marks_dict, grades_dict):
    print("\n" + "-" * 50)
    print(f"{'Name':<20}{'Marks':<10}{'Grade':<10}")
    print("-" * 50)
    for name, marks in marks_dict.items():
        print(f"{name:<20}{marks:<10.1f}{grades_dict[name]:<10}")
    print("-" * 50)


# Main function 
def main():
    print("===== GRADEBOOK ANALYZER =====")

    while True:
        print("\n1. Manual Entry")
        print("2. Load from CSV File")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        marks_dict = {}

        if choice == '1':
            n = int(input("\nEnter number of students: "))
            for i in range(n):
                name = input(f"Enter name of student {i + 1}: ")
                marks = float(input(f"Enter marks of {name}: "))
                marks_dict[name] = marks

        elif choice == '2':
            filename = input("\nEnter CSV filename (with .csv extension): ")
            marks_dict = load_from_csv(filename)

        elif choice == '3':
            print("\nExiting GradeBook Analyzer. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")
            continue

        if not marks_dict:
            continue

        # ---- Perform Analysis ----
        avg = calculate_average(marks_dict)
        median = calculate_median(marks_dict)
        highest = find_max_score(marks_dict)
        lowest = find_min_score(marks_dict)
        grades = assign_grades(marks_dict)
        dist = grade_distribution(grades)
        passed, failed = pass_fail_lists(marks_dict)

        # ---- Display Results ----
        display_table(marks_dict, grades)

        print("\n STATISTICAL SUMMARY:")
        print(f"Average Marks: {avg:.2f}")
        print(f"Median Marks: {median:.2f}")
        print(f"Highest Marks: {highest}")
        print(f"Lowest Marks: {lowest}")

        print("\n GRADE DISTRIBUTION:")
        for grade, count in dist.items():
            print(f"{grade}: {count}")

        print("\n PASS/FAIL SUMMARY:")
        print(f"Passed ({len(passed)}): {', '.join(passed) if passed else 'None'}")
        print(f"Failed ({len(failed)}): {', '.join(failed) if failed else 'None'}")


#Staring point of the program

if __name__ == "__main__":
    main()