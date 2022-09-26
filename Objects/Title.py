from GameFrame import RoomObject, TextObject
import pygame

from GameFrame.Globals import Globals

class Title(RoomObject):
    """
    The object for displaying the title
    """
    def __init__(self, room, x, y):
        """
        Initialise the Title object
        """
        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Title.gif")
        self.set_image(image,500,300)
        
        # register for key events
        self.handle_key_events = True
        
    
    def key_pressed(self, key):  # sourcery skip: extract-duplicate-method
        """
        If the key pressed is space the game will start
        """
        
        if key[pygame.K_e]:
            Globals.demon_speed = 5
            Globals.demon_max_spawn = 200
            self.room.running = False
        elif key[pygame.K_m]:
            Globals.demon_speed = 10
            Globals.demon_max_spawn = 150
            self.room.running = False
        elif key[pygame.K_h]:
            Globals.demon_speed = 15
            Globals.demon_max_spawn = 100
            self.room.running = False
            
            
class DifficultyText(TextObject):
    """
    Displays the difficulty options in the menu
    """
    def __init__(self, room, x, y, text):
        """
        Initialise the DifficultyText instance
        """
        # include TextObject attribute and methods
        TextObject.__init__(self,room, x, y, text)
        
        # set values
        self.size = 40
        self.font = 'Arial Black'
        self.colour = (255,255,255)