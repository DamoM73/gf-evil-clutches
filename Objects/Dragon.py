from GameFrame import RoomObject

class Dragon(RoomObject):
    
    def __init__(self, room, x, y):
        RoomObject.__init__(self,room, x, y)

        # set dragon image
        dragon_image = self.load_image('Dragon_1.png')
        self.set_image(dragon_image, 135, 150)