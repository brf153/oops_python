# we make a class first
class Mercedes:
    car= 2
    wheel= 2

# now we can use it as 
Mercedes.__dict__
# this is called dunder dict 

# we can again add something to the class 
Mercedes.windows = 2
# now we will get car wheel and windows in the dunder dict.

# in order to show the dunder dict
print(Mercedes.__dict__)

# now we can create instances of it
m1 = Mercedes()
m2 = Mercedes()

# To recap, we traditionally define class state in the class body, but we could certainly also redefine or add outside of the class definition. Class state is stored in a special mapping object of type mapping proxy and that is retrievable Using dunder dict and class. State is shared and accessible by all instances of that class.
