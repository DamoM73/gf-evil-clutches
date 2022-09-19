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
        image = self.load_image("Fireball.png")
        self.set_image(image, 50, 48)
        
        # set movement
        self.set_direction(0, Globals.fireball_speed)
        
        # register events
        self.register_collision_object("Demon")
        
        
    def handle_collision(self, other, other_type):
        """
        Handles collision events for the Demon
        """
        if other_type == "Demon":
            self.room.delete_object(other)
            self.room.delete_object(self)