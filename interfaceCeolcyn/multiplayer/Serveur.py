#! /usr/bin/python3
# -*- coding: utf-8 -*-

import socket, sys, threading, time

# adresse IP et port utilisés par le serveur
HOST = ""
PORT = 50026

NOMBREJOUEUR = 2

dict_clients = {}  # dictionnaire des connexions clients
dict_pseudos = {}  # dictionnaire des pseudos
dict_reponses = {}  # dictionnaire des réponses des clients
dict_scores = {} # dictionnaire des scores
dict_scores_total = {}


class ThreadClient(threading.Thread):
    '''dérivation de classe pour gérer la connexion avec un client'''
    
    def __init__(self,conn):

        threading.Thread.__init__(self)
        self.connexion = conn
        
        # Mémoriser la connexion dans le dictionnaire
        
        self.nom = self.getName() # identifiant du thread "<Thread-N>"
        dict_clients[self.nom] = self.connexion
        dict_scores[self.nom] = 0
        dict_scores_total[self.nom] = 0
        
        print("Connexion du client", self.connexion.getpeername(),self.nom ,self.connexion)
        
        message = bytes("Vous êtes connecté au serveur.\n","utf-8")
        self.connexion.send(message)
        
        
    def run(self):
        
        # Choix du pseudo    
        
        self.connexion.send(b"Entrer un pseudo :\n")
        # attente réponse client
        pseudo = self.connexion.recv(4096)
        pseudo = pseudo.decode(encoding='UTF-8')
        
        dict_pseudos[self.nom] = pseudo
        
        print("Pseudo du client", self.connexion.getpeername(),">", pseudo)
        
        message = b"Attente des autres clients...\n"
        self.connexion.send(message)
    
        # Réponse aux questions
       
        while True:
            
            try:
                # attente réponse client
                reponse = self.connexion.recv(4096)
                reponse = reponse.decode(encoding='UTF-8')
            except:
                # fin du thread
                break
                
            # on enregistre la première réponse
            # les suivantes sont ignorées
            if self.nom not in dict_reponses:
                dict_reponses[self.nom] = reponse, time.time()
                print("Réponse du client",self.nom,">",reponse)

        print("\nFin du thread",self.nom)
        self.connexion.close()

def MessagePourTous(message):
    """ message du serveur vers tous les clients"""
    for client in dict_clients:
        dict_clients[client].send(bytes(message,"utf8"))
        
        
# Initialisation du serveur
# Mise en place du socket avec les protocoles IPv4 et TCP
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
try:
    mySocket.bind((HOST, PORT))
except socket.error:
    print("La liaison du socket à l'adresse choisie a échoué.")
    sys.exit()
print("Serveur prêt (port",PORT,") en attente de clients...")
mySocket.listen(5)


# len(dict_clients) -> nb de joueurs connectés

while len(dict_clients) < NOMBREJOUEUR:
    # Attente connexion nouveau client
    try:
        connexion, adresse = mySocket.accept()
    except:
        sys.exit()
    # Créer un nouvel objet thread pour gérer la connexion
    th = ThreadClient(connexion)
    # The entire Python program exits when no alive non-daemon threads are left
    th.setDaemon(1)
    th.start()
    

while len(dict_pseudos) < NOMBREJOUEUR:
    # on attend que tout le monde ait entré son pseudo
    pass


# Fin
MessagePourTous("\nFIN\nVous pouvez fermer l'application...\n")

# fermeture des sockets
for client in dict_clients:
    dict_clients[client].close()
    print("Déconnexion du socket", client)

input("\nAppuyer sur Entrée pour quitter l'application...\n")
# fermeture des threads (daemon) et de l'application