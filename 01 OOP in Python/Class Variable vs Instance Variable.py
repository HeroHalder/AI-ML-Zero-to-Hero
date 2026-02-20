class Student:
    university = "GUB"   # class variable

    def __init__(self, name):
        self.name = name  # instance variable

s1 = Student("Hero")

print(s1.university)
print(s1.name)
