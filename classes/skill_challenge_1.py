#Note 
"""
Instance Attribute:
An instance attribute is a variable that belongs to a specific instance of a class. Each instance can have its own unique values for instance attributes. These attributes are defined within the methods of the class, usually within the __init__ method, which is the constructor method of the class.

***
class MyClass:
    def __init__(self, value):
        self.instance_attr = value

obj1 = MyClass(10)
obj2 = MyClass(20)

print(obj1.instance_attr)  # Output: 10
print(obj2.instance_attr)  # Output: 20
***

In this example, instance_attr is an instance attribute, and each instance of MyClass has its own separate value for it.

Class Attribute:
A class attribute is a variable that belongs to the class itself rather than to any specific instance. It is shared among all instances of the class. Class attributes are defined outside of any methods within the class.

***
class MyClass:
    class_attr = 100

obj1 = MyClass()
obj2 = MyClass()

print(obj1.class_attr)  # Output: 100
print(obj2.class_attr)  # Output: 100
print(MyClass.class_attr)  # Output: 100

obj1.class_attr = 200  # This creates an instance attribute for obj1, not changing the class attribute

print(obj1.class_attr)  # Output: 200 (instance attribute)
print(obj2.class_attr)  # Output: 100 (class attribute)
print(MyClass.class_attr)  # Output: 100 (class attribute)
***

In this example, class_attr is a class attribute shared among all instances of MyClass. When you modify the class attribute using an instance (as shown with obj1.class_attr = 200), it actually creates a new instance attribute for that specific instance, rather than modifying the class attribute.

In summary, the main difference between instance attributes and class attributes lies in their scope and how they are accessed and shared among instances. Instance attributes are unique to each instance, while class attributes are shared among all instances of the class.
"""

import random

greet_list = ["Hi, I am {self.name}", "Hey there, my name is {self.name}", "Hi. Oh, my name is {self.name}"]

class Student:
    educational_institution = "udemy"

    def __init__(self, name, age=16):
        self.name = name
        self.age = age

    def greet(self):
        return random.choice(greet_list).format(self=self)
    

students = ["a", "b", "c", "d"]

for student in students:
    print(Student(student).greet())

    
