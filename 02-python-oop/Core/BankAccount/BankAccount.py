class BankAccount:

    all_accounts=[]
    def __init__(self, int_rate=0.025, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)


    def deposit(self, amount):
        self.balance+=amount

        return self

    def withdraw(self, amount):
        if self.balance<amount:
            print(f"Your balance is {self.balance} you can't withdraw {amount}")
            return self
        self.balance-=amount
        return self
    
    def display_account_info(self):
        print(f'Your Rate is {self.int_rate} --- your balance is {self.balance}')
        return None
    
    def yield_interest(self):
        self.balance = self.balance*self.int_rate
        return self
    
    @classmethod
    def BankAccounts(cls):
        for account in cls.all_accounts:
            account.display_account_info()

Account1 = BankAccount(0.02,2000)
Account2 = BankAccount(0.02,5000)


Account1.deposit(200).deposit(20).deposit(120).withdraw(50).display_account_info()
Account2.deposit(100).deposit(120).withdraw(30).withdraw(50).withdraw(70).withdraw(20).display_account_info()
BankAccount.BankAccounts()