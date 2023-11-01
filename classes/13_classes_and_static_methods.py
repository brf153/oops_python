class Mercedes:
    car = 2
    door = 3
    wheels = 4

    def __init__(self, color="black"):
        self.color = color

    def drive(self):
        return f"I am driving {self}\n"

    @staticmethod
    def auto_drive():
        return f"Auto drive for now...."


m1 = Mercedes()
m1.auto_drive()

"""
Python has static and class methods. In class methods, the class is implicitly passed as the first argument, whereas in static methods, neither the instance object nor the class is passed. Static methods are like regular functions that are grouped with the class namespace because they're somehow conceptually related to the class.
"""
