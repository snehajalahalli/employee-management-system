from abc import abstractmethod,ABC

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self,radius):
        return 3.14 * radius * radius


class Rectangle(Shape):
    def area(self,length,width):
        return length * width

c=Circle()
r=Rectangle()
print(c.area(7))
print(r.area(7,7))
# s=Shape()

class Payment(ABC):

    @abstractmethod
    def pay(self,amount):
        
        pass

class CreditCardPayment(Payment):

    
    def pay(self,amount):
        
        print(amount,"paying through credit card")

class UPIPayment(Payment):

    def pay(self,amount):
        print(amount,"paid through UPI")

class PayPalPayment(Payment):

    def pay(self,amount):
        print(amount,"paid through paypal")

cc=CreditCardPayment()
cc.pay(765)

upi=UPIPayment()
upi.pay(765)

pp=PayPalPayment()
pp.pay(765)