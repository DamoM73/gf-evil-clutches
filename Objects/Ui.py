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
                
    
    def update_target(self):
        """
        Records a rescue of a baby
        """
        Globals.baby_rescued += 1
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
        