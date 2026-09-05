# Q12. Basic Inheritance

# Create:

# Animal
#    ↓
# Dog

# Animal should have:

# eat()
# sleep()

# Dog should have:

# bark()

# Create a Dog object and call all three methods.

class Animal:
    def eat(self):
        return "Eat"

    def sleep(self):
        return "sleep"

class Dog(Animal):
    def bark(self):
        return "Bark"

d=Dog()
print(d.bark())
print(d.eat())
print(d.sleep())


# Q13. Method Overriding

# Create:

# Animal
#  ├── Dog
#  └── Cat

# Give Animal:

# sound()

# Override sound() in Dog and Cat.

class Animal:
    def sound(self):
        print("make sound")

class Dog(Animal):

    
    def sound(self):
        print("dog says woof")

class Cat(Animal):

    def sound(self):
        print("cat says meow")

d=Dog()
d.sound()

c=Cat()
c.sound()


# Q14. Employee Hierarchy

# Create:

# Employee
#  ├── Developer
#  └── Manager

# Employee:

# name
# salary

# Developer:

# programming_language

# Manager:

# team_size

# Implement suitable methods.

class Employee:

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def display(self):
        print("name:",self.name)
        print("salary:",self.salary)

class Developer(Employee):

    def __init__(self, name, salary,programing_languege):
        super().__init__(name, salary)
        self.programming_language=programing_languege
        print(name , salary, programing_languege)


    def display(self):
        super().display()
        print("programming language : ",self.programming_language)

class Manager(Employee):

    def __init__(self, name, salary,team_size):
        super().__init__(name, salary)
        self.team_size=team_size

    def display(self):
        super().display()
        print("team size:",self.team_size)

d=Developer("Sneha",21,"python")
m=Manager("sneha",21,7)

d.display()
m.display()


# Q15. Multilevel Inheritance

# Create:

# Vehicle
#    ↓
# Car
#    ↓
# ElectricCar

# Each class should have at least one unique attribute and method.

# Create an ElectricCar object and access functionality from all three levels.

class Vehical:

    def __init__(self,name):
        self.name=name

    def start(self):
        print(self.name,"is starting")

class Car(Vehical):

    def __init__(self, name,brand):
        super().__init__(name)
        self.brand=brand

    def drive(self):
        print(self.brand,"is driving")

    

class ElectricCar(Car):

    def __init__(self,name,brand,price):
        super().__init__(name,brand)
        self.price=price

    def charge(self):
        print("stop driving")

e=ElectricCar("sfd","edwe",87953)
e.start()
e.drive()
e.charge()

print(e.brand)
print(e.name)
print(e.price)


# Q16. Hierarchical Inheritance

# Create:

# Shape
#  ├── Circle
#  ├── Rectangle
#  └── Triangle

# Each class should calculate its own area.

class Shape:

    def display(self):
        print("this is a shape")

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14 * self.radius *self.radius

class Rectangle(Shape):

    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

class Triangle(Shape):

    def __init__(self,base,heigth):
        self.base=base
        self.heigth=heigth

    def area(self):
        return 0.5 * self.base * self.heigth

c=Circle(7)
r=Rectangle(7,7)
t=Triangle(7,7)

print(c.area())
print(r.area())
print(t.area())