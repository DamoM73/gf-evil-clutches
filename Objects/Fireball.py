from GameFrame import RoomObject
from GameFrame.Globals import Globals

class Fireball(RoomObject):
    """
    Class for the fireballs shot by the Dragon
    """
    
    def __init__(self, room, x, y):
        """
        Inistialise the firesball
        """
        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Laser.png")
        self.set_image(image, 33, 9)
        
        # set movement
        self.set_direction(0, Globals.fireball_speed)     
        
        # handle event
        self.register_collision_object("Demon")
        self.register_collision_object("Baby")
        
        
    # ---- Event handlers
    def handle_collision(self, other, other_type):
        """
        Handles fireball collisions with other registered objects
        """
        if other_type == "Demon":
            self.room.delete_object(other)
            self.room.delete_object(self)
            self.room.score.update_score(5)
        elif other_type == "Baby":
            self.room.delete_object(other)
            self.room.delete_object(self)
            self.room.score.update_score(-10)