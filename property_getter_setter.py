# Q41. Basic Property

# Create a Person class with a private:

# __age

# Create a property:

# age

# that allows reading the age

# class Person:
#     def __init__(self,age):
#         self.__age=age

#     @property
#     def age(self):
#         return self.__age

# p=Person(7)
# print(p.age)

class Person:

    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 0 < value < 150:
            self.__age = value
        else:
            raise ValueError("Age is invalid")

p1=Person(9)
print(p1.age)

# p2=Person(-1)
# print(p2.age)


# Q43. Temperature

# Create a Temperature class storing Celsius.

# Provide:

# celsius
# fahrenheit

# using properties.

# Changing Celsius should automatically affect Fahrenheit.

class Temperature:

    def __init__(self,celsius):
        self._celsius=celsius
        

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self,value):
        self._celsius=value 

    @property
    def fahrenheit(self):
        return self._celsius * (9/5) +32

t=Temperature(32)
print(t.celsius)
print(t.fahrenheit)

t.celsius=100

print(t.celsius)
print(t.fahrenheit)

# Q44. Backend-Style Validation 🔥

# Create a User class with:

# username
# email
# age

# Use properties to validate:

# username cannot be empty
# email must contain @
# age must be positive
class User:
    def __init__(self,username,email,age):
        self.username=username
        self.email=email
        self.age=age

    @property
    def username(self):
        return self._username    

    @property
    def email(self):
        return self._email

    @property
    def age(self):
        return self._age

    @username.setter
    def username(self,value):
        if value:
            self._username=value
        else:
            raise ValueError("username connot be empty")

    @email.setter
    def email(self,value):
        if "@" in value:
            self._email=value
        else:
            raise ValueError("email must contain @")

    @age.setter
    def age(self,value):
        if value>0:
            self._age=value
        else:
            raise ValueError("age must be greater than 0")

u=User("sneha","snehajalahalli@",21)

print(u.username)
print(u.email)
print(u.age)            


        

    

