#Write a generator function that generates the first 10 even numbers.

def first_ten_even_numbers():
    """
    A generator function that yields the first 10 even numbers (0 through 18).
    """
    count = 0
    num = 0
    while count < 10:
        yield num
        num += 2
        count += 1

# Example usage:
# Create the generator object
even_gen = first_ten_even_numbers()

# Iterate through the generator to get the numbers
for even_num in even_gen:
    print(even_num)
