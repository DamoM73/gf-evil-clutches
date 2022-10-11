from GameFrame import Level, Globals
from Objects.Ship import Ship
from Objects.Zork import Zork
from Objects.Ui import Score, Lives, RescueTarget, SkillCounter

class GamePlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("Background.png")
        
        # add objects
        self.ship = (Ship(self, 25, 50))
        self.add_room_object(self.ship)
        self.add_room_object(Zork(self, Globals.SCREEN_WIDTH - 225, 200))
        
        self.score = Score(self, Globals.SCREEN_WIDTH/2 - 20, 20, str(Globals.SCORE))
        self.add_room_object(self.score)
        
        self.lives = Lives(self, Globals.SCREEN_WIDTH - 150, 20)
        self.add_room_object(self.lives)
        
        self.target = RescueTarget(self, 25,
                                   Globals.SCREEN_HEIGHT - 50,
                                   f"{Globals.astronaut_rescued}/{Globals.astronaut_target} Rescued")
        self.add_room_object(self.target)
        
        self.skill_counter = SkillCounter(self, Globals.SCREEN_WIDTH/2 - 62,
                                          Globals.SCREEN_HEIGHT - 50)
        self.add_room_object(self.skill_counter)
        
        # load sounds
        self.laser_shot = self.load_sound("Laser_shot.ogg")
        self.astronaut_saved = self.load_sound("Astronaut_saved.ogg")
        self.asteroid_hit = self.load_sound("Asteroid_shot.wav")
        self.asteroid_hit.set_volume(0.25)
        self.bonus_score = self.load_sound("Bonus_score.mp3")
        self.bonus_score.set_volume(0.1)
        self.shot_increase = self.load_sound("Max_shot_increase.wav")
        self.bonus_score.set_volume(0.01)
        self.life_increase = self.load_sound("Life_increase.ogg")
        self.shields = self.load_sound("Shields.ogg")
        self.skill = self.load_sound("Skill_used.mp3")
        self.skill.set_volume(0.5)
        self.astronaut_hit = self.load_sound("Astronaut_hit.ogg")
        self.ship_damage = self.load_sound("Ship_damage.ogg")