from GameFrame import RoomObject, Globals
import random

class Asteroid(RoomObject):
    """
    A class for the game's evil minons
    """
    
    def __init__(self, room, x, y):  
        """
        Initialise the Asteroid object
        """
        # include attributes and methods from RoomObject
        RoomObject.__init__(self,room, x, y)
        
        # set animation values
        self.frame_rate = 4
        self.current_frame = random.randint(0,7)
        self.num_frames = 8
        
        # set image
        self.image_frames = []
        for index in range(self.num_frames):
            self.image_frames.append(self.load_image(f"Asteroid_frames\Asteroid_{index}.png"))        
        self.update_image()
        
        # set travel direction
        angle = random.randint(135,225)
        self.set_direction(angle, Globals.asteroid_speed)
        
        # register events
        self.register_collision_object("Ship")
        
    
    def update_image(self):
        """
        Animates the asteroid by changing the image as per frame rate
        """
        self.current_frame = (self.current_frame + 1) % self.num_frames
        self.set_image(self.image_frames[self.current_frame],50,49)
        self.set_timer(self.frame_rate, self.update_image)
    
           
    def step(self):
        """
        Determines what happens to the asteroid on each tick of the game clock
        """
        self.keep_in_room()
        self.outside_of_room()
        
    
    # --- Event Handlers
    def handle_collision(self, other, other_type):
        """
        Handles the collision events for Asteroid objects
        """
        if other_type == "Ship":
            if not other.invincible:
                Globals.LIVES -= 1
                self.room.ship_damage.play()
                if Globals.LIVES > 0:
                    self.room.lives.update_image()
                else:
                    self.room.running = False    
                Globals.unharmed_kill_count = 0    
            self.room.delete_object(self)
    
    
    def keep_in_room(self):
        """
        Keeps the asteroid inside the top and bottom room limits
        """
        if self.y < 0:
            self.y = 0
            self.y_speed *= -1
        elif self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y = Globals.SCREEN_HEIGHT - self.height
            self.y_speed *= -1
            
    
    def outside_of_room(self):
        """
        removes asteroid that have exited the room
        """
        if self.x + self.width < 0:
            self.room.delete_object(self)
        
        