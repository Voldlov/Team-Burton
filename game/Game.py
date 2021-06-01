from Player import Player
from entity import Enemies
import random

class Game:

	def __init__(self):
		#affichage

	def map(self):
		#création de la map c'est une image
		self.maping = "truc.jpg"

	def treasur(self):
		#position du trésor c'est un emplacement dans un tableau
		self.location_treasur = [random.randint(1, 10), random.radint(1, 10)]



#
#Ce qui suit est lancé à chaque fois qu'un joueur rentre dans un pièce, d'abord room qui créer théoriquement la pièce, qui va lancer le calcul des ennemis et des pièges. Mais ça génère aussi les trésors.
#il y a aussi une méthode pour voir si la pièce n'a jamais été générée ou non


	def room(self, difficulty, room):
		#Ce qui se trouve dans le pièce, c'est aléatoire avec un % de chance et de difficulté.
		if room[2] == 1 :
			#récupérer
		else :
			#créer
			#ennemies
			#piège
			#trésor
	def creatRoom(self, position):
		self.room = [position[0], position[1], 1]

	def shearchRoom(self, position):
		#trouver une salle déjà créé

