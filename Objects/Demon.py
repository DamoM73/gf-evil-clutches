from GameFrame import RoomObject

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
        self.set_image(image,130,140)
        
        # set travel
        self.x_speed = -10
        
        