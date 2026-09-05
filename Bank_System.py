class BankAccount:

    def __init__(self,account_number,holder_name,balance):
        self.account_number=account_number
        self.holder_name=holder_name
        self.__balance=balance

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
        else:
             raise ValueError("amount cannot be negative")

        

    def withdraw(self,amount):
        if 0<amount<=self.__balance:
            self.__balance-=amount
        else:
            raise ValueError("amount cannot be negative")
    @property
    def balance(self):
        return self.__balance

    # @balance.setter
    # def balance(self, value):
    #     if value < 0:
    #         raise ValueError("Balance cannot be negative")
    #     self.__balance = value

    def _update_balance(self, amount):
        self.__balance += amount

    def __str__(self):
        return f"Account number :{self.account_number } Holder : {self.holder_name} , Balance{self.__balance} "

    def __eq__(self, other):
        return self.account_number==other.account_number and self.holder_name==other.holder_name


class SavingsAccount(BankAccount):

    def __init__(self, account_number, holder_name, balance,interest_rate):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate=interest_rate

    def withdraw(self,amount):
        if amount<=0:
            raise ValueError("withdraw amount must be positive")
        if amount>self.balance:
            raise ValueError("insufficient balance")
        super().withdraw(amount) 
        

class CurrentAccount(BankAccount):

    
    def __init__(self, account_number, holder_name, balance,overdraft_limit):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit=overdraft_limit

    def withdraw(self,amount):
        if amount<=0:
            raise ValueError("withdraw amount must be positive")
        
        available_amount=self.balance+self.overdraft_limit

        if amount>available_amount:
            raise ValueError("overdraft limit exceed")

        self._update_balance(-amount)
        


account = BankAccount(101, "Sneha", 10000)
account.deposit(5000) 
account.withdraw(3000)
print(account)
print("Balance:", account.balance)

print("\n----- Savings Account -----") 
savings = SavingsAccount( 102, "Sneha", 10000, 5 ) 
savings.deposit(2000)
savings.withdraw(5000) 
print(savings)
print("Interest Rate:", savings.interest_rate) 

print("\n----- Current Account -----")
current = CurrentAccount( 103, "Sneha", 10000, 5000 )
current.withdraw(12000) 
print(current) 
print("Overdraft Limit:", current.overdraft_limit) 

print("\n----- Equality -----") 
account2 = BankAccount(101, "Sneha", 20000) 
print(account == account2)