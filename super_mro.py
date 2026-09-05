# Q24. super()

# Create:

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

# Explain exactly what super().__init__(name) does.



# Q25. Overriding + super()

# Create:

# Employee
#    ↓
# Developer

# Both classes should have a display() method.

# Call the parent's display() from the child's display() using super().
class Employee:
    def display(self):
        print("this is class employee")

class Developer(Employee):
    def display(self):
        return super().display()

d=Developer()
d.display()

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(B):
    def show(self):
        print("C")

obj = C()
obj.show()
print(C.mro())


class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
        super().show()

class C(A):
    def show(self):
        print("C")
        super().show()

class D(B, C):
    def show(self):
        print("D")
        super().show()

D().show()
print(D.mro())