from GameFrame import RoomObject, Globals
from Objects.Demon import Demon
import random

class Boss(RoomObject):
    """
    A class for the game's antagoist
    """
    def __init__(self, room, x, y):
        """
        Initialise the Dragon object
        """
        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Boss.png")
        self.set_image(image,135,165)
        
        # set inital movement
        self.y_speed = random.choice((-10,10))
        
        # spawn the first demon
        spawn_time = random.randint(Globals.demon_min_spawn,Globals.demon_max_spawn)
        self.set_timer(spawn_time,self.spawn_demon)
        
        
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
        new_demon = Demon(self.room, self.x, self.y)
        self.room.add_room_object(new_demon)
        
        spawn_time = random.randint(Globals.demon_min_spawn,Globals.demon_max_spawn)
        self.set_timer(spawn_time, self.spawn_demon)