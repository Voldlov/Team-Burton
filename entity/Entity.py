class Entity:

    def __init__(self, health_max, attack_max, luck_max, speed_max, defense_max):
        self.health, self.health_max = health_max
        self.attack, self.attack_max = attack_max
        self.luck, self.luck_max = luck_max
        self.speed, self.speed_max = speed_max
        self.defense, self.defense_max = defense_max

    def death(self, health):
        #si la vie est à 0 retourner le statue 0
        if health == 0 :
            status = 1
        else :
            status = 0
        return status

    def fight(self, p1, p2):
        #se lance pour les combats
        status = 1
        while status == 1:
            attack()
            death(p1.health)
            death(p2.health)

    def attack(self, health_def, defense_def, attack_atk):
        #attaque classique
        #défense
        atk = attack_atk - defense_def
        #retirer les points de vie
        return health_def - atk