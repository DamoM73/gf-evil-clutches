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
        image = self.load_image("Title.png")
        self.set_image(image,800,350)
        
        # register for key events
        self.handle_key_events = True       
    
    def key_pressed(self, key):  # sourcery skip: extract-duplicate-method
        """
        If the key pressed is space the game will start
        """
        
        if key[pygame.K_SPACE]:
            self.room.running = False
            
            
class Difficulty(RoomObject):
    """
    Displays the difficulty options in the menu
    """
    def __init__(self, room, x, y):  # sourcery skip: for-append-to-extend, list-comprehension
        """
        Initialise the Difficulty instance
        """
        # include TextObject attribute and methods
        RoomObject.__init__(self,room, x, y)
        
        # set image options
        self.num_frames = 3
        
        # set image
        self.image_frames = []
        for index in range(self.num_frames):
            self.image_frames.append(self.load_image(
                f"Select_difficulty_frames\Select_difficulty_{index}.png"
                ))
        self.set_image(self.image_frames[1],500,78)
        
        # register for key events
        self.handle_key_events = True
        
        
    def key_pressed(self, key):  # sourcery skip: extract-duplicate-method
        """
        Changes the difficulty in response to key press
        """
        if key[pygame.K_e]:
            Globals.asteroid_speed = 5
            Globals.asteroid_max_spawn = 200
            self.set_image(self.image_frames[0],500,78)
        elif key[pygame.K_m]:
            Globals.asteroid_speed = 10
            Globals.asteroid_max_spawn = 150
            self.set_image(self.image_frames[1],500,78)
        elif key[pygame.K_h]:
            Globals.asteroid_speed = 15
            Globals.asteroid_max_spawn = 100
            self.set_image(self.image_frames[2],500,78)
            

class ShipSelector(RoomObject):
    """
    Displays the ship options in the menu
    """
    
    def __init__(self,room,x,y):  # sourcery skip: for-append-to-extend, list-comprehension
        """
        Inistalises the ShipSelector object
        """
        # include RoomObject attributes and methods
        RoomObject.__init__(self,room,x,y)
        
        # set image options
        self.num_frames = 3
        
        # set image
        self.image_frames = []
        for index in range(self.num_frames):
            self.image_frames.append(self.load_image(
            f"Select_ship_frames\Select_ship_{index}.png"    
            ))
        self.set_image(self.image_frames[0],400,145)
        
        # register for key events
        self.handle_key_events = True
        
    
    def key_pressed(self, key):  # sourcery skip: extract-duplicate-method
        """
        Changes the difficulty in response to key press
        """
        if key[pygame.K_s]:
            Globals.ship_type = "Swerve"
            self.set_image(self.image_frames[0],400,145)
        elif key[pygame.K_a]:
            Globals.ship_type = "Attractor"
            self.set_image(self.image_frames[1],400,145)