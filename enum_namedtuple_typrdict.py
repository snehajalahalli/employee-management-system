from enum import Enum
from dataclasses import field

class JobStatus:
    APPLIED="applied"
    INTERVIEW="interview"
    SELECTED="selected"
    REJECTED="rejected"

j=JobStatus.APPLIED
print(j)


from enum import Enum

class Role(Enum):
    ADMIN = "admin"
    USER = "user"
    HR = "hr"


def access(role):
    if role == Role.ADMIN or role == Role.HR:
        print("Access permitted")
    else:
        print("Access denied")


access(Role.ADMIN)
access(Role.USER)
access(Role.HR)



from typing import NamedTuple,TypedDict
class Point(NamedTuple):
    x:int
    y:int

p=Point(7,6)
print(p.x)
print(p.y)

class Student(TypedDict):
    name:str
    age:int
    email:str
    skills:list[str]=field(default_factory=list)

s:Student={
    "name":"Sneha",
    "age":21,
    "email":"sneha@123",
    "skills":["python","java"]
}

print(s["name"],s["age"])