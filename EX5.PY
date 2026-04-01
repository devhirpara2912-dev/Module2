 # Practical Example 1: How does the Python code structure work? 

Modules: A Python program is typically organized into one or more files with a .py extension. Each file is called a module, which can contain functions, classes, and variables.
Indentation: Python uses indentation (four spaces are recommended by PEP 8) to define code blocks, such as those within functions, classes, loops, and conditional statements (if/else).
Statements: The basic units of instruction are statements, which the interpreter executes sequentially. Examples include assignments (a = 1), function calls (print(a)), and control flow statements (for loops).
Functions and Classes:
Functions are blocks of reusable code that perform a specific task and help break down problems into manageable parts.
Classes are blueprints for creating objects, grouping related data (attributes) and behavior (methods) together, which is the basis of object-oriented programming in Python. 


#Practical Example 2: How to create variables in Python? 

# 1. Integer variable (whole number)
user_age = 25

# 2. String variable (text enclosed in quotes)
user_name = "Ada Lovelace"

# 3. Float variable (decimal number)
tax_rate = 0.05

# 4. Boolean variable (True or False)
is_active = True

# 5. List variable (an ordered collection of items)
fruits = ["apple", "banana", "cherry"]

# 6. Dictionary variable (unordered collection of key-value pairs)
student_info = {"name": "Rohit", "age": 36}

# You can also perform calculations and assign the result to a new variable
total_cost = 1000 * tax_rate + 1000 

# Print the values to verify
print("Name:", user_name)
print("Age:", user_age)
print("Tax Rate:", tax_rate)
print("Is Active:", is_active)
print("Fruits:", fruits)
print("Student Info:", student_info)
print("Total Cost:", total_cost)


#Practical Example 3: How to take user input using the input() function. 

# Prompt the user for their name and store it in a variable
name = input("Enter your name: ") 

# Print a greeting using the input name
print("Hello, " + name + "!")

# Take age as input and convert it to an integer immediately
age = int(input("Enter your age: "))

# Perform a calculation with the numeric input
next_age = age + 1

# Print the result (age is automatically converted back to a string for printing)
print("You will be", next_age, "next year.") 
# Take two numbers separated by a space and store them as a list of strings
num1_str, num2_str = input("Enter two numbers separated by a space: ").split()

# Convert the string inputs to integers
num1 = int(num1_str)
num2 = int(num2_str)

# Calculate and print the sum
sum_of_numbers = num1 + num2
print("The sum of", num1, "and", num2, "is", sum_of_numbers)


#Practical Example 4: How to check the type of a variable dynamically using type()
n = 42 # an integer
f = 3.14 # a float
s = "Hello, World!" # a string
li = [1, 2, 3] # a list
d = {'key': 'value'} # a dictionary
b = True # a boolean

print(type(n))
print(type(f))
print(type(s))
print(type(li))
print(type(d))
print(type(b))

def process_data(data):
    if type(data) == int:
        print("Processing integer:", data * 2)
    elif type(data) == str:
        print("Processing string:", data.upper())
    else:
        print("Unsupported data type")

process_data(10)
process_data("python")
process_data([1, 2, 3])

