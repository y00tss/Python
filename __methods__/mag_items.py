class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError('Index out of range')

    def __setitem__(self, key, value):
        self.marks[key] = value

    def __delitem__(self, key):
        del self.marks[key]



s1 = Student('Shepel', [5, 4, 5, 3, 5])
print(s1.marks) # выводим все оценки
print(s1[0])    # выводим под индексом 0
s1[0] = 3       # меняем первый элемент
print(s1.marks) # выводим результат
del s1[0]       # удаляем первый элемент
print(s1.marks) # выводим результат
