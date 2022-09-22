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
        self.register_collision_object("Dragon")
        
    
    # --- Event Handlers
    def handle_collision(self, other, other_type):
        """
        Handles the collision event for Baby objects
        """
        # dragon collision
        if other_type == "Dragon":
            self.room.score.update_score(50)
            self.room.delete_object(self)
        elif other_type == "Fireball":
            self.room.delete_object(self)
            self.room.delete_object(other)
            self.room.score.update_score(-10)
            