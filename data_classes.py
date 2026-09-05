from dataclasses import dataclass,field
@dataclass
class Product:
    name:str
    price:float
    category:str

    

p=Product("sneha",34.23,"dress")
print(p.name)
print(p.price)
print(p.category)

@dataclass
class Student:
    name:str
    age:int
    marks:float

s1=Student("sneha",21,91.33)
s2=Student("sneha",21,91.33)

print(s1==s2)
print(s1)


@dataclass
class User:
    name:str
    email:str
    active:bool = True
    role:str="User"

u=User("sneha","sneha@123")
print(u)

u1=User("Shilpa","shilpa@123","false","Admin")
print(u1)


@dataclass
class Job:
    title:str
    company:str
    salary:float
    location:str="remote"
    skills:list[str]=field(default_factory=list)

    

j=Job("BD","techcorp",8872.1,skills=["python","java"])
print(j)