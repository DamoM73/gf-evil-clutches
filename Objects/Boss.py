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
        
    def step(self):
        """
        Determine what happens to the Boss on each tick of the game clock
        """
        # keep inside room
        if self.y < 0:
            self.y_speed *= -1
        elif self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y_speed *= -1
            
        # spawn demon
        if random.randint(1,Globals.spawn_rate) == 1:
            new_demon = Demon(self.room, self.x, self.y)
            self.room.add_room_object(new_demon)