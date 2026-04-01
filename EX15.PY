# Write a Python program that uses a custom iterator to iterate over a list of integers

class CustomIterator:
    """
    A custom iterator that iterates over a list of integers.
    """
    def __init__(self, data):
        self.data = data
        # Initialize an index to keep track of the current position
        self.index = 0

    def __iter__(self):
        # Returns the iterator object itself
        return self

    def __next__(self):
        """
        Returns the next item in the sequence.
        Raises StopIteration when the end of the data is reached.
        """
        if self.index >= len(self.data):
            raise StopIteration
        # Get the current item and advance the index
        item = self.data[self.index]
        self.index += 1
        return item

# --- Example Usage ---
# The list of integers to iterate over
my_list = [10, 20, 30, 40, 50]

# Create an instance of our custom iterator
custom_iter = CustomIterator(my_list)

print("Iterating using a for loop:")
# The 'for' loop automatically calls __iter__() and __next__()
for number in custom_iter:
    print(number)

print("\nIterating manually using next():")
# Demonstrating manual iteration (what 'for' loop does internally)
manual_iter = CustomIterator(my_list)
print(next(manual_iter))
print(next(manual_iter))
print(next(manual_iter))
# ... and so on until StopIteration is raised
