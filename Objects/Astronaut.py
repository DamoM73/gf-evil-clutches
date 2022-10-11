from GameFrame import RoomObject
from GameFrame.Globals import Globals
import random

class Astronaut(RoomObject):
    """
    Class for the babies escaping from the Zork
    """
    
    def __init__(self,room,x,y):
        # sourcery skip: for-append-to-extend, list-comprehension, remove-zero-from-range
        """
        Initialise the astronaut instance
        """
        # include attirbutes and method from RoomObject
        RoomObject.__init__(self,room,x,y)
        
        # set animation values
        self.frame_rate = 4
        self.current_frame = random.randint(0,7)
        self.num_frames = 8
        
        # set image
        self.image_fames = []
        for index in range(self.num_frames):
            self.image_fames.append(self.load_image(f"Astronaut_frames/Astronaut_{index}.png"))
        self.update_image()
        
        # set travel direction
        self.set_direction(180, Globals.astronaut_speed)
        
        # handle events
        self.register_collision_object("Ship")
        
    
    def update_image(self):
        """
        Animates the Astronaut by chnaging the image per frame rate
        """
        self.current_frame = (self.current_frame + 1) % self.num_frames
        self.set_image(self.image_fames[self.current_frame], 56, 56)
        self.set_timer(self.frame_rate,self.update_image)
    
    
    def step(self):
        """
        Determines what happend to the astronaut on each tick of the game clock
        """
        self.outside_of_room()
        if Globals.skill_active and Globals.ship_type == "Attractor":
            self.rotate_to_coordinate(self.room.ship.x,self.room.ship.y)
    
    
    # --- Event Handlers
    def handle_collision(self, other, other_type):
        """
        Handles the collision event for Astronaut objects
        """
        # ship collision
        if other_type == "Ship":
            self.room.astronaut_saved.play()
            self.room.score.update_score(50)
            self.room.target.update_target(True)
            self.room.delete_object(self)
            
    
    def outside_of_room(self):
        """
        removes babies that have existed the room
        """
        if self.x < 0 - self.width:
            self.room.delete_object(self)