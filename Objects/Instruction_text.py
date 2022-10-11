from GameFrame import TextObject

class Text(TextObject):
    """
    Objects for the instructions text
    """
    
    def __init__(self, room, x: int, y: int, text: str):
        """
        Initialise the Instructions object
        """
        TextObject.__init__(self, room, x, y, text)
        
        # set values          
        self.size = 40
        self.font = 'Arial Black'
        self.colour = (255,255,255)