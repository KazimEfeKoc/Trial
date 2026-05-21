from character import Character

class Creature:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        a = Character(self)
        a.life -= 1