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
        
        # set object values
        self.invincible = False
        
        # set animation values
        self.frame_rate = 6
        self.current_frame = 0
        self.num_frames = 4
                
        # set image
        self.image_frames = []
        self.invincible_frames = []
        for index in range(self.num_frames):
            self.image_frames.append(self.load_image(f"Rescue_frames/Rescue_{index}.png"))
            self.invincible_frames.append(self.load_image(f"Rescue_invinc_frames/Rescue_{index}.png"))        
        self.update_image()
        
        # register events
        self.handle_key_events = True
        
        # firing mechanism
        self.can_shoot = True
        
    
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
                
    
    def update_image(self):
        """
        Animates the Dragon by changing the image per the frame rate
        """
        self.current_frame = (self.current_frame + 1) % self.num_frames
        if self.invincible:
            self.set_image(self.invincible_frames[self.current_frame],100,100)
        else:    
            self.set_image(self.image_frames[self.current_frame],100,100)
        self.set_timer(self.frame_rate, self.update_image)
    
    
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
        if self.room.count_object("Fireball") < Globals.fireball_max and self.can_shoot:
            new_fireball = Fireball(self.room, self.x + self.width, self.y + self.height/2 - 4)
            self.room.add_room_object(new_fireball)            
            self.can_shoot = False
            self.set_timer(10, self.reset_shoot)
            
    
    def reset_shoot(self):
        """
        Re-enables shooting
        """
        self.can_shoot = True
        
        
    def set_invincible(self):
        """
        Makes the Dragon invincible for limited time
        """
        self.invincible = True
        self.set_timer(Globals.invincible_duration, self.reset_invincible)
        
        
    def reset_invincible(self):
        """
        Turns invinciblew off
        """
        self.invincible = False