from GameFrame import RoomObject
from GameFrame.Globals import Globals

class Baby(RoomObject):
    """
    Class for the babies escaping from the Boss
    """
    
    def __init__(self,room,x,y):
        """
        Initialise the baby instance
        """
        # include attirbutes and method from RoomObject
        RoomObject.__init__(self,room,x,y)
        
        # set image
        image = self.load_image("Baby.png")
        self.set_image(image, 53, 55)
        
        # set travel direction
        self.set_direction(180, Globals.baby_speed)
        
        # handle events
        self.register_collision_object("Baby")
        
    
    def handle_collision(self, other, other_type):
        """
        Handles the collision event for the baby
        """
        # fireball collision
        if other_type == "Fireball":
            self.room.delete_object(other)
            self.room.delete_object(self)
        elif other_type == "Dragon":
            Globals.SCORE += 1
            self.room.delete_object(self)