"""
The proper way to set instance attributes is during the instance initialization itself and Python gives us access to to that step using a special method called init.
"""

class Mercedes:
    window = 4
    door = 4
    model = "G"

    def __init__(self, color):
        self.color = color

    def drive(self):
        return f"Hello I am {self}\n"
    
# note that we can also set a default value to color as def __init__(self, color="black") otherwise anytime we call the Mercedes class we will have to define the color as Mercedes("black") only then we will be able to call the class

m1 = Mercedes("red")
m2 = Mercedes("blue")

"""
So attributes are simply variables associated with objects, just as we associate those variables with certain values and we bind to the class object Mercedes right here. We can also do with instances and instance attributes could be set before or after the instance object is returned, but typically it is a best practice to set them in dunder in it, which is a special method that Python specifically exposes for this purpose.
"""
        