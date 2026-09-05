class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"{self.name},{self.age}"
s=Student("sneha",21)
print(s)

class Book:

    def __init__(self,name,author):
        self.name=name
        self.author=author

    def __str__(self):
        return f"book name:{self.name} author :{self.author}"

    def __repr__(self):
        return f"Book(book name:{self.name} author :{self.author})"

b=Book("Autography","Sneha")
print(b)
print([b])

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __eq__(self, other):
        return self.name==other.name and self.age==other.age

s1=Student("Sneha",21)
s2=Student("Sneha",21)
print(s1==s2)

class Playlist:
    def __init__(self,songs):
        self.songs=songs

    def __len__(self):
        return len(self.songs)

p=Playlist(["a","b","c","d"])
print(len(p))

class Counter:

    def __init__(self):
        self.count=0
    def __call__(self):
        self.count+=1

c=Counter()
c()
c()
print(c.count)

class ShoppingCart:
    def __init__(self,product,price):

        self.product=product
        self.price=price

    def __str__(self):
        return f"product:{self.product} price:{self.price}"

    def __len__(self,):
        return len(self.product)

    def __eq__(self, other):
        return self.product==other.product and self.price==other.price

    def __contains__(self,product):
        return product in self.product


s1=ShoppingCart("pen",5)
s2=ShoppingCart("pens",5)
print(s)
print(s1==s2)
print(len(s1))
print(len(s2))
print("apple" in s1)
print("pens" in s2)