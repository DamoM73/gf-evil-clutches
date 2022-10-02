from GameFrame import TextObject, RoomObject
from GameFrame.Globals import Globals


class Score(TextObject):
    """
    A class for displaying the current score
    """
    def __init__(self, room, x: int, y: int, text=None):
        """
        Intialises the score object
        """         
        # include attributes and methods from TextObject
        TextObject.__init__(self, room, x, y,text)
        
        # set values         
        self.size = 60
        self.font = 'Arial Black'
        self.colour = (255,255,255)
        self.bold = False
        self.update_text()
        
    
    def update_score(self, change):
        """
        Updates the score with each score change event
        """
        Globals.SCORE += change
        self.text = str(Globals.SCORE)
        self.update_text()

        
class Lives(RoomObject):
    
    def __init__(self, room, x: int, y: int):
        # sourcery skip: for-append-to-extend, list-comprehension, remove-zero-from-range
        RoomObject.__init__(self, room, x, y)
        
        # set image
        self.lives_icon = []
        for index in range(0,6):
            self.lives_icon.append(self.load_image(f"Lives_frames/Lives_{index}.png"))
        self.update_image()
        
        
    def update_image(self):
        """
        Updates the number of lives on the UI
        """
        self.set_image(self.lives_icon[Globals.LIVES], 125, 23)
        
        
class RescueTarget(TextObject):
    """
    Records the progress towards hatchling rescue target
    """
    def __init__(self, room, x: int, y: int, text=None):
        """
        Intialises the Rescue Target object
        """         
        # include attributes and methods from TextObject
        TextObject.__init__(self, room, x, y,text)
        
        # set values         
        self.size = 30
        self.font = 'Arial Black'
        self.colour = (255,255,255)
        self.bold = False
        self.update_text()
                
    
    def update_target(self, rescue: bool):
        """
        Changes the update target. If rescue True, baby is rescued, if rescue false, baby has been hit
        """
        if rescue:
            Globals.baby_rescued += 1
        else:
            Globals.baby_target -= 1
        if Globals.baby_rescued == Globals.baby_target:
            self.target_bonus()
            Globals.baby_rescued = 0
            Globals.baby_target *= 2
            Globals.demon_speed += 3
        self.text = f"{Globals.baby_rescued}/{Globals.baby_target} Rescued"
        self.update_text()
        
        
    def target_bonus(self):
        """
        Gives bonus for reaching target
        """
        self.room.score.update_score(Globals.baby_rescued * 10)
        

class SkillCounter(RoomObject):
    """
    Counts down the skill once in use
    """
    def __init__(self, room, x: int, y: int):
        """
        Initialise the skill counter 
        """
        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)
        
        # set animation values
        self.num_frames = 7
        self.current_frame = 6
        
        # set image
        self.image_frames = []
        for index in range(self.num_frames):
            self.image_frames.append(self.load_image(
                f"Skill_frames\Skill_{index}.png"
            ))
        self.set_image(self.image_frames[self.current_frame],124,23)
        
        
    def countdown(self):
        self.current_frame = 0
        self.update_image()
    
    
    def update_image(self):
        if self.current_frame < self.num_frames - 1:
            self.set_image(self.image_frames[self.current_frame],124,23)
            self.current_frame += 1
            self.set_timer(Globals.skill_duration, self.update_image)
        else:
            Globals.skill_active = False
            Globals.ship_speed = 10
            self.current_frame = 5
            self.set_image(self.image_frames[self.current_frame],124,23)
            self.set_timer(Globals.skill_cooldown, self.activate_skill)
            
            
    def activate_skill(self):
        self.current_frame = 6
        self.set_image(self.image_frames[self.current_frame],124,23)
        Globals.skill_available = True