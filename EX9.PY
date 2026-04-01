#Practical Example 8: Write a Python program to check if a person is eligible to donate blood using a nested if.  

# Practical Example 8: Check blood donation eligibility using nested if

def check_eligibility(age, weight_lbs):
    """
    Checks blood donation eligibility using a nested if structure.
    Minimum age for donation is generally 16-18, minimum weight is 110 lbs.
    """
    MIN_AGE = 16
    MIN_WEIGHT_LBS = 110

    print(f"Checking eligibility for Age: {age}, Weight: {weight_lbs} lbs")

    if age >= MIN_AGE:
        # Outer if condition met: Age is sufficient
        if weight_lbs >= MIN_WEIGHT_LBS:
            # Nested if condition met: Weight is also sufficient
            print("Status: Eligible to donate blood.")
        else:
            # Nested else condition
            print(f"Status: Ineligible. Must weigh at least {MIN_WEIGHT_LBS} lbs.")
    else:
        # Outer else condition
        print(f"Status: Ineligible. Must be at least {MIN_AGE} years old.")

# --- Example Usage ---

# Example 1: Eligible candidate
check_eligibility(age=25, weight_lbs=150)
print("-" * 20)

# Example 2: Ineligible due to age
check_eligibility(age=15, weight_lbs=120)
print("-" * 20)

# Example 3: Ineligible due to weight
check_eligibility(age=30, weight_lbs=100)
print("-" * 20)
# Example 4: Ineligible due to both age and weight
check_eligibility(age=15, weight_lbs=100)   
