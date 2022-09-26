from GameFrame import RoomObject
from GameFrame.Globals import Globals

class Baby(RoomObject):
    """
    Class for the babies escaping from the Boss
    """
    
    def __init__(self,room,x,y):
        # sourcery skip: for-append-to-extend, list-comprehension, remove-zero-from-range
        """
        Initialise the baby instance
        """
        # include attirbutes and method from RoomObject
        RoomObject.__init__(self,room,x,y)
        
        # set animation values
        self.frame_rate = 2
        self.current_frame = 0
        self.num_frames = 2
        
        # set image
        self.image_fames = []
        for index in range(self.frame_rate):
            self.image_fames.append(self.load_image(f"Baby_frames/Baby_{index}.png"))
        self.update_image()
        
        # set travel direction
        self.set_direction(180, Globals.baby_speed)
        
        # handle events
        self.register_collision_object("Dragon")
        
    
    # --- Event Handlers
    def handle_collision(self, other, other_type):
        """
        Handles the collision event for Baby objects
        """
        # dragon collision
        if other_type == "Dragon":
            self.room.score.update_score(50)
            self.room.target.update_target()
            self.room.delete_object(self)
            
            
    
    def update_image(self):
        """
        Animates the Baby by chnaging the image per frame rate
        """
        self.current_frame = (self.current_frame + 1) % self.num_frames
        self.set_image(self.image_fames[self.current_frame], 53, 55)
        self.set_timer(self.frame_rate,self.update_image)