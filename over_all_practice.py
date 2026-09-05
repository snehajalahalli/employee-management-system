class Employee:

    company="ABC Technologies"
    employee_count=0

    def __init__(self,name,salry):
        self.name=name
        self.__salary=salry

        Employee.employee_count+=1

    def display(self):
        print("name:",self.name , "salary:",self.__salary)

    def calculate_salary(self):
        return self.__salary

    def get_salary(self):
        return self.__salary

    def set_salary(self,salary):
        if  salary>0:
            self.__salary=salary
        else:
            print("Salary must be positive")

    @classmethod
    def company_name(cls):
        print("company:",cls.company)

    @staticmethod
    def is_valid_salary(salary):
        return salary>0

    def __str__(self):
        return f"Employee(Name={self.name}, salary={self.__salary})"
    

class Developer(Employee):

    def __init__(self,name,salary,role):
        super().__init__(name,salary)
        self.role=role


    def display(self):
        return super().display()
        print("Role:",self.role)

    def calculate_salary(self):
        return self.get_salary() + 5000
    
class Manager(Employee):

    def __init__(self, name,salary,dept):
        super().__init__(name,salary)
        self.dept=dept

    def display(self):
        super().display()
        print("Department:",self.dept)

    def calculate_salary(self):
        return self.get_salary()+10000
    

class Intern(Employee):

    def __init__(self, name,salary,duration):
        super().__init__(name,salary)
        self.duration=duration

    def display(self): 
        super().display() 
        print("Duration:", self.duration) 

    def calculate_salary(self): 
        return self.get_salary()

e = Employee("Sneha", 32423) 
d = Developer("Sneha", 23423, "Python Developer")
m = Manager("Ananya", 50000, "HR")
i = Intern("Priya", 15000, "6 months")

    
#Employee
print("----- Employee -----")
e.display()
print("Calculated Salary:", e.calculate_salary()) 

# Developer 
print("\n----- Developer -----") 
d.display()
print("Calculated Salary:", d.calculate_salary()) 

# Manager
print("\n----- Manager -----") 
m.display() 
print("Calculated Salary:", m.calculate_salary())

 # Intern 
print("\n----- Intern -----") 
i.display()
print("Calculated Salary:", i.calculate_salary()) 

# Class method
print("\n----- Class Method -----") 
Employee.company_name() 

# Static method 
print("\n----- Static Method -----") 
print(Employee.is_valid_salary(25000))

# __str__ 
print("\n----- __str__ -----") 
print(d)

# Class variable 
print("\nTotal Employees:", Employee.employee_count)