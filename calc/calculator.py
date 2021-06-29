

class Calculator:
    def __init__(self,a , b):
        self.add(a, b)
        self.subtract(a, b)
        self.divide(a, b)
        self.multiply(a, b)
        self.reverse_divide(a, b)

    def add(self, a, b):
        print("Addition: " + str(a + b))
        return a + b

    def subtract(self, a, b):
        print("Subtraction: " +str(a - b))
        return a - b

    def multiply(self, a, b):
        print("Multiplication: " + str(a * b))
        return b * a

    def divide(self, a, b):
        print("Division: " + str(a / b))
        return a / b

    def reverse_subtract(self, a, b):
        print("Reverse Subtraction: " + str(b - a))
        return b - a

    def reverse_divide(self, a, b):
        return b / a


