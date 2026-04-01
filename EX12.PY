# Practical Example 3: Write a Python program to find a specific string in the list using a simple 

# The list of strings to search through
my_list = ["apple", "banana", "cherry", "date"]

# The specific string to find
search_string = "banana"

# Use the 'in' operator to check for membership
if search_string in my_list:
    print(f"'{search_string}' was found in the list.")
else:
    print(f"'{search_string}' was not found in the list.")

# Example with a string that is not in the list
search_string_two = "grape"

if search_string_two in my_list:
    print(f"'{search_string_two}' was found in the list.")
else:
    print(f"'{search_string_two}' was not found in the list.")
