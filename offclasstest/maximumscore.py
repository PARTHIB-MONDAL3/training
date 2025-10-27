'''Write a program to collect all the students information and find who 
is score maximum '''

s=input("Enter the student details ")
student=[]
choice=1
while choice!=-1:
    name=input("Enter the name ")
    Score=int(input("Enter the score "))
    student.append((name,Score))
    choice=int(input("Enter -1 to exit, any other to continue"))

topper=max(student,key=lambda x:x[1])
print("Topper name",topper[0])
print("Topper score",topper[1])