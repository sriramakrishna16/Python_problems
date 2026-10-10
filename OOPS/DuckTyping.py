class PDF:
    def open(self):
        print("PDF opening")

class Image:
    def open(self):
        print("Image opening")

def open_file(file):
    file.open()
p = PDF()
open_file(p)


# operator overloading

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __add__(self, other):
        return self.marks + other.marks


s1 = Student("Ram", 85)
s2 = Student("Ravi", 90)

print(s1 + s2)


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks


s1 = Student("Ram", 85)
s2 = Student("Ravi", 90)

print(s1 > s2)
print(s2 > s1)


class Parent:
    def __init__(self):
        self.public = 10
        self._protected = 20
        self.__private = 30

    def show(self):
        print(self.public)
        print(self._protected)
        print(self.__private)


class Child(Parent):
    def display(self):
        print(self.public)
        print(self._protected)
        # print(self.__private)  # AttributeError


p = Parent()
c = Child()

p.show()
c.display()

print(p._protected)  # Works, but convention says avoid this
