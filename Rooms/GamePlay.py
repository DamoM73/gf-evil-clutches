from GameFrame import Level, Globals
from Objects.Dragon import Dragon
from Objects.Boss import Boss
from Objects.Ui import Score, Lives, RescueTarget, SkillCounter

class GamePlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("Background.png")
        
        # add objects
        self.dragon = (Dragon(self, 25, 50))
        self.add_room_object(self.dragon)
        self.add_room_object(Boss(self, Globals.SCREEN_WIDTH - 225, 200))
        
        self.score = Score(self, Globals.SCREEN_WIDTH/2 - 20, 20, str(Globals.SCORE))
        self.add_room_object(self.score)
        
        self.lives = Lives(self, Globals.SCREEN_WIDTH - 150, 20)
        self.add_room_object(self.lives)
        
        self.target = RescueTarget(self, 25,
                                   Globals.SCREEN_HEIGHT - 50,
                                   f"{Globals.baby_rescued}/{Globals.baby_target} Rescued")
        self.add_room_object(self.target)
        
        self.skill_counter = SkillCounter(self, Globals.SCREEN_WIDTH/2 - 62,
                                          Globals.SCREEN_HEIGHT - 50)
        self.add_room_object(self.skill_counter)