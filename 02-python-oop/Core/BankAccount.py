class BankAccount:
    # don't forget to add some default values for these parameters!
    all_accounts=[]
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance+=amount
        return self
        # your code here
    def withdraw(self, amount):
        # your code here
        self.balance-=amount
        return self
    def display_account_info(self):
        # your code here
        print(f'Your Rate is {self.int_rate} --- your balance is {self.balance}')
        return None
    def yield_interest(self):
        if(self.balance>0):
            self.balance*=self.int_rate
        return self
        # your code here
    @classmethod
    def BankAccounts(cls):
        for account in cls.all_accounts:
            account.display_account_info()

Account1 = BankAccount(0.02,2000)
Account2 = BankAccount(0.02,5000)
# Dep = Account1.deposit(200)
# print(Dep)
# WithdrawAc = Account1.withdraw(20)
# print(WithdrawAc)
# Account1.display_account_info()
# Yield = Account1.yield_interest()
# print(f'yield {Yield}')

Account1.deposit(200).deposit(20).deposit(120).withdraw(50).display_account_info()
Account2.deposit(100).deposit(120).withdraw(30).withdraw(50).withdraw(70).withdraw(20).display_account_info()
BankAccount.BankAccounts()