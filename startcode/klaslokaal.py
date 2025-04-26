from student import *

class Klaslokaal:
    def __init__(self):
        self.studenten = []

    def voeg_student_toe(self, student):
        self.studenten.append(student)

    def toon_studenten(self):
        for student in self.studenten:
            student.stel_voor()

student1 = Student('Floor Mat', '18')
student2 = Student('Ron De Bril', '17')

klaslokaal1A = Klaslokaal()
klaslokaal1A.voeg_student_toe(student1)
klaslokaal1A.voeg_student_toe(student2)
klaslokaal1A.toon_studenten()
