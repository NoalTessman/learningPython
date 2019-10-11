class Employee():
    def __init__(self, first, last, pay):
        self.first = first
        self.pay = pay
        self.last = last
        self.email = first + "." + last + "@Company.com"
    
    def fullName(self):
        print(self.first + " " +self.last)


emp_1 = Employee("Neal","Tessburg",15)

print(emp_1.email)

emp_1.fullName()

Employee.fullName(emp_1)