from GameFrame import TextObject
import pygame

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
        
        # register events
        self.handle_key_events = True
        
    
    # --- event handlers
    def key_pressed(self, key):
        """
        Respond to space keypress 
        """
        
        if key[pygame.K_SPACE]:
            self.room.running = False