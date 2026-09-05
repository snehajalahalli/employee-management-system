# Q17. Protected Convention

# Create a BankAccount with:

# _balance

# Use the _balance convention to indicate that it should not normally be accessed directly from outside.


class BankAccount:

    def __init__(self,balance):
        self._balance=balance

    def deposit(self,amount):
        self._balance+=amount

    def check_balance(self):
        return self._balance

acc=BankAccount(7000)
acc.deposit(777)
print(acc.check_balance())

# Q18. Private Attribute

# Create:

# class User:
#     def __init__(self, password):
#         self.__password = password

# Create a method:

# check_password()

# that verifies a password without exposing the actual password.

class User:
    def __init__(self,password):
        self.__password=password

    def check_password(self,password):
        return self.__password==password

user=User("sneha123")
print(user.check_password("sneha123"))
print(user.check_password("khfier"))


# Q19. Name Mangling

# Given:

# class Test:
#     def __init__(self):
#         self.__value = 10

# obj = Test()

# Answer:

# print(obj.__value)

# What happens?

# Then investigate why this works:

# print(obj._Test__value)

# Explain name mangling.
class Test:
    def __init__(self):
        self.__value = 10

obj = Test()

print(obj._Test__value)


# Q20. Encapsulated Bank Account

# Create a BankAccount where:

# balance is private
# deposit validates the amount
# withdrawal validates the amount
# balance can only be accessed through a method

# Add appropriate validation.
class BankAccount:
    def __init__(self,balance):
        if balance < 0:
            raise ValueError("Initially balance cannot be negative")
        self.__balance=balance

    def deposit(self,amount):
        if amount<=0:
            print("Deposit amount should be greater than 0")
            return
        
        self.__balance+=amount
        print(amount ,"deposited successfully")

    def withdraw(self,amount):
        if amount <=0:
            print("withdraw amount should be greater than 0")
            return

        if amount>self.__balance:
            print("Insufficient balance")
            return

        self.__balance-+amount
        print(amount,"withdrawn successfully")

    def check_balance(self):
        return self.__balance

acc=BankAccount(6767)
print("balance:",acc.check_balance())  

acc.withdraw(573)
print("balance:",acc.check_balance())  

acc.deposit(7982)
print("balance:",acc.check_balance())  

