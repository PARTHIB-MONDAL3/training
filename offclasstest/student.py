class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def details(self):
        print("Name:",self.name)
        print("Age:",self.age)

class ug_student(student):
    def __init__(self,name,age,semester,department):
            super().__init__(name,age)
            self.semester=semester
            self.department=department

    def ug_details(self):
            self.details()
            print("Semester:",self.semester)
            print("Department:",self.department)

result=ug_student("Alice",20,4,"Computer Science")
result.ug_details()
result2=student("Bob",22)
result2.details()       
