from GameFrame import Level, Globals
from Objects.Title import Title, Difficulty, ShipSelector

class WelcomeScreen(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
    
        # set background image
        self.set_background_image("Background.png")
        
        # add title object
        self.add_room_object(Title(self, 
                                   Globals.SCREEN_WIDTH / 2 - 400, 
                                   50))
        
        # add ship options
        self.ship_choice = ShipSelector(self,
                                        Globals.SCREEN_WIDTH / 2 - 200,
                                        500)
        self.add_room_object(self.ship_choice)
        self.ship_choice.update()
        
        # add difficulty options
        self.diff_choice = Difficulty(self, 
                                      Globals.SCREEN_WIDTH / 2 - 250,
                                      Globals.SCREEN_HEIGHT - 100)
        self.add_room_object(self.diff_choice)
        self.diff_choice.update()
        
        # play music
        self.soundtrack = self.load_sound("Music.mp3")
        self.soundtrack.set_volume(0.2)
        self.soundtrack.play(loops=-1)
        