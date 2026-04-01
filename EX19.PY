##   Practical Example: 1) Write a Python program to skip 'banana' in a list using the continue statement. List1 = ['apple', 'banana', 'mango'] 


# Define the list
List1 = ['apple', 'banana', 'mango']

# Loop through the list and skip 'banana'
for fruit in List1:
    if fruit == 'banana':
        continue
    print(fruit)


##Practical Example: 2) Write a Python program to stop the loop once 'banana' is found using the break statement.   

# Define the list
List1 = ['apple', 'banana', 'mango']

# Loop through the list and stop once 'banana' is found
for fruit in List1:
    if fruit == 'banana':
        break
    print(fruit)
