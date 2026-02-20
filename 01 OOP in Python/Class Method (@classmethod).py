class Student:
    count = 0

    def __init__(self):
        Student.count += 1

    @classmethod
    def total_student(cls):
        print(cls.count)

s1 = Student()
s2 = Student()

Student.total_student()
print(Student.count) #same as above
