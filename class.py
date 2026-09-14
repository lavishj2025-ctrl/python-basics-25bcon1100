class Student:
    def __init__(self):
        self.rollno = 0
        self.name = ""
        self.marks = 0.0

s = Student()
s.rollno = int(input("Enter the roll no. :"))
s.name = input("Enter the name :")
s.marks = float(input("Enter the marks :"))

print(f"Roll Number : {s.rollno}")
print(f"Name : {s.name}")
print(f"Marks : {s.marks:.6f}")
