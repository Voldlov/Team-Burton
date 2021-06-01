from mysql import connector


class Player:
    def __int__(self, name):
        #ouvrir la connection
        #cn = connector.connect(user='', password='', host='localhost', database='')
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
        #la requête
        q = 'SELECT *** FROM ***'
        #créer un curseur
        c = cn.cursor()
        #envoyer la requête et recevoir le résultat
        return c.execute(q)

    def passWord(self, mdp):
        #comparer les mots de passe demandé et enregistré
        #la requête
        q = 'SELECT *** FROM ***'
        #créer un curseur
        c = cn.cursor()
        #envoyer la requête et recevoir le résultat
        if mdp == c.execute(q) :
            a = 1
        else :
            a = 0
        return a

    def save(self):
        #sauvegarde des informations

    def close(self):
        #fermer la connexion avec la base de donnée
        cn.close()
