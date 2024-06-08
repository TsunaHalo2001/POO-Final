import pygame
from character import Character
from constants import eightySize, ratio18_28, ratio19_28, ratio20_28, ratio21_28

class Player(Character):
    def __init__(self, gScreen):
        super().__init__(gScreen)

        self.size = [None, None, None, None, None]
        self.size[0] = (int(self.screen.get_width()*eightySize), int(self.screen.get_width()*eightySize*ratio18_28))
        self.size[1] = (int(self.screen.get_width()*eightySize), int(self.screen.get_width()*eightySize*ratio19_28))
        self.size[2] = (int(self.screen.get_width()*eightySize), int(self.screen.get_width()*eightySize*ratio18_28))
        self.size[3] = (int(self.screen.get_width()*eightySize), int(self.screen.get_width()*eightySize*ratio20_28))
        self.size[4] = (int(self.screen.get_width()*eightySize), int(self.screen.get_width()*eightySize*ratio21_28))

        self.pos = pygame.Vector2(self.screen.get_width() / 2 - self.size[0][0] / 2, self.screen.get_height() / 2 - self.size[0][1] / 2)

        self.oldPos = [self.pos.x, self.pos.y]

        self.state = "idle"
        
        self.tstate = 0
        
        self.sprite.append(pygame.image.load('img/idle.png'))
        self.sprite.append(pygame.image.load('img/up.png'))
        self.sprite.append(pygame.image.load('img/upper.png'))
        self.sprite.append(pygame.image.load('img/down1.png'))
        self.sprite.append(pygame.image.load('img/down2.png'))
        self.sprite[0] = pygame.transform.scale(self.sprite[0], self.size[0])
        self.sprite[1] = pygame.transform.scale(self.sprite[1], self.size[1])
        self.sprite[2] = pygame.transform.scale(self.sprite[2], self.size[2])
        self.sprite[3] = pygame.transform.scale(self.sprite[3], self.size[3])
        self.sprite[4] = pygame.transform.scale(self.sprite[4], self.size[4])

    def draw(self):
        if self.state == "idle":
            self.screen.blit(self.sprite[0], self.pos)
            self.tstate = 0

        elif self.state == "up":
            if self.tstate == 0:
                self.screen.blit(self.sprite[1], self.pos)

            elif self.tstate > 0:
                self.screen.blit(self.sprite[2], self.pos)

        elif self.state == "down":
            if self.tstate == 0:
                self.screen.blit(self.sprite[3], self.pos)

            elif self.tstate > 0:
                self.screen.blit(self.sprite[4], self.pos)

    def move(self, dt, keys):
        btController = True
        if not btController:
            if keys[pygame.K_w]:
                self.pos.y -= 300 * dt
            if keys[pygame.K_s]:
                self.pos.y += 300 * dt
        if btController:
            self.pos.y = 720 - (keys * 720 / 50)

        if self.pos.y < 0:
            self.pos.y = 0

        if self.pos.y > self.screen.get_height() - self.size[0][1]:
            self.pos.y = self.screen.get_height() - self.size[0][1]

        if self.pos.y > self.oldPos[1]:
            self.state = "down"

        elif self.pos.y < self.oldPos[1]:
            self.state = "up"

        elif self.pos.y == self.oldPos[1]:
            self.state = "idle"

    def getRect(self):
        return pygame.Rect(self.pos.x, self.pos.y, self.size[0][0], self.size[0][1])