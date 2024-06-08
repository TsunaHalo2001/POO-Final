import pygame
import random
import math
from character import Character
from constants import eightySizeBrontoL, eightySizeBrontoM, eightySizeBrontoH, ratio23_21, ratio25_24, ratio23_24
from constants import eightySizeTrunk, ratio120_103
from constants import eightySizeTookeyL, eightySizeTookeyM, eightySizeTookeyH, ratio24_24, ratio24_23, ratio25_25
from constants import eightySizeTwizzyL, eightySizeTwizzyM, eightySizeTwizzyH, ratio24_24, ratio25_19, ratio24_23
from constants import eightySizeDrakooga, ratio24_15
from constants import eightySizePata, ratio16_16
from constants import eightySizeFireL, eightySizeFireM, eightySizeFireH, ratio48_29, ratio41_24, ratio40_28
from constants import eightySizeMarx, ratio78_42

class Enemy(Character):
    def __init__(self, gScreen, model, pPos=None):
        super().__init__(gScreen)

        self.model = model

        self.size = [None, None, None]
        if self.model == "bronto":
            self.size[0] = (int(self.screen.get_width()*eightySizeBrontoL), int(self.screen.get_width()*eightySizeBrontoL*ratio23_21))
            self.size[1] = (int(self.screen.get_width()*eightySizeBrontoM), int(self.screen.get_width()*eightySizeBrontoM*ratio25_24))
            self.size[2] = (int(self.screen.get_width()*eightySizeBrontoH), int(self.screen.get_width()*eightySizeBrontoH*ratio23_24))
            self.sprite.append(pygame.image.load('img/brontoLow.png'))
            self.sprite.append(pygame.image.load('img/brontoMid.png'))
            self.sprite.append(pygame.image.load('img/brontoHigh.png'))
            self.sprite[0] = pygame.transform.scale(self.sprite[0], self.size[0])
            self.sprite[1] = pygame.transform.scale(self.sprite[1], self.size[1])
            self.sprite[2] = pygame.transform.scale(self.sprite[2], self.size[2])
        if self.model == "trunk":
            self.size[0] = (int(self.screen.get_width()*eightySizeTrunk), int(self.screen.get_width()*eightySizeTrunk*ratio120_103))
            self.sprite.append(pygame.image.load('img/trunk.png'))
            self.sprite[0] = pygame.transform.scale(self.sprite[0], self.size[0])
        if self.model == "tookey":
            self.size[0] = (int(self.screen.get_width()*eightySizeTookeyL), int(self.screen.get_width()*eightySizeTookeyL*ratio24_24))
            self.size[1] = (int(self.screen.get_width()*eightySizeTookeyM), int(self.screen.get_width()*eightySizeTookeyM*ratio24_23))
            self.size[2] = (int(self.screen.get_width()*eightySizeTookeyH), int(self.screen.get_width()*eightySizeTookeyH*ratio25_25))
            self.sprite.append(pygame.image.load('img/tookeyLow.png'))
            self.sprite.append(pygame.image.load('img/tookeyMid.png'))
            self.sprite.append(pygame.image.load('img/tookeyHigh.png'))
            self.sprite[0] = pygame.transform.scale(self.sprite[0], self.size[0])
            self.sprite[1] = pygame.transform.scale(self.sprite[1], self.size[1])
            self.sprite[2] = pygame.transform.scale(self.sprite[2], self.size[2])
        if self.model == "twizzy":
            self.size[0] = (int(self.screen.get_width()*eightySizeTwizzyL), int(self.screen.get_width()*eightySizeTwizzyL*ratio24_24))
            self.size[1] = (int(self.screen.get_width()*eightySizeTwizzyM), int(self.screen.get_width()*eightySizeTwizzyM*ratio25_19))
            self.size[2] = (int(self.screen.get_width()*eightySizeTwizzyH), int(self.screen.get_width()*eightySizeTwizzyH*ratio24_23))
            self.sprite.append(pygame.image.load('img/twizzyLow.png'))
            self.sprite.append(pygame.image.load('img/twizzyMid.png'))
            self.sprite.append(pygame.image.load('img/twizzyHigh.png'))
            self.sprite[0] = pygame.transform.scale(self.sprite[0], self.size[0])
            self.sprite[1] = pygame.transform.scale(self.sprite[1], self.size[1])
            self.sprite[2] = pygame.transform.scale(self.sprite[2], self.size[2])
        if self.model == "drakooga":
            self.size[0] = (int(self.screen.get_width()*eightySizeDrakooga), int(self.screen.get_width()*eightySizeDrakooga*ratio24_15))
            self.size[1] = (int(self.screen.get_width()*eightySizeDrakooga), int(self.screen.get_width()*eightySizeDrakooga*ratio24_15))
            self.size[2] = (int(self.screen.get_width()*eightySizeDrakooga), int(self.screen.get_width()*eightySizeDrakooga*ratio24_15))
            self.sprite.append(pygame.image.load('img/drakoogaLow.png'))
            self.sprite.append(pygame.image.load('img/drakoogaMid.png'))
            self.sprite.append(pygame.image.load('img/drakoogaHigh.png'))
            self.sprite[0] = pygame.transform.scale(self.sprite[0], self.size[0])
            self.sprite[1] = pygame.transform.scale(self.sprite[1], self.size[1])
            self.sprite[2] = pygame.transform.scale(self.sprite[2], self.size[2])
        if self.model == "pata":
            self.size[0] = (int(self.screen.get_width()*eightySizePata), int(self.screen.get_width()*eightySizePata*ratio16_16))
            self.size[1] = (int(self.screen.get_width()*eightySizePata), int(self.screen.get_width()*eightySizePata*ratio16_16))
            self.size[2] = (int(self.screen.get_width()*eightySizePata), int(self.screen.get_width()*eightySizePata*ratio16_16))
            self.sprite.append(pygame.image.load('img/pataLow.png'))
            self.sprite.append(pygame.image.load('img/pataMid.png'))
            self.sprite.append(pygame.image.load('img/pataHigh.png'))
            self.sprite[0] = pygame.transform.scale(self.sprite[0], self.size[0])
            self.sprite[1] = pygame.transform.scale(self.sprite[1], self.size[1])
            self.sprite[2] = pygame.transform.scale(self.sprite[2], self.size[2])
        if self.model == "fire":
            self.size[0] = (int(self.screen.get_width()*eightySizeFireL), int(self.screen.get_width()*eightySizeFireL*ratio48_29))
            self.size[1] = (int(self.screen.get_width()*eightySizeFireM), int(self.screen.get_width()*eightySizeFireM*ratio41_24))
            self.size[2] = (int(self.screen.get_width()*eightySizeFireH), int(self.screen.get_width()*eightySizeFireH*ratio40_28))
            self.sprite.append(pygame.image.load('img/fireLow.png'))
            self.sprite.append(pygame.image.load('img/fireMid.png'))
            self.sprite.append(pygame.image.load('img/fireHigh.png'))
            self.sprite[0] = pygame.transform.scale(self.sprite[0], self.size[0])
            self.sprite[1] = pygame.transform.scale(self.sprite[1], self.size[1])
            self.sprite[2] = pygame.transform.scale(self.sprite[2], self.size[2])
        if self.model == "marx":
            self.size = [None, None, None, None]
            self.size[0] = (int(self.screen.get_width()*eightySizeMarx), int(self.screen.get_width()*eightySizeMarx*ratio78_42))
            self.size[1] = (int(self.screen.get_width()*eightySizeMarx), int(self.screen.get_width()*eightySizeMarx*ratio78_42))
            self.size[2] = (int(self.screen.get_width()*eightySizeMarx), int(self.screen.get_width()*eightySizeMarx*ratio78_42))
            self.size[3] = (int(self.screen.get_width()*eightySizeMarx), int(self.screen.get_width()*eightySizeMarx*ratio78_42))
            self.sprite.append(pygame.image.load('img/marx1.png'))
            self.sprite.append(pygame.image.load('img/marx2.png'))
            self.sprite.append(pygame.image.load('img/marx3.png'))
            self.sprite.append(pygame.image.load('img/marx4.png'))
            self.sprite[0] = pygame.transform.scale(self.sprite[0], self.size[0])
            self.sprite[1] = pygame.transform.scale(self.sprite[1], self.size[1])
            self.sprite[2] = pygame.transform.scale(self.sprite[2], self.size[2])
            self.sprite[3] = pygame.transform.scale(self.sprite[3], self.size[3])

        if self.model == "bronto":
            genPos = (self.screen.get_width(), random.randint(0, self.screen.get_height() / 2))
        if self.model == "trunk":
            genPos = (self.screen.get_width(), random.randint(int(self.screen.get_height() / 2), self.screen.get_height()))
        if self.model == "tookey":
            genPos = (self.screen.get_width(), random.randint(0, self.screen.get_height()))
        if self.model == "twizzy":
            genPos = (self.screen.get_width(), random.randint(0, self.screen.get_height()))
        if self.model == "drakooga":
            genPos = (self.screen.get_width(), random.randint(0, self.screen.get_height()))
        if self.model == "pata":
            genPos = (0, random.randint(0, self.screen.get_height()))
        if self.model == "fire":
            genPos = (self.screen.get_width(), random.randint(0, self.screen.get_height()))
        if self.model == "marx":
            genPos = (self.screen.get_width(), random.randint(int(self.screen.get_height() / 2), self.screen.get_height()))

        self.pos = pygame.Vector2(genPos)
        self.spawnPos = pygame.Vector2(genPos)
        self.mb = []
        if self.model == "drakooga":
            m = (self.pos.y - pPos.y) / (self.pos.x - pPos.x)
            b = self.pos.y - m * self.pos.x
            self.mb = [m, b]
        if self.model == "pata":
            m = (pPos.y - self.pos.y) / (pPos.x - self.pos.x)
            b = self.pos.y - m * self.pos.x
            self.mb = [m, b]

        self.state = 0

    def draw(self):
        if self.model == "bronto" or self.model == "tookey" or self.model == "twizzy" or self.model == "drakooga" or self.model == "pata" or self.model == "fire":
            if self.state == 0:
                self.screen.blit(self.sprite[0], self.pos)

            elif self.state == 1:
                self.screen.blit(self.sprite[1], self.pos)

            elif self.state == 2:
                self.screen.blit(self.sprite[2], self.pos)

            elif self.state == 3:
                self.screen.blit(self.sprite[1], self.pos)

        if self.model == "trunk":
            self.screen.blit(self.sprite[0], self.pos)

        if self.model == "marx":
            if self.state == 0:
                self.screen.blit(self.sprite[0], self.pos)
            if self.state == 1:
                self.screen.blit(self.sprite[1], self.pos)
            if self.state == 2:
                self.screen.blit(self.sprite[2], self.pos)
            if self.state == 3:
                self.screen.blit(self.sprite[3], self.pos)

    def move(self, speed):
        if not self.model == "pata":
            self.pos.x -= speed
            if self.model == "tookey":
                angleRad = math.radians(self.pos.x * 360 / self.screen.get_width())
                self.pos.y = int(self.spawnPos.y - math.sin(angleRad) * self.screen.get_height() / 4)
            if self.model == "twizzy":
                angleRad = math.radians(self.pos.x * 360 / self.screen.get_width()) + math.pi / 2
                self.pos.y = int(self.spawnPos.y - math.sin(angleRad) * self.screen.get_height() / 4)
            if self.model == "drakooga":
                self.pos.y = int(self.mb[0] * self.pos.x + self.mb[1])

        if self.model == "pata":
            self.pos.x += speed
            self.pos.y = int(self.mb[0] * self.pos.x + self.mb[1])

    def getHigherSize(self):
        if self.model == "bronto" or self.model == "tookey" or self.model == "twizzy" or self.model == "drakooga" or self.model == "pata":
            return 2
        if self.model == "trunk" or self.model == "fire" or self.model == "marx":
            return 0
        
    def getRect(self):
        if self.model == "bronto" or self.model == "tookey" or self.model == "twizzy" or self.model == "drakooga" or self.model == "pata" or self.model == "fire":
            if self.state == 0 or self.state == 3:
                return pygame.Rect(self.pos, self.size[0])
            if self.state == 1 or self.state == 2:
                return pygame.Rect(self.pos, self.size[self.state])
        if self.model == "trunk" or self.model == "marx":
            return pygame.Rect(self.pos, self.size[0])