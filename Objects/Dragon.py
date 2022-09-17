from GameFrame import RoomObject, Globals
import pygame

class Dragon(RoomObject):
    """
    A class for the player's avitar (the Dragon)
    """
    
    def __init__(self, room, x, y):
        """
        Initialise the Dragon object
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
            self.y_speed = -10         
        elif key[pygame.K_DOWN]:
            self.y_speed = 10
                
    
    def step(self):
        """
        Determine what happens to the Dragon on each click of the game clock
        """
        self.keep_in_room()
            
    
    def keep_in_room(self):
        """
        Keeps the dragon inside the top and bottom room limits
        """
        if self.y < 0:
            self.y = 0
        elif self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y = Globals.SCREEN_HEIGHT - self.height
        