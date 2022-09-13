from GameFrame import Level
from Objects.Dragon import Dragon

class GamePlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("Background.bmp")
        
        # add Dragon
        self.add_room_object(Dragon(self,25,50))