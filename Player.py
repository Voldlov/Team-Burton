class Player:
    def __int__(self, name):
        self.name = name
        result = self.verify(name)
        if result :
            self.recovery()
        else :
            self.creat()

    def creat(self, name):
        #création d'une nouvelle ligne dans la table

    def verify(self, name):
        #le nom est-il déjà utilisé ?
        return 0

    def recovery(self):
        #récupération des information dans la table

    def passWord(self):
        #comparer les mots de passe demandé et enregistré

    def save(self):
        #sauvegarde des informations
