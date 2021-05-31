class Player:
    def __int__(self):
        self.cordinates = (0,0)
        self.name = "player"
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.defence = 10
        self.luck = 10
        self.velocity = 10

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
#verifier la santé ou l'attaque du personnage

    def getHealth(self):
        return self.health
    def getAttack(self):
        return self.attack
    def getLuck(self):
        return self.luck
    def getDefence(self):
        return self.defence
    def getName(self):
        return self.name

        #player = player()
        #self.pressed = {
        #    "touche fleche_droite":True,
        #    "touche fleche_gauche": False
        #}