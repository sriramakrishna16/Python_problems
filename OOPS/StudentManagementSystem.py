class Student:
    def __init__(self, id, name, marks):
        self.id = id
        self.name = name
        self.marks = marks

    def totalMarks(self):
        return sum(self.marks)

    def avgMarks(self):
        return sum(self.marks)/ len(self.marks)

    def calculateGrade(self):
        avg = sum(self.marks)/len(self.marks)

        if avg >= 90:
            return 'A'
        elif avg >= 80 and avg < 90:
            return 'B'
        elif avg >= 70 and avg < 80:
            return 'C'
        elif avg >= 60 and avg < 70:
            return 'D'
        else:
            return 'Fail'

    def display_details(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Total: {self.totalMarks()}")
        print(f"Average: {self.avgMarks():.2f}")
        print(f"Grade: {self.calculateGrade()}")

s1 = Student(101,"RK", [90,80,70])
s2 = Student(102, "Krunal", [90,50,70])
s1.display_details()

    

    