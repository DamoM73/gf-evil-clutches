from GameFrame import Level, Globals
from Objects.Instruction_text import Text

class Instructions(Level):
    
    def __init__(self, screen, joysticks):
        Level.__init__(self,screen, joysticks)
        
        # set background image
        self.set_background_image("Background.png")
        
        # add story
        line_1_text = "The evil Zork has kidnapped your astronauts"
        self.line_1 = Text(self,
                          Globals.SCREEN_WIDTH / 2 - 490,
                          Globals.SCREEN_HEIGHT / 2 - 350,
                          line_1_text
                          )
        print(self.line_1.width)
        self.add_room_object(self.line_1)
        self.line_1.update_text()
        
        line_2_text = "from your Space Station."
        self.line_2 = Text(self,
                           Globals.SCREEN_WIDTH / 2 - 260,
                           Globals.SCREEN_HEIGHT / 2 - 300,
                           line_2_text)
        self.add_room_object(self.line_2)
        self.line_2.update_text()
        
        line_3_text = "Capture the astronauts as they escape"
        self.line_3 = Text(self,
                           Globals.SCREEN_WIDTH / 2 - 425,
                           Globals.SCREEN_HEIGHT / 2 - 200,
                           line_3_text)
        self.add_room_object(self.line_3)
        self.line_3.update_text()
        
        line_4_text = "but watch out for the asteroids."
        self.line_4 = Text(self,
                           Globals.SCREEN_WIDTH / 2 - 330,
                           Globals.SCREEN_HEIGHT / 2 - 150,
                           line_4_text)
        self.add_room_object(self.line_4)
        self.line_4.update_text()
        
        # instructions
        line_5_text = "Move Up - W or Up Arrow"
        self.line_5 = Text(self,
                           Globals.SCREEN_WIDTH / 2 - 270,
                           Globals.SCREEN_HEIGHT / 2,
                           line_5_text)
        self.add_room_object(self.line_5)
        self.line_5.update_text()
        
        line_6_text = "Move Down - S or Down Arrow"
        self.line_6 = Text(self,
                           Globals.SCREEN_WIDTH / 2 - 330,
                           Globals.SCREEN_HEIGHT / 2 +50,
                           line_6_text)
        self.add_room_object(self.line_6)
        self.line_6.update_text()
        
        line_7_text = "Fire - Space"
        self.line_7 = Text(self,
                           Globals.SCREEN_WIDTH / 2 - 125,
                           Globals.SCREEN_HEIGHT / 2 + 100,
                           line_7_text)
        self.add_room_object(self.line_7)
        self.line_7.update_text()
                
        line_8_text = "Shoot asteroids without getting hit for extra bullets"
        self.line_8 = Text(self,
                           Globals.SCREEN_WIDTH / 2 - 550,
                           Globals.SCREEN_HEIGHT / 2 + 200,
                           line_8_text)
        self.add_room_object(self.line_8)
        self.line_8.update_text()
        
        line_9_text = "Press ctrl to activate special powers"
        self.line_9 = Text(self,
                           Globals.SCREEN_WIDTH / 2 - 400,
                           Globals.SCREEN_HEIGHT / 2 + 250,
                           line_9_text)
        self.add_room_object(self.line_9)
        self.line_9.update_text()