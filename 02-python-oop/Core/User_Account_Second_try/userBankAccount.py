from bankAccount import BankAccount
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        # self.bank_account = BankAccount(0.02,0)
        self.all_account = [BankAccount(0.02,0)]

    def make_deposit(self,amount):
        response = input(f"select an account to deposit in : 1 - {len(self.all_account)}")

        self.all_account[int(response)-1].deposit(amount)
        return self

    def make_withdrawal(self,amount):
        response = input(f"select an account to withdraw from : 1 - {len(self.all_account)}")

        for account in range(len(self.all_account)):
            self.all_account[int(response)-1].withdraw(amount)
        return self

    def display_user_bale(self):
        response = input("Do You want to display all accounts? Y/N: ")
        if(response== "Y" or response=="y"):
            for i in range(len(self.all_account)):
                print(f"{self.all_account[i].int_rate} ---- {self.all_account[i].balance}")
            return self

    def transfer_money(self,receiver,amount):
        response = input(f"select an account to withdraw from to transfer money : 1 - {len(self.all_account)}")

        for account in range(len(self.all_account)):
            self.all_account[int(response)-1].withdraw(amount)
        print(f"------ {receiver.name} select an account to depose your money")
        receiver.make_deposit(amount)

Amine = User("Amine","amine@gmail.com")
Yassine = User ("Yassine","Yassine@gmail.com")
Yassine.all_account.append(BankAccount(0.02,600))
Amine.make_deposit(200)
# Amine.make_withdrawal(50)
# Amine.display_user_bale()


Amine.transfer_money(Yassine,50)
print("-----Yassine account-----")
Yassine.display_user_bale()