# Q1. Basic Class

# Create a Student class with:

# name
# age
# course

# Create 3 student objects and print their details.

class Student:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Course:",self.course)
        print()

s1=Student("Sneha",21,"CSE")
s2=Student("Shilpa",28,"EEE")
s3=Student("Sahana",20,"Civil")

s1.display()
s2.display()
s3.display()


# Q2. Constructor

# Create a Car class whose __init__() accepts:

# brand
# model
# price

# Create two cars and display their information.

class Car:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price

    def display(self):
        print("Brand:",self.brand)
        print("Model:",self.model)
        print("Price:",self.price)
        print()

c1=Car("Audi","S1",2324)
c2=Car("Maruthi","S2",2343454)

c1.display()
c2.display()

# Q3. Instance Attributes

# Create an Employee class with:

# name
# salary

# Add a method display() that prints both.

# Create two employees and verify that changing one employee's salary does not affect the other.

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def display(self):
        print("name : ",self.name , "salary : ",self.salary)
        print()


e1=Employee("Sneha",50000)
e2=Employee("Shilpa",938824)

print("before changing")
e1.display()
e2.display()


#changing salary
e1.salary=216381

print("after changing")
e1.display()
e2.display()


# Q4. Understanding self

# What happens in this code?
# """Student.__init__() takes 
# 2 positional arguments but 
# 3 were given"""

# class Student:
#     def __init__(name, age):
#         name = name
#         age = age

# s = Student("Sneha", 21)

# Explain the problem and fix it.


class BankAccount:

    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(amount," deposited successfully")
        

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance-=amount
            print(amount," withdrawn successfully")
        
        else:
            print("insufficient balance")

    def check_balance(self):
        print("balance : ",self.balance)


acc=BankAccount("Sneha",7000)

acc.check_balance()

acc.deposit(6562)
acc.check_balance()

acc.withdraw(52)
acc.check_balance()