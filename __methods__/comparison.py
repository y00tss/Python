class Calc:
    def __init__(self, age):

        self.age = age
        if self.age > 100:
            raise ValueError("Age cannot be greater than 100")

    def __eq__(self, other):
        if not isinstance(other, (int, Calc)):
            raise TypeError("Can only compare with int or Calc")
        return self.age == other

    def __ne__(self, other):
        if not isinstance(other, (int, Calc)):
            raise TypeError("Can only compare with int or Calc")
        return self.age != other

    def __lt__(self, other):
        if not isinstance(other, (int, Calc)):
            raise TypeError("Can only compare with int or Calc")
        return self.age < other

    def __gt__(self, other):
        if not isinstance(other, (int, Calc)):
            raise TypeError("Can only compare with int or Calc")
        return self.age > other


a = Calc(25)
b = Calc(20)

print(a == b)
print(a != b)
print(a < b)
print(a > b)
