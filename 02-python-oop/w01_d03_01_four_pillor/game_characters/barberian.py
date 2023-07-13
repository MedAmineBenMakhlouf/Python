from character import Character 
class Barbarian(Character): #Inheritance
    def __init__(self, name):
        super().__init__(name)
        self.power += 30 # polymorphism change parent attribute
        self.health += 20 # polymorphism change parent attribute
        self.rage = 30 # polymorphism add new attribute