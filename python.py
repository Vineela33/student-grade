def calculate_gpa(average_grade):
    """Calculate GPA based on the average grade."""
    return min(max(0, (average_grade - 60) // 10), 4.0)

def get_letter_grade(average_grade):
    """Determine the letter grade based on the average grade."""
    if average_grade >= 90:
        return 'A'
    if average_grade >= 80:
        return 'B'
    if average_grade >= 70:
        return 'C'
    if average_grade >= 60:
        return 'D'
    return 'F'

def main():
    grades = []
    subjects = []
    print("Welcome to the Student Grade Management System")
    
    while True:
        subject = input("Enter the subject name (or type 'done' to finish): ").strip()
        if subject.lower() == 'done':
            break
        try:
            grade = float(input(f"Enter the grade for {subject}: "))
            if 0 <= grade <= 100:
                subjects.append(subject)
                grades.append(grade)
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric grade.")

    if not grades:
        print("No grades entered. Exiting program.")
        return

    average_grade = sum(grades) / len(grades)
    letter_grade = get_letter_grade(average_grade)
    gpa = calculate_gpa(average_grade)

    print("\n--- Grade Report ---")
    for subject, grade in zip(subjects, grades):
        print(f"Subject: {subject}, Grade: {grade:.2f}")
    
    print(f"\nAverage Grade: {average_grade:.2f}")
    print(f"Letter Grade: {letter_grade}")
    print(f"GPA: {gpa:.2f}")

if __name__ == "__main__":
    main()
