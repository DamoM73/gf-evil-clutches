import Objects
from GameFrame import Level
from Objects import Dragon

class Cave(Level):

    def __init__(self, screen, joysticks):
        Level.__init__(self,screen,joysticks)

        # add background
        self.set_background_image('Background.bmp')
        
        # add mother dragon
        dragon_obj = Dragon(self,100,400)
        self.add_room_object(dragon_obj)