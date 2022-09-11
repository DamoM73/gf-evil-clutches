from GameFrame import Level, Globals
from Objects.Title import Title

class WelcomeScreen(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
    
        # set background image
        self.set_background_image("Background.bmp")
        
        # add title object
        self.add_room_object(Title(self, Globals.SCREEN_WIDTH / 2 - 250, 
                                   Globals.SCREEN_HEIGHT / 2 - 150))
        
        # play music
        self.soundtrack = self.load_sound("Music.mp3")
        self.soundtrack.play()