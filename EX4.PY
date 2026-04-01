#Write a Python program to demonstrate the creation of variables and different data types. 

# Program to demonstrate variable creation and different data types in Python

# 1. Numeric Data Types (int, float, complex)
# Integers (whole numbers)
student_age = 20
print(f"Variable 'student_age': Value = {student_age}, Type = {type(student_age)}")

# Floating-point numbers (numbers with decimals)
height_meters = 1.75
print(f"Variable 'height_meters': Value = {height_meters}, Type = {type(height_meters)}")

# Complex numbers (real and imaginary parts)
complex_number = 1 + 2j
print(f"Variable 'complex_number': Value = {complex_number}, Type = {type(complex_number)}")

print("-" * 30)

# 2. String Data Type (str)
# Sequence of characters enclosed in single or double quotes
user_name = "Alice"
print(f"Variable 'user_name': Value = {user_name}, Type = {type(user_name)}")

print("-" * 30)

# 3. Boolean Data Type (bool)
# Represents True or False values
is_student = True
print(f"Variable 'is_student': Value = {is_student}, Type = {type(is_student)}")

print("-" * 30)

# 4. Sequence Types (list, tuple, range)
# List: Ordered and mutable collection of items
my_list = [10, 20, "Python", True]
print(f"Variable 'my_list': Value = {my_list}, Type = {type(my_list)}")

# Tuple: Ordered and immutable collection of items
my_tuple = (10, 20, 30)
print(f"Variable 'my_tuple': Value = {my_tuple}, Type = {type(my_tuple)}")

print("-" * 30)

# 5. Mapping Type (dict)
# Dictionary: Collection of key-value pairs
person_info = {"name": "John", "age": 25, "city": "New York"}
print(f"Variable 'person_info': Value = {person_info}, Type = {type(person_info)}")

print("-" * 30)

# 6. Set Types (set)
# Set: Unordered collection of unique items
unique_numbers = {1, 2, 3, 3, 4} # Duplicate 3 is automatically removed
print(f"Variable 'unique_numbers': Value = {unique_numbers}, Type = {type(unique_numbers)}")

print("-" * 30)

# Demonstration of dynamic typing (variable type can change)
dynamic_var = 10
print(f"Variable 'dynamic_var' initially: Value = {dynamic_var}, Type = {type(dynamic_var)}")

dynamic_var = "Now I am a string"
print(f"Variable 'dynamic_var' after re-assignment: Value = {dynamic_var}, Type = {type(dynamic_var)}")
