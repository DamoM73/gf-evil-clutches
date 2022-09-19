from GameFrame import RoomObject, Globals
from Objects.Fireball import Fireball
import pygame

from Objects.Fireball import Fireball

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
        
        # register events
        self.handle_key_events = True
        
        # allow bullet firing limit
        self.room.set_timer(5, self.reset_shoot)
        self.can_shoot = False
        
    
    # --- event handlers
    def key_pressed(self, key):
        """
        Respond to keypress up and down
        """
        
        if key[pygame.K_w]: 
            self.y_speed = -10         
        elif key[pygame.K_s]:
            self.y_speed = 10
        elif key[pygame.K_SPACE]:
            self.shoot_fireball()
                
    
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
            
            
    def shoot_fireball(self):
        """
        Shoots a fireball from the Dragon
        """
        if self.can_shoot:
            new_fireball = Fireball(self.room, self.x + self.width, self.y)
            self.room.add_room_object(new_fireball)
            self.room.set_timer(10, self.reset_shoot)
            self.can_shoot = False
            
            
    def reset_shoot(self):
        """
        Allows the dragon to shoot again
        """
        self.can_shoot = True
    