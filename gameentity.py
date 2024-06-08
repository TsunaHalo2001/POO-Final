from abc import ABC, abstractmethod

class GameEntity(ABC):
    def __init__(self, gScreen):
        self.screen = gScreen
        self.state = None

    @abstractmethod
    def draw(self):
        pass