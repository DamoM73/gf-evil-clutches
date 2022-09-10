from pickle import GLOBAL
from GameFrame import Level
from GameFrame import Globals
from Objects.Credits import Credits

class EndScreen(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # - Add credits text
        self.attrib = Credits(self,150,550,"Created using GameFame: gameframeforpygame.wordpress.com")
        self.attrib.size = 16
        self.attrib.colour = (255, 255, 255)
        self.attrib.update_text()
        self.add_room_object(self.attrib)