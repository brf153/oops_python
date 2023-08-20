class Mercedes:
    doors = 4
    windows = 4
    model = "G"
# right now we only have state no behaviour or action

# now we can create a definition like
    def drive():
        return "I am driving"
    
# in classes the definitions are a bit different
class Mercedes:
    doors = 4
    windows = 4
    model = "G"

    def handleDrive(self):
        return self
# note that by convention the first parameter will be self which is Mercedes. note that the self is an instance. 

"""
In Python, an instance refers to a specific object created from a class. When you create an object from a class, you're creating an instance of that class. Each instance can have its own unique data (attributes) and can perform actions (methods) defined in the class. Instances allow you to work with and manipulate data in an object-oriented manner.
"""

m1 = Mercedes()
print(m1.handleDrive())
print(m1.handleDrive()==m1)
print(m1.handleDrive() is m1)

# note that m1 is not equal to Mercedes because Mercedes is a class and m1 in an instance

# now when you create multiple instances, the instances will return different self because self was an instance
class Mercedes:
    doors = 4
    windows = 4
    model = "G"

    def drive(self):
        return f"I am driving a Mercedes which is {self}\n"  

m1 = Mercedes()
m2 = Mercedes()

print(m1.drive())
print(m2.drive())

# note that it would print something like <__main__.Mercedes object at 0x7feb77dc7970> and <__main__.Mercedes object at 0x7feb78069e80> in the end where 0x7feb78069e80 and 0x7feb77dc7970 are memory addresses where the object (also called instance) is stored in memory.

"""
We add behavior to our classes by defining functions. This functions are special in that they always have at least one parameter called self. By convention, that parameter is called self, and it represents the instance when functions are defined within the body of the class, they become bound or attached to instances of that class and correspondingly their name changes. They're then called methods.
"""