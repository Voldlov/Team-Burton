
class Room:

    def __init__(self, location_x, location_y, difficult):
        self.room = [location_x, location_y, difficult]


    def ennemies(self):
        # position et type des ennemies
        enemies_position = [0, 0]
        enemies_type = 1
        return enemies_position, enemies_type

    def trap(self):
        # position et type des pièges
        trap_position = [0, 0]
        trap_type = 1
        return trap_position, trap_type

    def treasur_room(self):
        # position et type de trésor
        return 0