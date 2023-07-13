class Character:
    def __init__(self,name):
        self.name = name
        self.health = 50
        self.power = 50
        self.defense = 30
        self.weapon = None

    def attack(self,target):
        # target.health -= self.power
        print(f"[attack] {self.name} attacked  {target.name}")
        damage = target.defend(self.power)
        print(f"and cause damage equal {self.power}")
        return self
    
    def defend(self,damage):
        print(f"[Defend] {self.name} defended  {damage} and reduce it by {self.defense}")
        return self