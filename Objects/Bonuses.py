from ast import Global
from GameFrame import RoomObject, Globals
import random

class LifeBonus(RoomObject):
    """
    The class for random life bonus
    """
    
    def __init__(self, room, x: int, y: int):
        """
        Initialise Life Bonus object
        """
        # include attributes and methods from RoomObject
        RoomObject.__init__(self,room, x, y)
        
        # set animation values
        self.frame_rate = 10
        self.current_frame = random.randint(0,7)
        self.num_frames = 8
        
        # set image
        self.image_frames = []
        for index in range(self.num_frames):
            self.image_frames.append(self.load_image(f"Repair_kit_frames/Repair_kit_{index}.png"))
        self.update_image()
        
        # set travel direction
        self.set_direction(180, Globals.bonus_speed)
        
        # handle events
        self.register_collision_object("Dragon")
        
        
    # - Event Handlers
    def handle_collision(self, other, other_type):
        """
        Handles collisions for the life bonus object
        """
        # dragon collision
        if other_type == "Dragon":
            if Globals.LIVES < 5:
                Globals.LIVES += 1
                self.room.lives.update_image()
            self.room.delete_object(self)
                
        
    def update_image(self):
        """
        Animates the repair kit
        """
        self.current_frame = (self.current_frame + 1) % self.num_frames
        self.set_image(self.image_frames[self.current_frame],54,54)
        self.set_timer(self.frame_rate, self.update_image)
        
        
class ShieldBonus(RoomObject):
    """
    The class for rando life bonus
    """
    
    def __init__(self, room, x: int, y: int):
        """
        Initilaise shield bonus object
        """
        # include attributes and methods from Room Object
        RoomObject.__init__(self, room, x, y)
        
        # set animation values
        self.frame_rate = 5
        self.current_frame = 0
        self.num_frames = 4
        
        # set image
        self.image_frames = []
        for index in range(self.num_frames):
            self.image_frames.append(self.load_image(f"Shield_frames/Shield_{index}.png"))
        self.update_image()
        
        # set travel direction
        self.set_direction(180, Globals.bonus_speed)

        # handle events
        self.register_collision_object("Dragon")
                
    
    # -- Event Handlers
    def handle_collision(self, other, other_type):
        """
        Handles collisions for the shield bonus object
        """
        # dragon collision
        if other_type == "Dragon":
            other.set_invincible()
            self.room.delete_object(self)
            
    
        
    def update_image(self):
        """
        Animates the shield bonus
        """
        self.current_frame = (self.current_frame + 1) % self.num_frames
        self.set_image(self.image_frames[self.current_frame],54,54)
        self.set_timer(self.frame_rate, self.update_image)