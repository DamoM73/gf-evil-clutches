from GameFrame import TextObject

class Credits(TextObject):
    def __init__(self, room, x, y, text):
        TextObject.__init__(self, room, x, y, text)
        
        # set values
        self.size = 16
        self.colour = (255, 255, 255)
        
        
class FinalScore(TextObject):
    def __init__(self, room, x, y, text):
        TextObject.__init__(self, room, x, y, text)
        
        # set values         
        self.size = 100
        self.font = 'Arial Black'
        self.colour = (255,255,255)