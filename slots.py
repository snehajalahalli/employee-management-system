class Student:

    __slots__=["name","age"]

    def __init__(self,name,age):
        self.name=name
        self.age=age

s=Student("sneha",21)
s.name="sneha"
s.age=21
# s.email="sdas2@"

class NormalStudent:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class SlottedStudent:
    __slots__ = ["name", "age"]

    def __init__(self, name, age):
        self.name = name
        self.age = age

normal = NormalStudent("Sneha", 21)
slotted = SlottedStudent("Sneha", 21)

print(normal.__dict__)
# print(slotted.__dict__)