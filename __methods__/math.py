class Calc:
    def __init__(self, age):

        self.age = age
        if self.age > 100:
            raise ValueError("Age cannot be greater than 100")

    def __add__(self, other):
        if not isinstance(other, int):
            raise TypeError("Please enter an integer")
        return self.age + other

    def __sub__(self, other):
        if not isinstance(other, int):
            raise TypeError("Please enter an integer")
        return self.age - other

    def __mul__(self, other):
        if not isinstance(other, int):
            raise TypeError("Please enter an integer")
        return self.age * other

    def __truediv__(self, other):
        if not isinstance(other, int):
            raise TypeError("Please enter an integer")
        elif other == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return int(self.age // other)


a = Calc(25)
b = Calc(24)

print(a + 5)
print(a - 5)
print(a * 5)
print(a / 0)