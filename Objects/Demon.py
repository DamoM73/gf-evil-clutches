from GameFrame import RoomObject, Globals
import random

class Demon(RoomObject):
    """
    A class for the game's evil minons
    """
    
    def __init__(self, room, x, y):
        """
        Initialise the Demon object
        """
        # include attributes and methods from RoomObject
        RoomObject.__init__(self,room, x, y)
        
        # set image
        image = self.load_image("Demon.png")
        self.set_image(image,130,115)
        
        # set travel direction
        angle = random.randint(135,225)
        self.set_direction(angle, Globals.demon_speed)
        
    
    def step(self):
        """
        Determines what happens to the demon on each tick of the game clock
        """
        self.keep_in_room()
    
    
    def keep_in_room(self):
        """
        Keeps the demon inside the top and bottom room limits
        """
        if self.y < 0:
            self.y_speed *= -1
        elif self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y_speed *= -1
        