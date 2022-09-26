from GameFrame import Level, Globals
from Objects.Title import Title, DifficultyText

class WelcomeScreen(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
    
        # set background image
        self.set_background_image("Background.bmp")
        
        # add title object
        self.add_room_object(Title(self, Globals.SCREEN_WIDTH / 2 - 250, 
                                   Globals.SCREEN_HEIGHT / 2 - 150))
        
        # add difficulty options
        self.diff_choice = DifficultyText(self, Globals.SCREEN_WIDTH / 2 - 310,
                                          Globals.SCREEN_HEIGHT - 100,
                                          "E: Easy  M: Medium  H: Hard")
        self.add_room_object(self.diff_choice)
        self.diff_choice.update_text()
        
        # play music
        self.soundtrack = self.load_sound("Music.mp3")
        self.soundtrack.play()