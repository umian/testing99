class Employee:
    employee_count=0
    def __init__(self,passed_name,passed_number):
        self.name=passed_name
        self.number=passed_number
        Employee.employee_count+=1
        self.employee_count = Employee.employee_count

    def show(self):
        print("name:",self.name)
        print("numner:",self.number)
        print("Employee#:",self.employee_count)
        print("Employee#:",Employee.employee_count)


first=Employee("usman",1234).show()
second=Employee("rebecka",99999).show()

print("total employees", Employee.employee_count)