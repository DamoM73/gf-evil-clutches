from GameFrame import Level, Globals
from Objects.Instruction_text import Text

class Instructions(Level):
    
    def __init__(self, screen, joysticks):
        Level.__init__(self,screen, joysticks)
        
        # set background image
        self.set_background_image("Background.png")
        
        # add instructions
        line_1_text = "The evil Zork has kidnapped astronauts from your\nSpace Station"
        self.line_1 = Text(self,
                          Globals.SCREEN_WIDTH / 2 -300,
                          Globals.SCREEN_HEIGHT / 2 -300,
                          line_1_text
                          )
        self.add_room_object(self.line_1)
        self.line_1.update_text()