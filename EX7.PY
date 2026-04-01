# Practical Example 6: Write a Python program to check if a number is prime using if_else. 

# Function to check if a number is prime
def is_prime(number):
    # Prime numbers must be greater than 1
    if number <= 1:
        return False
    # Check for factors from 2 up to the square root of the number
    # It's more efficient to check up to the square root
    for i in range(2, int(number**0.5) + 1):
        if (number % i) == 0:
            # If a factor is found, it's not a prime number
            return False
    # If no factors are found, it is a prime number
    return True

# --- Main part of the program ---

# Take input from the user
user_input = input("Enter a number to check: ")
num = int(user_input)

# Use if-else conditional statements to print the result
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
