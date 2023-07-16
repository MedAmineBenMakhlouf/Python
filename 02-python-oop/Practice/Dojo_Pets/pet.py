class Pet:
    def __init__(self, name , petType , tricks ):
        self.name = name
        self.type = petType
        self.tricks = tricks
        self.health = 0
        self.energy = 0
        
    # implement the following methods:
    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy+=25
        return self
    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy+=5
        self.health+=10
        return self
    # play() - increases the pet's health by 5
    def play(self):
        self.health+=5
        print(self.health)
        return self
    
    # noise() - prints out the pet's sound
    def noise(self):
        print("pet noise")
        
    def __repr__(self):
        return f"Pet Name is: {self.name} --- his Type is: {self.type} --- his tricks: {self.tricks} --- his energy is: {self.energy} --- his health is {self.health}"
        

bagera = Pet("bagera","Cat","fly")

bagera.play().play().eat().sleep()

print(bagera)
