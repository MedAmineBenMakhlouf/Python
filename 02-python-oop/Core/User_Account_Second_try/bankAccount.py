class BankAccount:
    all_account = []
    def __init__(self, int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        self.all_account.append(self)

    def deposit(self, amount):
        self.balance+=amount
        return self
    
    def withdraw(self, amount):
        if self.balance<amount:
            response = input("Insufficient funds: Charging a $5 fee!! Continue ? Y/N: ")
            if(response == "Y" or response=="y"):
                self.balance-=amount-5
                return self
        self.balance-=amount
        return self
    def display_account_info(self):
        print(f"YOUR BALANCE: ${self.balance}")

    def yield_interest(self):
        self.balance += self.balance*self.int_rate
        return self
    
    @classmethod
    def print_all_instance(cls):
        for account in cls.all_account:
            account.display_account_info

    # def __repr__(self):
    #     print(f"your balance is: ${self.balance} your interest is: {self.int_rate}")
    #     return self

Account1 = BankAccount(0.02,0)
Account2 = BankAccount(0.02,0)

Account1.deposit(200).deposit(20).deposit(120).withdraw(50).display_account_info()
Account2.deposit(100).deposit(120).withdraw(30).withdraw(50).withdraw(70).withdraw(20).display_account_info()

BankAccount.print_all_instance()