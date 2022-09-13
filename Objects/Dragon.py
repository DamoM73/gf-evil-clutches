from GameFrame import RoomObject, Globals
import pygame

class Dragon(RoomObject):
    """
    A class for the player's avitar (the Dragon)
    """
    
    def __init__(self, room, x, y):
        """
        Initialise the Title object
        """
        # include attributes and methods from RoomObject
        RoomObject.__init__(self,room, x, y)
        
        # set image
        image = self.load_image("Dragon.png")
        self.set_image(image,135,150)
        
        # register for key events
        self.handle_key_events = True
        
    
    def key_pressed(self, key):
        """
        Prespond to keypress up and down
        """
        
        if key[pygame.K_UP]: 
            if self.y <= 0:
                self.y = 0
            else:
                self.y -= 10         
        elif key[pygame.K_DOWN]:
            if self.y >= Globals.SCREEN_HEIGHT - 150:
                self.y = Globals.SCREEN_HEIGHT - 150
            else:
                self.y += 10
        