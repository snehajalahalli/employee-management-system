class point:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def __add__(self,other):
        return point(self.num1+other.num1,self.num2+other.num2)
p1=point(1,2)
p2=point(3,4)
p3=p1+p2
print(p3.num1)
print(p3.num2)

class Student:
    def __init__(self,marks):
        self.marks=marks

    def __lt__(self,other):
        return self.marks<other.marks

s1=Student(90)
s2=Student(75)
print(s1<s2)

class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self, other):
        return Vector(self.x+other.x,self.y+other.y)

    def __sub__(self,other):
        return Vector(self.x-other.x,self.y-other.y)
    
    def __mul__(self,other):
            return Vector(self.x*other.x,self.y*other.y)
    
    def __eq__(self, other):
        return self.x==other.x and self.y==other.y
    
    def __str__(self):
        return f"Vector({self.x},{self.y})"

v1=Vector(3,4)
v2=Vector(4,3)
print(v1.__add__(v2))
print(v1.__sub__(v2))
print(v1.__mul__(v2))
print(v1.__eq__(v2))