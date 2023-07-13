import character
class Elf(character.Character):
    def __init__(self, name):
        super().__init__(name)

    def magic_attack(self,target):
        target.health -= self.power
        target.power -=20
        target.defense -= 20