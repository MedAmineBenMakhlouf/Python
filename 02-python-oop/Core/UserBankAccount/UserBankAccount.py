class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self
        # your code here

    def withdraw(self, amount):
        # your code here
        self.balance -= amount
        return self

    def display_account_info(self):
        # your code here
        print(f"Your Rate is {self.int_rate} --- your balance is {self.balance}")
        return None

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= self.int_rate
        return self
        # your code here


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_accounts= []

    # other methods
    def make_deposit(self):
        # your code here
        account_index = input("Which account? ")
        amount = input("How much")
        account_index = int(account_index)-1
        if account_index<len(self.all_accounts) or account_index<0:
            self.all_accounts[account_index].deposit(float(amount))
        return self



    def make_withdrawal(self):
        account_index = input("Which Account ? ")
        amount = input("How Much ? ")
        account_index = int(account_index)-1
        if account_index<len(self.all_accounts) or account_index<0:
            self.all_accounts[account_index].withdraw(float(amount))
        return self

    def display_user_balance(self):
        for i in range(len(self.all_accounts)):
            self.all_accounts[i].display_account_info()
        return self


    def add_account(self, unt_rate, amount):
            self.all_accounts.append(BankAccount(unt_rate,amount))


Account1 = BankAccount(0.02, 2000)
Account2 = BankAccount(0.02, 4000)

Amine = User("Amine", "mohamedamin.benmakhlouf@gmail.com")
User.add_account(Account1)
User.add_account(Account2)
print(Amine.all_accounts[0].balance)
Amine.make_withdrawal()
print(Amine.all_accounts[0].balance)
# Amine.display_user_balance()
# Amine.account = Account1
# print(Amine.account.balance)
