# Practical Example 7: Write a Python program to calculate grades based on percentage using if-else ladder. 

# Function to calculate the grade based on percentage
def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"

# Main part of the program
try:
    # Prompt user for input and convert it to a float
    marks = float(input("Please enter the student's percentage (0-100): "))

    # Validate input to be within a realistic range
    if 0 <= marks <= 100:
        # Get the grade using the function
        grade = calculate_grade(marks)
        print(f"A percentage of {marks}% gets a grade: {grade}")
    else:
        print("Invalid input. Please enter a value between 0 and 100.")

except ValueError:
    # Handle non-numeric input errors
    print("Invalid input. Please enter a numerical value.")
