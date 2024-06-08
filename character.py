from gameentity import *

class Character(GameEntity):
    def __init__(self, gScreen):
        super().__init__(gScreen)
        self.size = []
        self.pos = None
        self.sprite = []

    @abstractmethod
    def move(self):
        pass
    
    @abstractmethod
    def getRect(self):
        pass