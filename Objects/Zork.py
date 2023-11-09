from GameFrame import RoomObject, Globals
from Objects.Asteroid import Asteroid
from Objects.Astronaut import Astronaut
from Objects.Bonuses import LifeBonus, ShieldBonus
import random

from Objects.Ui import Lives

class Zork(RoomObject):
    """
    A class for the game's antagoist
    """
    def __init__(self, room, x, y):
        # sourcery skip: for-append-to-extend, list-comprehension, remove-zero-from-range
        """
        Initialise the Ship object
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
        
        # spawn the initial Asteroid spawn time
        asteroid_spawn_time = random.randint(Globals.asteroid_min_spawn,Globals.asteroid_max_spawn)
        self.set_timer(asteroid_spawn_time,self.spawn_asteroid)
        
        # spawn the initial astronaut spawn time
        astronaut_spawn_time = random.randint(Globals.astronaut_min_spawn,Globals.astronaut_max_spawn)
        self.set_timer(astronaut_spawn_time,self.spawn_astronaut)
        
        # prevent bonuses from spawning
        self.bonus_can_spawn = False
        self.set_timer(Globals.bonus_time, self.spawn_bonus)
        
    
    def update_image(self):
        """
        Animates the Zork by updating the image 
        """
        self.current_frame = (self.current_frame + 1) % self.num_frames
        self.set_image(self.image_frames[self.current_frame],200,248)
        self.set_timer(self.frame_rate,self.update_image)
    
        
    def step(self):
        """
        Determine what happens to the Zork on each tick of the game clock
        """
        self.keep_in_room()
            
    
    def keep_in_room(self):
        """
        Keeps the Zork inside the top and bottom room limits
        """
        if self.y < 0:
            self.y_speed *= -1
        elif self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y_speed *= -1
           
        
    def spawn_asteroid(self):
        """
        Randomly spawns a new Asteroid
        """
        # spawn Asteroid and add to room
        new_asteroid = Asteroid(self.room, self.x, self.y + self.height/2)
        self.room.add_room_object(new_asteroid)
        print(self.room)
        
        # reset time for next Asteroid spawn
        asteroid_spawn_time = random.randint(Globals.asteroid_min_spawn,Globals.asteroid_max_spawn)
        self.set_timer(asteroid_spawn_time, self.spawn_asteroid)

        
    def spawn_astronaut(self):
        """
        Randomly spawns a new astronaut
        """
        # spawn astronaut and add to room
        new_astronaut = Astronaut(self.room, self.x, self.y + self.height/2)
        self.room.add_room_object(new_astronaut)
        
        # reset timer for next astronaut spawn
        astronaut_spawn_time = random.randint(Globals.astronaut_min_spawn + Globals.astronaut_rescued,
                                         Globals.astronaut_max_spawn + Globals.astronaut_rescued*2)
        self.set_timer(astronaut_spawn_time,self.spawn_astronaut)
        
    
    def spawn_bonus(self):
        """
        Spawns a bonus 
        """
        if random.randint(1,Globals.bonus_chance) == 1:
            new_bonus = random.choice([ShieldBonus(self.room, self.x, self.y + self.height/2),
                                       LifeBonus(self.room, self.x, self.y + self.height/2)])
            self.room.add_room_object(new_bonus)
        self.set_timer(Globals.bonus_time, self.spawn_bonus)
        