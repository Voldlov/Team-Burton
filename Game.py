from Player import Player
import Monster import Monster


class Game:
    def __init__(self):
		while True:
			self.cmd=input("Ceolcyn")
			if self.cmd=="exit":
				exit()
    def __int__(self):
        self.pressed = {}
        self.player = Player(self)

    def spawn_monster (self):
        Monster = Monster