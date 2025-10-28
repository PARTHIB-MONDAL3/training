'''As a HR manager I want to manage employee details
HR
HR MANAGER
EMPLOYEE

MANAGE'''

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def show_details(self):
        return f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}"
        #print(f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}")


class HRManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def get_employee_details(self, employee_name):
        for emp in self.employees:
            if emp.name == employee_name:
                return emp.show_details()
        return "Employee not found."
    
hr=HRManager()
emp1=Employee("Alice","Developer",70000)
emp2=Employee("Bob","Designer",65000)   
hr.add_employee(emp1)
hr.add_employee(emp2)
print(hr.get_employee_details("Alice"))
print(hr.get_employee_details("Bob"))


