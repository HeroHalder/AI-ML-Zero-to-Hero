marks = {"Hero": 80, "Amit": 45, "Ramu": 60, "Nila": 30}
new_marks={}
for name, mark in marks.items():
    if mark>=50:
        new_marks[name]=mark
print(new_marks)
