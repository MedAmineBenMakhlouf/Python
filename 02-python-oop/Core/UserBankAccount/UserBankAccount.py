class BankAccount:
    def __init__(self, int_rate, balance, account_id):
        self.int_rate = int_rate
        self.balance = balance
        self.account_id = account_id

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
class User:
    all_accounts=[]
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
        User.all_accounts.append()
    
    # other methods
    def make_deposit(self, amount, account_id):
    	# your code here

        self.account.deposit(amount)
        return self
    
    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        self.account.display_account_info()

    def add_account(self,account):
        self.add_accounts.append(account)



Amine = User("Amine","mohamedamin.benmakhlouf@gmail.com")
Account1 = BankAccount(0.02,2000)
Account2 = BankAccount(0.02,4000)
# Amine.account = Account1
print(Amine.add_account())
# print(Amine.account.balance)

