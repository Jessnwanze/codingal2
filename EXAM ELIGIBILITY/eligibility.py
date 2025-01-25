def check_exam_eligibility():
    # Input: Age, attendance, and completion of prerequisites
    print("Welcome to the Exam Eligibility Checker!")

    # Get the user's age
    age = int(input("Enter your age: "))
    
    # Get the user's attendance percentage
    attendance = float(input("Enter your attendance percentage: "))
    
    # Get the status of prerequisite subjects or coursework completion
    prerequisites_completed = input("Have you completed the required prerequisites? (yes/no): ").strip().lower()

    # Eligibility criteria
    min_age = 18
    min_attendance = 75
    required_prerequisites = 'yes'

    # Check eligibility based on the conditions
    if age >= min_age and attendance >= min_attendance and prerequisites_completed == required_prerequisites:
        print("Congratulations! You are eligible to appear for the exam.")
    else:
        print("Sorry, you are not eligible to appear for the exam.")
        
        if age < min_age:
            print("You must be at least 18 years old.")
        if attendance < min_attendance:
            print("You need at least 75% attendance.")
        if prerequisites_completed != required_prerequisites:
            print("You must complete the required prerequisites.")

# Run the eligibility checker
check_exam_eligibility()
