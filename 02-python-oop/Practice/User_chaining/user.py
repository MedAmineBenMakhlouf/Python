class User:
    all_users = []
    def __init__(self,first_name,last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.all_users.append(self)


    def display_info(self):
        print(f'First Name is {self.first_name}, Last name {self.last_name} email: {self.email} age {self.age} is member {self.is_rewards_member} gold {self.gold_card_points}\n')
        return self
    
    def enroll(self):
        if self.is_rewards_member == True:
            print("User already member")
            print("false")
        else:
            print("True")
        return self

    
    def spend_points(self, amount):
        if self.gold_card_points>amount:
            self.gold_card_points-=amount
            
        else:
            print("Not enough points")

        return self

    @classmethod
    def display_all_info(cls):
        for user in cls.all_users:
            user.display_info()
    



Amine = User ("Amine","Ben Makhlouf","medamin@gmail.com",35)


Yassine = User ("Yassine","Ben Makhlouf","medyassineBm@gmail.com",5)
Sadok = User ("Sadok", "Ben Makhlouf","sadok.bm@gmail.com",2)

Amine.display_info().enroll().enroll().spend_points(10).display_info().spend_points(50)

Yassine.enroll().spend_points(80)


Sadok.spend_points(40)

User.display_all_info()