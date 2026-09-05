class Person:
    def __init__(self,**kwargs):
        super().__init__(*kwargs)
    def display(self):
        print("i am a person")

class Student(Person):
    def __init__(self,name,**kwargs):
        super().__init__(**kwargs)
        self.name=name

    def display(self):
        super().display()
        print("name:",self.name)

class Employee(Person):
    def __init__(self,eid,**kwargs):
        super().__init__(**kwargs)
        self.eid=eid

    def display(self):
        super().display()
        print("eid",self.eid)

class StudentEmployee(Student,Employee):
    def __init__(self, name,eid,intern):
        super().__init__(name=name,eid=eid)
        self.intern=intern

    def display(self):
        super().display()
        print("intern",self.intern)

se=StudentEmployee("sneha",77,True)
se.display()


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
    pass

D().show()
print(D.mro())

class LoggingMixin:
    def log(self,msg):
        print(self.name,msg)

class UserService(LoggingMixin):
    def create_user(self,name):
        self.name=name

u=UserService()
u.create_user("sneha")
u.log("Logged in")


class ValidateMixin:
    def validate_email(self,email):
        return "@" in email and "." in email

class LoggingMixin:
    def log(self,msg):
        print("log:",msg)

class UserService(ValidateMixin,LoggingMixin):

    def create_user(self,name,email):
        if not self.validate_email(email):
            print("invalid email")
            return
        self.log(f"User {name} created")
        print("User created successfully")


U=UserService()
U.create_user("Sneha","sneha@jalahalli.com")
