from GameFrame import RoomObject, Globals
from Objects.Laser import Laser
import pygame

from Objects.Laser import Laser

class Ship(RoomObject):
    """
    A class for the player's avitar (the Ship)
    """
    
    def __init__(self, room, x, y):
        """
        Initialise the Ship object
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
            if Globals.ship_type == "Swerve":
                self.image_frames.append(self.load_image(
                    f"Rescue_frames/Rescue_{index}.png"
                    ))
                self.invincible_frames.append(self.load_image(
                    f"Rescue_invinc_frames/Rescue_{index}.png"
                    ))
            elif Globals.ship_type == "Attractor":
                self.image_frames.append(self.load_image(
                    f"Attractor_frames/Rescue_{index}.png"
                    ))
                self.invincible_frames.append(
                    self.load_image(f"Attractor_invinc_frames/Rescue_{index}.png"
                    ))
        self.update_image()
        
        # register events
        self.handle_key_events = True
        
        # firing mechanism
        self.can_shoot = False
        self.set_timer(5,self.reset_shoot)
        
        
    
    # --- event handlers
    def key_pressed(self, key):
        """
        Respond to keypress up and down
        """
        
        if key[pygame.K_w] or key[pygame.K_UP]: 
            self.y_speed = Globals.ship_speed * -1       
        elif key[pygame.K_s] or key[pygame.K_DOWN]:
            self.y_speed = Globals.ship_speed
        elif key[pygame.K_SPACE]:
            self.shoot_laser()    
        elif (key[pygame.K_LCTRL] or key[pygame.K_RCTRL]) and Globals.skill_available:
            Globals.skill_available = False
            self.activate_skill()
            self.room.skill.play()
                
    
    def update_image(self):
        """
        Animates the Ship by changing the image per the frame rate
        """
        self.current_frame = (self.current_frame + 1) % self.num_frames
        if self.invincible:
            self.set_image(self.invincible_frames[self.current_frame],100,100)
        else:    
            self.set_image(self.image_frames[self.current_frame],100,100)
        self.set_timer(self.frame_rate, self.update_image)
    
    
    def step(self):
        """
        Determine what happens to the Ship on each click of the game clock
        """
        self.keep_in_room()
            
    
    def keep_in_room(self):
        """
        Keeps the ship inside the top and bottom room limits
        """
        if self.y < 0:
            self.y = 0
        elif self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y = Globals.SCREEN_HEIGHT - self.height
            
            
    def shoot_laser(self):
        """
        Shoots a laser from the Ship
        """
        if self.room.count_object("Laser") < Globals.laser_max and self.can_shoot:
            self.room.laser_shot.play()
            new_laser = Laser(self.room, self.x + self.width, self.y + self.height/2 - 4)
            self.room.add_room_object(new_laser)            
            self.can_shoot = False
            self.set_timer(10, self.reset_shoot)
            
    
    def reset_shoot(self):
        """
        Re-enables shooting
        """
        self.can_shoot = True
        
        
    def set_invincible(self):
        """
        Makes the Ship invincible for limited time
        """
        self.invincible = True
        self.set_timer(Globals.invincible_duration, self.reset_invincible)
        
        
    def reset_invincible(self):
        """
        Turns invincible off
        """
        self.invincible = False
        
        
    def activate_skill(self):
        """
        Activates the ships special skill according to the ship type
        """                
        Globals.skill_active = True
        Globals.skill_available = False
        Globals.ship_speed = 20
        self.room.skill_counter.countdown()
