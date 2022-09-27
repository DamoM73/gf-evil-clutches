from GameFrame import RoomObject, Globals
from Objects.Demon import Demon
from Objects.Baby import Baby
import random

class Boss(RoomObject):
    """
    A class for the game's antagoist
    """
    def __init__(self, room, x, y):
        # sourcery skip: for-append-to-extend, list-comprehension, remove-zero-from-range
        """
        Initialise the Dragon object
        """
        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)
        
        # set animation values
        self.frame_rate = 4
        self.current_frame = 0
        self.num_frames = 4
        
        # set image
        self.image_frames = []
        for index in range(self.num_frames):
            self.image_frames.append(self.load_image(f"Zork_frames/Zork_{index}.png"))
        self.update_image()
        
        # set inital movement
        self.y_speed = random.choice((-10,10))
        
        # spawn the initial demon spawn time
        demon_spawn_time = random.randint(Globals.demon_min_spawn,Globals.demon_max_spawn)
        self.set_timer(demon_spawn_time,self.spawn_demon)
        
        # spawn the initial baby spawn time
        baby_spawn_time = random.randint(Globals.baby_min_spawn,Globals.baby_max_spawn)
        self.set_timer(baby_spawn_time,self.spawn_baby)
        
    
    def update_image(self):
        """
        Animates the Boss by updating the image 
        """
        self.current_frame = (self.current_frame + 1) % self.num_frames
        self.set_image(self.image_frames[self.current_frame],200,248)
        self.set_timer(self.frame_rate,self.update_image)
    
        
    def step(self):
        """
        Determine what happens to the Boss on each tick of the game clock
        """
        self.keep_in_room()
            
    
    def keep_in_room(self):
        """
        Keeps the Boss inside the top and bottom room limits
        """
        if self.y < 0:
            self.y_speed *= -1
        elif self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y_speed *= -1
           
        
    def spawn_demon(self):
        """
        Randomly spawns a new demon
        """
        # spawn demon and add to room
        new_demon = Demon(self.room, self.x, self.y + self.height/2)
        self.room.add_room_object(new_demon)
        
        # reset time fro next demon spawn
        demon_spawn_time = random.randint(Globals.demon_min_spawn,Globals.demon_max_spawn)
        self.set_timer(demon_spawn_time, self.spawn_demon)

        
    def spawn_baby(self):
        """
        Randomly spawns a new baby
        """
        # spawn baby and add to room
        new_baby = Baby(self.room, self.x, self.y + self.height/2)
        self.room.add_room_object(new_baby)
        
        # reset timer for next baby spawn
        baby_spawn_time = random.randint(Globals.baby_min_spawn + Globals.baby_rescued,
                                         Globals.baby_max_spawn + Globals.baby_rescued*2)
        self.set_timer(baby_spawn_time,self.spawn_baby)