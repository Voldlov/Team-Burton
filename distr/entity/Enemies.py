from entity.Entity import Entity


class Enemies(Entity):
    def getHealth(self):
        return self.health


    def getAttack(self):
        return self.attack

    def getChance(self):
        return self.chance


    def getName(self):
        return self.name