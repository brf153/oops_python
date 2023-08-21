class Mercedes:
    doors = 4
    windows = 4
    model = "G"

    def drive(self):
        return f"hello i am {self}\n"
    
    def __init__(self, color):
        self.color = color

    def auto_drive():
        return f"I am driving"

m1 = Mercedes("pink")

# Note that m1.auto_drive() will return an error because auto_drive is an instance method and while calling instance methods, self is passed by default in m1.auto_drive(). So, it is necessary to define auto_drive as `def auto_drive(self)` such that it does not show any error

"""
self is always the first argument passed to instance methods. It represents the instance object bound to the method. It is called self only by convention, albeit a very good convention and self is neither a reserved keyword nor does it have any special meaning in Python.
"""