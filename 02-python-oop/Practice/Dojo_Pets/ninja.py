from pet import Pet
class Ninja:
    def __init__(self, first_name , last_name , treats , pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet("Simp","Dog","wizard")
        


    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        return self
    
    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        self.pet.eat()
        return self
    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.noise()
        return self
    
treatpet = ["treat1", "treat2"]
foodpet = ["pizza", "burger"]

gogo = Ninja("gogo","flidg",treatpet,foodpet)

gogo.pet.type = "elf"

gogo.feed().walk().bathe()