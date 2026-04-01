##Write a Python program to demonstrate string slicing. 


# Define a sample string
text = "Python Programming"

# 1. Slice from the start to index 5 (exclusive)
print(f"First 6 characters: '{text[:6]}'")

# 2. Slice from index 7 to the end
print(f"From 7th position to end: '{text[7:]}'")

# 3. Slice a middle section (indices 2 to 5)
print(f"Indices 2 to 5: '{text[2:5]}'")

# 4. Slice using a step (every 2nd character)
print(f"Every 2nd character: '{text[::2]}'")

# 5. Reverse the string using slicing
print(f"Reversed string: '{text[::-1]}'")



## Write a Python program that manipulates and prints strings using various string methods. 

# Define a sample string with extra spaces
text = "  python programming is fun!  "

# 1. strip() - Removes leading and trailing whitespace
clean_text = text.strip()
print(f"Stripped: '{clean_text}'")

# 2. upper() and lower() - Changes case
print(f"Uppercase: {clean_text.upper()}")
print(f"Lowercase: {clean_text.lower()}")

# 3. title() - Capitalizes the first letter of each word
print(f"Title Case: {clean_text.title()}")

# 4. replace() - Replaces a substring with another
new_text = clean_text.replace("fun", "awesome")
print(f"Replaced: {new_text}")

# 5. split() - Splits the string into a list of words
words = clean_text.split()
print(f"Split into list: {words}")

# 6. find() - Returns the index of the first occurrence of a substring
index = clean_text.find("programming")
print(f"Index of 'programming': {index}")

