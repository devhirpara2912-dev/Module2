# Practical Example 2: Write a Python program to find the length of each string in List1

List1 = ["apple", "banana", "cherry", "date"]
lengths = []

for string in List1:
    length = len(string) # Get the length of the current string
    lengths.append(length) # Add the length to the new list

print(f"Original list: {List1}")
print(f"Lengths of each string: {lengths}")


List1 = ["Sharpener", "book", "notepad", "pencil"]

# Create a new list containing the length of each string
lengths = [len(string) for string in List1]

print(f"Original list: {List1}")
print(f"Lengths of each string: {lengths}")
