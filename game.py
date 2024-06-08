import pygame
import math
import random
from constants import ratio05
from gameentity import GameEntity
from player import Player
from enemy import Enemy

class Game(GameEntity):
    def __init__(self, gScreen):
        super().__init__(gScreen)
        self.doubleScreen = (self.screen.get_width() * 2, self.screen.get_height() * 2)
        self.twoThirdsScreen = (int(self.screen.get_width() * 2 / 3), int(self.screen.get_height() * 2 / 3))

        self.bgSpeed = self.screen.get_width() * ratio05

        self.keys = None
        self.tcount = 0
        self.animCount = 0
        self.difficulty = 45

        self.transitionFlag = False
        self.musicFlag = True
        self.difficultyFlag = True
        self.deathFlag = False
        self.exitTransition = False

        self.state = 1
        self.score = 0

        # Load the self.background image (replace 'self.background.jpg' with your image file)
        self.background = []
        self.background_x = []
        self.background.append(pygame.image.load('img/bg1.jpg'))
        self.background.append(pygame.image.load('img/bg2.jpg'))
        self.background.append(pygame.image.load('img/bg3.jpg'))
        self.background.append(pygame.image.load('img/bg4.jpg'))
        self.background.append(pygame.image.load('img/bg4.jpg'))
        for i in range(len(self.background)):
            self.background[i] = pygame.transform.scale(self.background[i], (self.doubleScreen[0], self.doubleScreen[0]))
            self.background_x.append(0)
        self.background.append(pygame.image.load('img/died.jpg'))
        self.background[5] = pygame.transform.scale(self.background[5], (self.screen.get_width(), self.screen.get_height()))
        self.background.append(pygame.image.load('img/main1.jpg'))
        self.background[6] = pygame.transform.scale(self.background[6], (self.screen.get_width(), self.screen.get_height()))
        self.background.append(pygame.image.load('img/main2.jpg'))
        self.background[7] = pygame.transform.scale(self.background[7], (self.screen.get_width(), self.screen.get_height()))
        self.background.append(pygame.image.load('img/bt.jpg'))
        self.background[8] = pygame.transform.scale(self.background[8], (self.screen.get_width(), self.screen.get_height()))
        self.background_x[4] = self.doubleScreen[0] + 1

        self.bgColors = []
        self.bgColors_x = []
        self.bgColors.append(pygame.image.load('img/bgGreenArrow1.png'))
        self.bgColors.append(pygame.image.load('img/bgGreenArrow2.png'))
        self.bgColors.append(pygame.image.load('img/bgBlueArrow1.png'))
        self.bgColors.append(pygame.image.load('img/bgBlueArrow2.png'))
        self.bgColors.append(pygame.image.load('img/bgBlackArrow1.png'))
        self.bgColors.append(pygame.image.load('img/bgBlackArrow2.png'))
        self.bgColors[0] = pygame.transform.scale(self.bgColors[0], (self.screen.get_width() * 1.1, self.screen.get_height() * 1.1))
        self.bgColors[1] = pygame.transform.scale(self.bgColors[1], (self.screen.get_width() * 2, self.screen.get_height()))
        self.bgColors[2] = pygame.transform.scale(self.bgColors[2], (self.screen.get_width() * 1.1, self.screen.get_height() * 1.1))
        self.bgColors[3] = pygame.transform.scale(self.bgColors[3], (self.screen.get_width() * 2, self.screen.get_height()))
        self.bgColors[4] = pygame.transform.scale(self.bgColors[4], (self.screen.get_width() * 1.1, self.screen.get_height() * 1.1))
        self.bgColors[5] = pygame.transform.scale(self.bgColors[5], (self.screen.get_width() * 2, self.screen.get_height()))
        self.bgColors_x.append(self.screen.get_width())
        self.bgColors_x.append(0)
        self.bgColors_x.append(self.screen.get_width())
        self.bgColors_x.append(0)
        self.bgColors_x.append(self.screen.get_width())
        self.bgColors_x.append(0)

        self.bgTransition = [[],[],[],[]]
        self.bgTransition[0].append(pygame.image.load('img/bg11.jpg'))
        self.bgTransition[0].append(pygame.image.load('img/bg12.jpg'))
        self.bgTransition[0].append(pygame.image.load('img/bg13.jpg'))
        self.bgTransition[0].append(pygame.image.load('img/bg14.jpg'))
        self.bgTransition[1].append(pygame.image.load('img/bg21.jpg'))
        self.bgTransition[1].append(pygame.image.load('img/bg22.jpg'))
        self.bgTransition[1].append(pygame.image.load('img/bg23.jpg'))
        self.bgTransition[1].append(pygame.image.load('img/bg24.jpg'))
        self.bgTransition[2].append(pygame.image.load('img/bg31.jpg'))
        self.bgTransition[2].append(pygame.image.load('img/bg32.jpg'))
        self.bgTransition[2].append(pygame.image.load('img/bg33.jpg'))
        self.bgTransition[2].append(pygame.image.load('img/bg34.jpg'))
        for i in range(len(self.bgTransition[0])):
            self.bgTransition[0][i] = pygame.transform.scale(self.bgTransition[0][i], (self.screen.get_width(), self.screen.get_height()))
        for i in range(len(self.bgTransition[1])):
            self.bgTransition[1][i] = pygame.transform.scale(self.bgTransition[1][i], (self.screen.get_width(), self.screen.get_height()))
        for i in range(len(self.bgTransition[2])):
            self.bgTransition[2][i] = pygame.transform.scale(self.bgTransition[2][i], (self.screen.get_width(), self.screen.get_height()))\
            
        self.player1 = Player(self.screen)

        self.enemies = []

    def draw(self, btController):
        if self.state == 1:
            if self.musicFlag:
                pygame.mixer.music.load('bgm/00.mp3')
                pygame.mixer.music.play(0)
                self.musicFlag = False
            if btController:
                self.screen.blit(self.background[6], (0, 0))
            if not btController:
                self.screen.blit(self.background[7], (0, 0))

        if self.state == 0:
            if btController:
                if self.score == 40:
                    self.transitionFlag = True

                    if not self.exitTransition and self.transitionFlag:
                        if self.tcount <= 30 and self.bgColors_x[0] >= -self.screen.get_width():
                            self.bgColors_x[0] -= self.screen.get_width() / 15
                            self.screen.blit(self.bgColors[0], (int(self.bgColors_x[0]), -int(self.screen.get_width() * 0.1)))

                        if self.bgColors_x[0] < -self.screen.get_width() and self.animCount == 0:
                            if self.tcount == 30:
                                self.screen.blit(self.bgTransition[0][0], (0, 0))
                            if self.tcount == 45:
                                self.screen.blit(self.bgTransition[0][1], (0, 0))
                            if self.tcount == 60:
                                self.screen.blit(self.bgTransition[0][2], (0, 0))
                            if self.tcount == 15:
                                self.screen.blit(self.bgTransition[0][3], (0, 0))
                                self.animCount = 1

                        if self.animCount == 1:
                            if self.keys[pygame.K_SPACE]:
                                self.transitionFlag = False
                                self.exitTransition = True
                                self.animCount = 0

                    if self.exitTransition:
                        if self.tcount <= 60 and self.bgColors_x[1] >= -self.screen.get_width() * 2:
                            self.bgColors_x[1] -= self.screen.get_width() / 7.5

                            self.screen.blit(self.background[1], (int(self.background_x[1]), -self.screen.get_width()))
                            self.screen.blit(self.bgColors[1], (int(self.bgColors_x[1]), 0))

                        if self.bgColors_x[1] < -self.screen.get_width() * 2:
                            self.exitTransition = False
                            self.transitionFlag = False
                            self.musicFlag = True
                            self.score += 1

                if self.score == 80:
                    self.transitionFlag = True

                    if not self.exitTransition and self.transitionFlag:
                        if self.tcount <= 30 and self.bgColors_x[2] >= -self.screen.get_width():
                            self.bgColors_x[2] -= self.screen.get_width() / 15
                            self.screen.blit(self.bgColors[2], (int(self.bgColors_x[2]), -int(self.screen.get_width() * 0.1)))

                        if self.bgColors_x[2] < -self.screen.get_width() and self.animCount == 0:
                            if self.tcount == 30:
                                self.screen.blit(self.bgTransition[1][0], (0, 0))
                            if self.tcount == 45:
                                self.screen.blit(self.bgTransition[1][1], (0, 0))
                            if self.tcount == 60:
                                self.screen.blit(self.bgTransition[1][2], (0, 0))
                            if self.tcount == 15:
                                self.screen.blit(self.bgTransition[1][3], (0, 0))
                                self.animCount = 1

                        if self.animCount == 1:
                            if self.keys[pygame.K_SPACE]:
                                self.transitionFlag = False
                                self.exitTransition = True
                                self.animCount = 0

                    if self.exitTransition:
                        if self.tcount <= 60 and self.bgColors_x[3] >= -self.screen.get_width() * 2:
                            self.bgColors_x[3] -= self.screen.get_width() / 7.5

                            self.screen.blit(self.background[2], (int(self.background_x[2]), -self.twoThirdsScreen[1]))
                            self.screen.blit(self.bgColors[3], (int(self.bgColors_x[3]), 0))

                        if self.bgColors_x[3] < -self.screen.get_width() * 2:
                            self.exitTransition = False
                            self.transitionFlag = False
                            self.musicFlag = True
                            self.score += 1

                if self.score == 120:
                    self.transitionFlag = True

                    if not self.exitTransition and self.transitionFlag:
                        if self.tcount <= 30 and self.bgColors_x[4] >= -self.screen.get_width():
                            self.bgColors_x[4] -= self.screen.get_width() / 15
                            self.screen.blit(self.bgColors[4], (int(self.bgColors_x[4]), -int(self.screen.get_width() * 0.1)))

                        if self.bgColors_x[4] < -self.screen.get_width() and self.animCount == 0:
                            if self.tcount == 30:
                                self.screen.blit(self.bgTransition[2][0], (0, 0))
                            if self.tcount == 45:
                                self.screen.blit(self.bgTransition[2][1], (0, 0))
                            if self.tcount == 60:
                                self.screen.blit(self.bgTransition[2][2], (0, 0))
                            if self.tcount == 15:
                                self.screen.blit(self.bgTransition[2][3], (0, 0))
                                self.animCount = 1

                        if self.animCount == 1:
                            if self.keys[pygame.K_SPACE]:
                                self.transitionFlag = False
                                self.exitTransition = True
                                self.animCount = 0

                    if self.exitTransition:
                        if self.tcount <= 60 and self.bgColors_x[5] >= -self.screen.get_width() * 2:
                            self.bgColors_x[5] -= self.screen.get_width() / 7.5

                            self.screen.blit(self.background[3], (int(self.background_x[3]), -self.twoThirdsScreen[1]))
                            self.screen.blit(self.bgColors[5], (int(self.bgColors_x[5]), 0))

                        if self.bgColors_x[5] < -self.screen.get_width() * 2:
                            self.exitTransition = False
                            self.transitionFlag = False
                            self.musicFlag = True
                            self.score += 1

                if not self.transitionFlag:
                    if self.score < 40:
                        if self.musicFlag:
                            pygame.mixer.music.load('bgm/01.mp3')
                            pygame.mixer.music.play(-1)
                            self.musicFlag = False
                        self.background_x[0] -= self.bgSpeed

                        self.screen.blit(self.background[0], (int(self.background_x[0]), -self.screen.get_width()))

                    if self.score > 40 and self.score < 80:
                        if self.musicFlag:
                            pygame.mixer.music.load('bgm/02.mp3')
                            pygame.mixer.music.play(-1)
                            self.musicFlag = False
                        self.background_x[1] -= self.bgSpeed

                        self.screen.blit(self.background[1], (int(self.background_x[1]), -self.screen.get_width()))

                    if self.score > 80 and self.score < 120:
                        if self.musicFlag:
                            pygame.mixer.music.load('bgm/03.mp3')
                            pygame.mixer.music.play(-1)
                            self.musicFlag = False
                            self.difficulty = 30
                        self.background_x[2] -= self.bgSpeed

                        self.screen.blit(self.background[2], (int(self.background_x[2]), -self.twoThirdsScreen[1]))

                    if self.score > 120:
                        if self.musicFlag:
                            pygame.mixer.music.load('bgm/04.mp3')
                            pygame.mixer.music.play(-1)
                            self.musicFlag = False
                            self.difficulty = 15

                        if self.difficulty > 1:
                            if self.score % 20 == 0 and self.difficultyFlag:
                                self.difficulty -= 1
                                self.difficultyFlag = False

                            if self.score % 20 != 0:
                                self.difficultyFlag = True

                        self.background_x[3] -= self.bgSpeed
                        self.background_x[4] -= self.bgSpeed

                        if self.background_x[3] < -self.doubleScreen[0]:
                            self.background_x[3] = self.doubleScreen[0]

                        if self.background_x[4] < -self.doubleScreen[0]:
                            self.background_x[4] = self.doubleScreen[0]

                        self.screen.blit(self.background[3], (int(self.background_x[3]), -self.twoThirdsScreen[1]))
                        self.screen.blit(self.background[4], (int(self.background_x[4]), -self.twoThirdsScreen[1]))

                    if not self.score == 40 and not self.score == 80 and not self.score == 120:
                        self.player1.draw()

                        if len(self.enemies) > 0:
                            for i in range(len(self.enemies)):
                                self.enemies[i].draw()
                                if self.tcount % 15 == 0:
                                    self.enemies[i].state += 1
                                    if self.enemies[i].state > 3:
                                        self.enemies[i].state = 0

            if not btController:
                self.screen.blit(self.background[8], (0, 0))

        if self.state == 2:
            if self.musicFlag:
                pygame.mixer.music.load('bgm/05.mp3')
                pygame.mixer.music.play(0)
                self.musicFlag = False
            self.screen.blit(self.background[5], (0, 0))
            font = pygame.font.Font('freesansbold.ttf', 36)
            text = font.render('Score: ' + str(self.score), True, (255, 255, 255))
            self.screen.blit(text, (0, 0))

    def update(self, dt, btinput):
        self.player1.oldPos = [self.player1.pos.x, self.player1.pos.y]
        self.keys = pygame.key.get_pressed()
        if self.state == 1:
            if self.keys[pygame.K_SPACE] and not self.deathFlag:
                self.state = 0
                self.musicFlag = True
            if not self.keys[pygame.K_SPACE]:
                self.deathFlag = False
        if self.state == 2:
            if self.keys[pygame.K_SPACE]:
                self.state = 1
                self.musicFlag = True
                self.score = 0
                self.deathFlag = True
                self.enemies.clear()
        if self.state == 0:
            if btinput == "":
                self.keys = 0
            if not self.transitionFlag and not btinput == "":
                print("btinput: ", btinput)
                self.keys = int(btinput)
            if not self.transitionFlag:
                self.player1.move(dt, self.keys)
                
                enemySpeed = int(3.0412 * math.e ** (0.0072 * (self.score + dt * self.tcount)))
                if len(self.enemies) > 0:
                    for i in range(len(self.enemies)):
                        self.enemies[i].move(enemySpeed)
                        if not self.enemies[i].model == "pata":
                            if self.enemies[i].pos.x < -self.enemies[i].size[self.enemies[i].getHigherSize()][0]:
                                self.enemies.pop(i)
                                break
                        if self.enemies[i].model == "pata":
                            if self.enemies[i].pos.x > self.screen.get_width():
                                self.enemies.pop(i)
                                break

                enemySpawnRate = 7 * math.e ** (-0.022 * (self.score + dt * self.tcount))
                enemySpawnRateAux = (enemySpawnRate - int(enemySpawnRate)) * 60

                coin = random.randint(0, 1)
                isTrunk = False
                for enemy in self.enemies:
                    if enemy.model == "trunk":
                        isTrunk = True

                if self.score != 0:
                    if int(enemySpawnRate) > 0:
                        if self.score % int(enemySpawnRate) == 0:
                            if self.tcount == int(enemySpawnRateAux):
                                if self.score < 40:
                                    if coin == 0 or isTrunk:
                                        self.enemies.append(Enemy(self.screen, "bronto"))
                                    elif coin == 1:
                                        self.enemies.append(Enemy(self.screen, "trunk"))

                                if self.score > 40 and self.score < 80:
                                    if coin == 0:
                                        self.enemies.append(Enemy(self.screen, "tookey"))
                                    if coin == 1:
                                        self.enemies.append(Enemy(self.screen, "twizzy"))

                                if self.score > 80 and self.score < 120:
                                    if coin == 0:
                                        self.enemies.append(Enemy(self.screen, "drakooga", self.player1.pos))
                                    if coin == 1:
                                        self.enemies.append(Enemy(self.screen, "pata", self.player1.pos))

                                if self.score > 120:
                                    if coin == 0:
                                        self.enemies.append(Enemy(self.screen, "fire"))
                                    if coin == 1:
                                        self.enemies.append(Enemy(self.screen, "marx"))

                    elif int(enemySpawnRate) == 0:
                        if self.tcount != 0:
                            if self.tcount % self.difficulty == 0:
                                if self.score < 40:
                                    if coin == 0 or isTrunk:
                                        self.enemies.append(Enemy(self.screen, "bronto"))
                                    elif coin == 1:
                                        self.enemies.append(Enemy(self.screen, "trunk"))

                                if self.score > 40 and self.score < 80:
                                    if coin == 0:
                                        self.enemies.append(Enemy(self.screen, "tookey"))
                                    if coin == 1:
                                        self.enemies.append(Enemy(self.screen, "twizzy"))

                                if self.score > 80 and self.score < 120:
                                    if coin == 0:
                                        self.enemies.append(Enemy(self.screen, "drakooga", self.player1.pos))
                                    if coin == 1:
                                        self.enemies.append(Enemy(self.screen, "pata", self.player1.pos))

                                if self.score > 120:
                                    if coin == 0:
                                        self.enemies.append(Enemy(self.screen, "fire"))
                                    if coin == 1:
                                        self.enemies.append(Enemy(self.screen, "marx"))

    def conts(self, btController):
        if self.state == 0:
            if btController:
                self.tcount += 1

                if self.tcount % 30 == 0 and not self.transitionFlag:
                    self.player1.tstate += 1

                if self.tcount % 60 == 0:
                    if not self.transitionFlag:
                        print("Score: ", self.score)
                        self.score += 1
                    self.tcount = 0
            if not btController:
                pass

    def checkCollisions(self):
        if len(self.enemies) > 0:
            for i in range(len(self.enemies)):
                if pygame.Rect.colliderect(self.player1.getRect(), self.enemies[i].getRect()):
                    self.tcount = 0
                    self.state = 2
                    self.musicFlag = True
                    self.enemies.clear()
                    break