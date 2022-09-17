from GameFrame import Level, Globals
from Objects.Credits import Credits

class EndScreen(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # - Add credits text
        self.attrib = Credits(self, Globals.SCREEN_WIDTH / 2 - 250,
                              Globals.SCREEN_HEIGHT - 30,
                              "Created using GameFame: gameframeforpygame.wordpress.com")
        self.attrib.size = 16
        self.attrib.colour = (255, 255, 255)
        self.attrib.update_text()
        self.add_room_object(self.attrib)