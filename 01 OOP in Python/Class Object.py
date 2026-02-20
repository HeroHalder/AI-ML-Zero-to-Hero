class Student:
    def __init__(self, name,id):
        self.name=name
        self.id=id

    def __repr__(self):
        return f"Student(name='{self.name}', id={self.id})"
    def view(self):
        print(f"Student name: {self.name}, Student ID: {self.id}")


#===========================================================================================================

s1=Student("Hero",242)
h1=Hero("Hero",24)
h1.department()
print(h1.__dict__)




