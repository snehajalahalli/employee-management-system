# Q21. Basic Polymorphism

# Create:

# Dog
# Cat
# Cow

# Each has:

# speak()

# Write one function:
# make_sound(animal)

# that works with all three.

class Dog:
    def speak(self):
        print("dog says woof")

class Cat:
    def speak(self):
        print("cat says meow")

class Cow:
    def speak(self):
        print("cow says moo")

def make_sound(animal):
    animal.speak()


d=Dog()
c=Cat()
cow=Cow()
make_sound(d)
make_sound(c)
make_sound(cow)


class PDF:
    def read(self):
        print("Reading PDF")

class Word:
    def read(self):
        print("Reading Word")

class Image:
    def read(self):
        print("Reading Image")

def process_file(file):
    file.read()

pdf=PDF()
word=Word()
image=Image()

process_file(pdf)
process_file(word)
process_file(image)

class EmailNotification:

    def send(self,msg):
        print("Sendind msg through en",msg)

class SMSNotification:
    def send(self,msg):
        print("Sendind msg through SMS",msg)

class PushNotification:
    def send(self,msg):
        print("Sendind msg through pn",msg)

def notify(service,msg):
    service.send(msg)

en=EmailNotification()
notify(en,"hello")

sms=SMSNotification()
notify(sms,"hello")

pn=PushNotification()
notify(pn,"hello")