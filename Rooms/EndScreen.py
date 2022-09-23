from GameFrame import Level, Globals
from Objects.Credits import Credits, FinalScore
from GameFrame import Globals

class EndScreen(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # --- Add credits text
        self.attrib = Credits(self, 
                              Globals.SCREEN_WIDTH / 2 - 250,
                              Globals.SCREEN_HEIGHT - 30,
                              "Created using GameFame: gameframeforpygame.wordpress.com")
        self.add_room_object(self.attrib)
        self.attrib.update_text()
        
        # --- Add final score
        self.final_score = FinalScore(self, 
                                      Globals.SCREEN_WIDTH / 2 - 300,
                                      Globals.SCREEN_HEIGHT / 2 - 80,
                                      f"SCORE: {Globals.SCORE}")
        self.add_room_object(self.final_score)
        self.final_score.update_text()