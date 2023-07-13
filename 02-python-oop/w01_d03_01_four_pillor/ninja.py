class Ninja:
    dojo = "Tokyo"
    all_ninjas= []

    def __init__(self, name, age):
        self.name= name
        self.age = age
        self.health = 50
        self.power = 10
        Ninja.all_ninjas.append(self)

    def attack(self,target):
        target.health -= self.power
        print(f"[attack] {self.name} attacked  {target.name} and cause damage equal {self.power}")
        return self
    
    def heal(self):
        # if self.health >= 50:
        #     return self
        self.health =+20
        return self
    @classmethod
    def boot_camp(cls):
        for ninja in cls.all_ninjas:
            ninja.health +=20
            ninja.power += 10
        return None
    @staticmethod
    def validate_ninja(dict):
        is_valid = True
        if(len(dict["name"])<2):
            is_valid = False
        if(dict["age"]<17):
            is_valid = False
        return is_valid

john = Ninja("john",41)
alex = Ninja("Alex",23)
print("Before",alex.health)
john.attack(alex)
print("After",alex.health)