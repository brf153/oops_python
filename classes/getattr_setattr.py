class Mercedes:
    windows = 4
    doors = 4
    model = "G"

    def __init__(self, color):
        self.color = color

    def drive(self):
        return f"Hello I am {self}\n"

m1 = Mercedes("black")
m2 = Mercedes("blue")

# using getattr function we can get the attribute of an instance. 
print(getattr(m1, "color"))
# it is equal to m1.color

# using setattr function we can set the attribute of an instance
setattr(m1, "color", "red")
print(m1.color)
# it is equal to m1.color = "red"

# note that setattr and getattr are used when there are many instances that needs to be manipulated at the same time
objs = [m1, m2]

attribs = ["color", "doors"]
values = ["navy", 3]

for obj in objs:
    for attrib, val in zip(attribs,values):
        setattr(obj, attrib, val)

print(m1.color, m2.color)

# In getattr you can also send an optional error message if the attribute is not found like getattr(m1,"wingspan","Attribute not found")

"""
In addition to the traditional dot access, syntax attributes could also be read and set using getattr and setattr built in methods. These methods are most useful if we're manipulating objects programmatically, and especially if we're doing so at scale for, you know, a really large number of them.
""" 

# Note
"""
In Python, the zip function is used to combine multiple iterables (such as lists, tuples, or other sequences) into a single iterable. It aggregates elements from each input iterable into tuples, where the first element in each passed iterable is paired together, the second element in each iterable is paired together, and so on.

The resulting iterable produced by zip is often used in scenarios where you want to process corresponding elements from multiple sequences in parallel.

Here's an example of how the zip function works:

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 28]
countries = ["USA", "Canada", "Australia"]

# Using zip to combine multiple lists
combined = zip(names, ages, countries)

# Converting the zip object to a list of tuples
combined_list = list(combined)

print(combined_list)

Output :
[('Alice', 25, 'USA'), ('Bob', 30, 'Canada'), ('Charlie', 28, 'Australia')]
"""


# Note
"""
In Python, a tuple is an ordered, immutable collection of elements. Tuples are similar to lists, but with a key difference: once you create a tuple, you cannot modify its elements or size. Tuples are defined using parentheses () and can contain elements of different data types, including other tuples.

# Creating a tuple
my_tuple = (1, 2, 3, "apple", "banana")

# Accessing elements of a tuple
print(my_tuple[0])       # Output: 1
print(my_tuple[3])       # Output: apple

# Tuples can contain elements of different data types
mixed_tuple = (4, "orange", 2.5, True)

# Nested tuples
nested_tuple = ((1, 2), ("a", "b"), (True, False))

# Unpacking a tuple
a, b, c, d, e = my_tuple
print(a, b, c)           # Output: 1 2 3

"""


# Note 
"""
Arrays and lists are both used to store collections of elements in programming, but they have some differences in how they are implemented and used. In Python, the term "list" is used to refer to a data structure that can hold an ordered collection of items. The term "array" is often used in the context of other programming languages like C, C++, and Java, where arrays have certain characteristics that differ from Python lists.

Here are the main differences between arrays and lists:

Memory Allocation:

Arrays in languages like C and Java are fixed in size and require contiguous memory allocation. They have a predetermined size that doesn't change during runtime.
Lists in Python are dynamic in size and don't require contiguous memory allocation. They can grow or shrink as needed.

Data Types:
In some programming languages, arrays are homogeneous collections, meaning they can only hold elements of the same data type.
Python lists can hold elements of different data types (heterogeneous) without any restriction.

Operations:
Arrays in languages like C and Java have a fixed set of operations available, often limited to basic indexing and iteration.
Python lists provide a wide range of built-in methods and operations beyond basic indexing, including appending, removing, slicing, sorting, and more.

Flexibility:
Lists in Python are more flexible and convenient for general-purpose programming due to their dynamic nature and rich feature set.
Arrays in other languages can be more efficient for specific operations when memory layout and fixed sizes are important.

Library Usage:
If you're working with numerical data, you might use specialized libraries like NumPy in Python, which provides arrays that offer better performance for numerical computations compared to native Python lists.

In Python, you often use the term "list" to refer to collections of items, regardless of the differences that exist in other languages. Python's list is a versatile and widely used data structure that can hold various types of elements and offers a range of built-in functions for manipulation. If you need more specialized behavior or better performance for numerical computations, you might consider using libraries like NumPy, which provide array-like structures optimized for such tasks.
"""