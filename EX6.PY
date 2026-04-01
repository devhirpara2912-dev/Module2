# Practical Example 5: Write a Python program to find greater and less than a number using if_else. 

# Practical Example 5: Python program to find greater and less than a number using if-else

# 1. Prompt the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# 2. Use if-elif-else statements to compare the numbers
if num1 > num2:
    # This block executes if the first number is greater than the second
    print(f"Result: {num1} is greater than {num2}")
elif num2 > num1:
    # This block executes if the second number is greater than the first
    print(f"Result: {num2} is greater than {num1}")
else:
    # This block executes if neither of the above conditions is true (i.e., they are equal)
    print(f"Result: {num1} is equal to {num2}")

