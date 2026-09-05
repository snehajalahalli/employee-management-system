# Q6. Instance Method

# Create a Rectangle class with:

# length
# width

# Create an instance method:

# area()

# that returns the area.

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

r1=Rectangle(7,7)
print(r1.area())


# Q7. Class Variable

# Create a Student class where every student has:

# school = "ABC College"

# Create multiple students.

# Change the school name through the class and observe what happens.

class Student:
    school="ABC college"

    def __init__(self,name):
        self.name=name

    def display(self):
        print("name : ",self.name)
        print("school : ",self.school)

s1=Student("Sneha")
s1.display()

Student.school="XYZ school"
s2=Student("Kanaka")
s2.display()

# Q8. Class Method

# Create an Employee class with a class variable:

# company = "TechCorp"

# Create a class method:

# change_company()

# that changes the company for all employees.

class Employee:
    company="TechCorp"

    def __init__(self,name):
        self.name=name

    @classmethod        
    def change_company(cls,new_company):
        cls.company=new_company

    def display(self):
        print("name:",self.name)
        print("company:",self.company)


e1=Employee("Sneha")
e1.display()

Employee.change_company("Google")

e1.display()

# Q9. Alternative Constructor
# Create a Person class with:

# name
# age

# Implement:

# from_string("Sneha-21")

# using @classmethod.

# It should create and return a Person object.
class Person:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def from_string(cls,data):
        name,age=data.split("-")
        return cls(name,int(age))

    def display(self):
        print("Name:",self.name)
        print("age:",self.age)

p=Person.from_string("sneha-21")
p.display()


# Q10. Static Method

# Create a MathUtils class with:

# is_even(number)
# is_prime(number)

# Make both methods static
class MathUtils:

    @staticmethod
    def is_even(number):
        return number%2==0

    @staticmethod
    def is_prime(number):
        if number<2:
            return False
        for i in range(2,int(number ** 0.5)+1):
            if number%i==0:
                return False
        
        return True

print(MathUtils.is_even(7))
print(MathUtils.is_prime(10))