import pygame
from pygame.locals import *

pygame.init()


class WindowVar:
    def __init__(self):
        self.clock = pygame.time.Clock()

        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.black = (0, 0, 0)
        self.skyBlue = (153, 217, 234)

        self.windowWidth = 1000
        self.windowHeight = 500
        self.fps = 30
        self.tileSize = 50
        self.coinSize = 25
        self.playerHeight = 50
        self.imageWidth = 30
        self.doorWidth = 45
        self.doorHeight = 90
        self.window = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        pygame.display.set_caption("Platformer")
        print('*** PLATFORMER ***')
        self.assets = {
            'deadPlayer': pygame.transform.scale(pygame.image.load("img/platformerAssets/deadPlayer.png"), (self.playerHeight, self.imageWidth)),
            'door': pygame.transform.scale(pygame.image.load("img/platformerAssets/door.png"), (self.doorWidth, self.doorHeight)),
            'gndTile': pygame.transform.scale(pygame.image.load("img/platformerAssets/gndTile.png"), (self.tileSize, self.tileSize)),
            'grassTile': pygame.transform.scale(pygame.image.load("img/platformerAssets/grassTile.png"), (self.tileSize, self.tileSize)),
            'lava': pygame.transform.scale(pygame.image.load("img/platformerAssets/lava.png"), (self.tileSize * 10, self.tileSize // 2)),
            'cloud': pygame.transform.scale(pygame.image.load("img/platformerAssets/cloud.png"), (150, 90)),
            'sun': pygame.transform.scale(pygame.image.load("img/platformerAssets/sun.png"), (self.tileSize, self.tileSize)),
            'coin': pygame.transform.scale(pygame.image.load("img/platformerAssets/coin.png"), (self.coinSize, self.coinSize)),
            'playerStanding': pygame.transform.scale(pygame.image.load("img/platformerAssets/standingnew.png"), (self.imageWidth, self.playerHeight)),
            'R1': pygame.transform.scale(pygame.image.load("img/platformerAssets/R1new.png"), (self.imageWidth, self.playerHeight)),
            'R2': pygame.transform.scale(pygame.image.load("img/platformerAssets/R2new.png"), (self.imageWidth, self.playerHeight)),
            'R3': pygame.transform.scale(pygame.image.load("img/platformerAssets/R3new.png"), (self.imageWidth, self.playerHeight)),
            'R4': pygame.transform.scale(pygame.image.load("img/platformerAssets/R4new.png"), (self.imageWidth, self.playerHeight)),
            'R5': pygame.transform.scale(pygame.image.load("img/platformerAssets/R5new.png"), (self.imageWidth, self.playerHeight)),
            'R6': pygame.transform.scale(pygame.image.load("img/platformerAssets/R6new.png"), (self.imageWidth, self.playerHeight)),
            'R7': pygame.transform.scale(pygame.image.load("img/platformerAssets/R7new.png"), (self.imageWidth, self.playerHeight)),
            'R8': pygame.transform.scale(pygame.image.load("img/platformerAssets/R8new.png"), (self.imageWidth, self.playerHeight)),
            'R9': pygame.transform.scale(pygame.image.load("img/platformerAssets/R9new.png"), (self.imageWidth, self.playerHeight)),
            'L1': pygame.transform.scale(pygame.image.load("img/platformerAssets/L1new.png"), (self.imageWidth, self.playerHeight)),
            'L2': pygame.transform.scale(pygame.image.load("img/platformerAssets/L2new.png"), (self.imageWidth, self.playerHeight)),
            'L3': pygame.transform.scale(pygame.image.load("img/platformerAssets/L3new.png"), (self.imageWidth, self.playerHeight)),
            'L4': pygame.transform.scale(pygame.image.load("img/platformerAssets/L4new.png"), (self.imageWidth, self.playerHeight)),
            'L5': pygame.transform.scale(pygame.image.load("img/platformerAssets/L5new.png"), (self.imageWidth, self.playerHeight)),
            'L6': pygame.transform.scale(pygame.image.load("img/platformerAssets/L6new.png"), (self.imageWidth, self.playerHeight)),
            'L7': pygame.transform.scale(pygame.image.load("img/platformerAssets/L7new.png"), (self.imageWidth, self.playerHeight)),
            'L8': pygame.transform.scale(pygame.image.load("img/platformerAssets/L8new.png"), (self.imageWidth, self.playerHeight)),
            'L9': pygame.transform.scale(pygame.image.load("img/platformerAssets/L9new.png"), (self.imageWidth, self.playerHeight)),
        }


class GameVar(WindowVar):
    def __init__(self):
        super().__init__()
        self.playerVel = 5
        self.jumpVel = 10

        self.isJump = 0
        self.left = 0
        self.right = 0
        self.walkCount = 0

        self.move = True
        self.standing = True

        self.score = 0

        self.run = True

        self.runRight = [self.assets['R1'], self.assets['R2'], self.assets['R3'],
                         self.assets['R4'], self.assets['R5'], self.assets['R6'],
                         self.assets['R7'], self.assets['R8'], self.assets['R9']]
        self.runLeft = [self.assets['L1'], self.assets['L2'], self.assets['L3'],
                        self.assets['L4'], self.assets['L5'], self.assets['L6'],
                        self.assets['L7'], self.assets['L8'], self.assets['L9']]

        self.playerRect = pygame.Rect(50, self.windowHeight - (2 * self.tileSize), self.playerHeight - 20, self.playerHeight)

        self.lavaRect = pygame.Rect((5 * self.tileSize, self.windowHeight - (2.5 * self.tileSize), self.tileSize * 10, self.tileSize // 2))

        self.tileRect = pygame.Rect(0, self.windowHeight - (2 * self.tileSize), self.tileSize, self.tileSize)
        self.endTileRect = pygame.Rect(self.windowWidth - self.tileSize, self.windowHeight - (5 * self.tileSize), self.tileSize, self.tileSize)

        self.startGrassRect1 = pygame.Rect(self.tileSize, self.windowHeight - self.tileSize, self.tileSize, self.tileSize)
        self.startGrassRect2 = pygame.Rect(2 * self.tileSize, self.windowHeight - self.tileSize, self.tileSize, self.tileSize)
        self.grassTileRect1 = pygame.Rect(3 * self.tileSize, self.windowHeight - (2 * self.tileSize), self.tileSize, self.tileSize)
        self.grassTileRect2 = pygame.Rect(4 * self.tileSize, self.windowHeight - (3 * self.tileSize), self.tileSize, self.tileSize)
        self.grassTileRect3 = pygame.Rect((6 * self.tileSize) + (self.tileSize // 2), self.windowHeight - (4 * self.tileSize) - (self.tileSize // 2), self.tileSize, self.tileSize)
        self.grassTileRect4 = pygame.Rect((9 * self.tileSize) + (self.tileSize // 2), self.windowHeight - (4 * self.tileSize) - (self.tileSize // 2), self.tileSize, self.tileSize)
        self.grassTileRect5 = pygame.Rect((12 * self.tileSize) + (self.tileSize // 2), self.windowHeight - (4 * self.tileSize) - (self.tileSize // 2), self.tileSize, self.tileSize)
        self.grassTileRect6 = pygame.Rect(self.windowWidth - (5 * self.tileSize), self.windowHeight - (3 * self.tileSize), self.tileSize, self.tileSize)
        self.grassTileRect7 = pygame.Rect(self.windowWidth - (4 * self.tileSize), self.windowHeight - (3 * self.tileSize), self.tileSize, self.tileSize)
        self.grassTileRect8 = pygame.Rect(self.windowWidth - (3 * self.tileSize), self.windowHeight - (4 * self.tileSize), self.tileSize, self.tileSize)
        self.grassTileRect9 = pygame.Rect(self.windowWidth - (2 * self.tileSize), self.windowHeight - (4 * self.tileSize), self.tileSize, self.tileSize)

        self.grassTileRectList = [self.startGrassRect1, self.startGrassRect2,
                                  self.grassTileRect1, self.grassTileRect2, self.grassTileRect3, self.grassTileRect4,
                                  self.grassTileRect5, self.grassTileRect6, self.grassTileRect7, self.grassTileRect8,
                                  self.grassTileRect9]

        self.nextLevelDoorRect = pygame.Rect(self.windowWidth - (1.5 * self.tileSize), self.windowHeight - (5.5 * self.tileSize), 0.5 * self.tileSize, 1.5 * self.tileSize)

        coinRect1 = pygame.Rect(self.grassTileRect3.x + (self.tileSize // 2) - (self.coinSize // 2), self.grassTileRect3.y - (self.coinSize + (self.coinSize // 2)), self.coinSize, self.coinSize)
        coinRect2 = pygame.Rect(self.grassTileRect4.x + (self.tileSize // 2) - (self.coinSize // 2), self.grassTileRect4.y - (self.coinSize + (self.coinSize // 2)), self.coinSize, self.coinSize)
        coinRect3 = pygame.Rect(self.grassTileRect5.x + (self.tileSize // 2) - (self.coinSize // 2), self.grassTileRect5.y - (self.coinSize + (self.coinSize // 2)), self.coinSize, self.coinSize)
        coinRect4 = pygame.Rect(self.grassTileRect3.x + (2 * self.tileSize) - (self.coinSize // 2), self.grassTileRect3.y - (3 * self.tileSize), self.coinSize, self.coinSize)
        coinRect5 = pygame.Rect(self.grassTileRect4.x + (2 * self.tileSize) - (self.coinSize // 2), self.grassTileRect3.y - (3 * self.tileSize), self.coinSize, self.coinSize)

        self.coinList = [coinRect1, coinRect2, coinRect3, coinRect4, coinRect5]

    def drawGrid(self):
        for i in range(0, self.windowWidth - self.tileSize + 1, 50):
            for j in range(0, self.windowHeight - self.tileSize + 1, 50):
                pygame.draw.rect(self.window, self.red, (i, j, self.tileSize, self.tileSize), 1)

        pygame.draw.rect(self.window, self.black, self.tileRect)
        pygame.draw.rect(self.window, self.black, self.endTileRect)

        for grassTileRect in self.grassTileRectList:
            pygame.draw.rect(self.window, self.green, grassTileRect)

        for coinRect in self.coinList:
            pygame.draw.rect(self.window, self.white, coinRect)

        pygame.draw.rect(self.window, self.blue, self.lavaRect)

    def drawCloudAndSun(self):
        self.window.blit(self.assets['sun'], (7 * self.tileSize, self.tileSize))
        self.window.blit(self.assets['cloud'], (150, 2 * self.tileSize))
        self.window.blit(self.assets['cloud'], (10 * self.tileSize, self.tileSize - 30))
        self.window.blit(self.assets['cloud'], (self.windowWidth - (4 * self.tileSize), self.tileSize))

    def playerMove(self):
        keys = pygame.key.get_pressed()

        if self.move:
            if keys[pygame.K_LEFT]:
                self.playerRect.x -= self.playerVel
                self.left = 1
                self.right = 0
                self.standing = False
            elif keys[pygame.K_RIGHT]:
                self.playerRect.x += self.playerVel
                self.left = 0
                self.right = 1
                self.standing = False
            else:
                self.standing = True
                self.walkCount = 0

            if self.isJump == 0:
                if keys[pygame.K_UP]:
                    self.isJump = 1
            if self.isJump == 1:
                neg = 1
                add = 0
                if self.jumpVel >= -10:
                    if self.jumpVel < 0:
                        neg = -1
                    if self.jumpVel == -10:
                        add = 5
                    self.playerRect.y -= (((self.jumpVel ** 2) * 0.5) + add) * neg
                    self.jumpVel -= 1
                else:
                    self.isJump = 0
                    self.jumpVel = 10

        if self.playerRect.left < self.tileRect.right:
            self.playerRect.x += self.playerVel
        if self.playerRect.bottomright == self.grassTileRect1.bottomleft:
            self.playerRect.x -= self.playerVel
        if self.playerRect.bottomright == self.grassTileRect2.bottomleft:
            self.playerRect.x -= self.playerVel
        if self.playerRect.bottomright == self.grassTileRect8.bottomleft:
            self.playerRect.x -= self.playerVel
        if self.playerRect.right > self.endTileRect.left:
            self.playerRect.x -= self.playerVel

        for grassTile in self.grassTileRectList:
            if self.playerRect.colliderect(grassTile):
                self.playerRect.y = grassTile.y - self.playerHeight

        if self.isJump == 0:
            if self.playerRect.right < self.grassTileRect1.left:
                self.playerRect.y = self.startGrassRect1.y - self.playerHeight
            elif self.grassTileRect1.left < self.playerRect.right < self.grassTileRect2.left:
                self.playerRect.y = self.grassTileRect1.y - self.playerHeight
            elif self.grassTileRect1.right < self.playerRect.left < self.grassTileRect2.right:
                self.playerRect.y = self.grassTileRect2.y - self.playerHeight
            elif self.grassTileRect2.right < self.playerRect.left and self.playerRect.right < self.grassTileRect3.left:
                self.playerRect.y = self.lavaRect.y - (self.playerHeight // 2)
            elif self.grassTileRect3.right < self.playerRect.left and self.playerRect.right < self.grassTileRect4.left:
                self.playerRect.y = self.lavaRect.y - (self.playerHeight // 2)
            elif self.grassTileRect4.right < self.playerRect.left and self.playerRect.right < self.grassTileRect5.left:
                self.playerRect.y = self.lavaRect.y - (self.playerHeight // 2)
            elif self.grassTileRect5.right < self.playerRect.left and self.playerRect.right < self.grassTileRect6.left:
                self.playerRect.y = self.lavaRect.y - (self.playerHeight // 2)
            elif self.grassTileRect6.left < self.playerRect.right < self.grassTileRect8.left:
                self.playerRect.y = self.grassTileRect6.y - self.playerHeight
            elif self.grassTileRect8.left < self.playerRect.right:
                self.playerRect.y = self.grassTileRect8.y - self.playerHeight

        if self.playerRect.colliderect(self.lavaRect):
            self.move = False
            self.standing = False
            self.right = 0
            self.left = 0

        # pygame.draw.rect(window, blue, playerRect, 1)

    def drawPlayer(self):
        if not self.standing:
            if self.right == 1:
                if self.walkCount >= 3 * len(self.runRight):
                    self.walkCount = 0
                self.window.blit(self.runRight[self.walkCount // 3], self.playerRect)
                self.walkCount += 1
            elif self.left == 1:
                if self.walkCount >= 3 * len(self.runLeft):
                    self.walkCount = 0
                self.window.blit(self.runLeft[self.walkCount // 3], self.playerRect)
                self.walkCount += 1
            if not self.move:
                self.window.blit(self.assets['deadPlayer'], (self.playerRect.x, self.playerRect.y))
        else:
            if self.right == 1:
                self.window.blit(self.assets['R1'], self.playerRect)
            elif self.left == 1:
                self.window.blit(self.assets['L1'], self.playerRect)
            elif self.standing:
                self.window.blit(self.assets['playerStanding'], self.playerRect)

    def updateScore(self):
        for coinRect in self.coinList:
            if self.playerRect.colliderect(coinRect):
                self.coinList.pop(self.coinList.index(coinRect))
                self.score += 10

    def showScore(self):
        print("Score: ", self.score)

    def drawCoin(self):
        for coinRect in self.coinList:
            self.window.blit(self.assets['coin'], coinRect)

    def drawTile(self):
        for i in range(0, self.windowWidth - self.tileSize + 1, 50):
            if i == 0 or i == self.windowWidth - self.tileSize:
                for j in range(0, self.windowHeight - self.tileSize + 1, 50):
                    self.window.blit(self.assets['gndTile'], (i, j))
            elif i == self.tileSize or i == 2 * self.tileSize:
                self.window.blit(self.assets['grassTile'], (i, self.windowHeight - self.tileSize))
            elif i == 3 * self.tileSize:
                self.window.blit(self.assets['grassTile'], (i, self.windowHeight - (2 * self.tileSize)))
                self.window.blit(self.assets['gndTile'], (i, self.windowHeight - self.tileSize))
            elif i == 4 * self.tileSize:
                self.window.blit(self.assets['grassTile'], (i, self.windowHeight - (3 * self.tileSize)))
                self.window.blit(self.assets['gndTile'], (i, self.windowHeight - self.tileSize))
                self.window.blit(self.assets['gndTile'], (i, self.windowHeight - (2 * self.tileSize)))
            elif i == 5 * self.tileSize:
                self.window.blit(self.assets['lava'], (i, self.windowHeight - (2.5 * self.tileSize)))
                self.window.blit(self.assets['gndTile'], (i, self.windowHeight - self.tileSize))
                self.window.blit(self.assets['gndTile'], (i, self.windowHeight - (2 * self.tileSize)))
            elif i == 6 * self.tileSize:
                self.window.blit(self.assets['grassTile'], (i + (self.tileSize // 2), self.windowHeight - (4 * self.tileSize) - (self.tileSize // 2)))
                self.window.blit(self.assets['gndTile'], (i, self.windowHeight - self.tileSize))
                self.window.blit(self.assets['gndTile'], (i, self.windowHeight - (2 * self.tileSize)))
            elif i == 9 * self.tileSize:
                self.window.blit(self.assets['grassTile'], (i + (self.tileSize // 2), self.windowHeight - (4 * self.tileSize) - (self.tileSize // 2)))
                self.window.blit(self.assets['gndTile'], (i, self.windowHeight - self.tileSize))
                self.window.blit(self.assets['gndTile'], (i, self.windowHeight - (2 * self.tileSize)))
            elif i == 12 * self.tileSize:
                self.window.blit(self.assets['grassTile'], (i + (self.tileSize // 2), self.windowHeight - (4 * self.tileSize) - (self.tileSize // 2)))
                self.window.blit(self.assets['gndTile'], (i, self.windowHeight - self.tileSize))
                self.window.blit(self.assets['gndTile'], (i, self.windowHeight - (2 * self.tileSize)))
            elif i == self.windowWidth - (2 * self.tileSize) or i == self.windowWidth - (3 * self.tileSize):
                self.window.blit(self.assets['grassTile'], (i, self.windowHeight - (4 * self.tileSize)))
                self.window.blit(self.assets['gndTile'], (i, self.windowHeight - self.tileSize))
                self.window.blit(self.assets['gndTile'], (i, self.windowHeight - (2 * self.tileSize)))
                self.window.blit(self.assets['gndTile'], (i, self.windowHeight - (3 * self.tileSize)))
            elif i == self.windowWidth - (4 * self.tileSize) or i == self.windowWidth - (5 * self.tileSize):
                self.window.blit(self.assets['grassTile'], (i, self.windowHeight - (3 * self.tileSize)))
                self.window.blit(self.assets['gndTile'], (i, self.windowHeight - self.tileSize))
                self.window.blit(self.assets['gndTile'], (i, self.windowHeight - (2 * self.tileSize)))
            else:
                self.window.blit(self.assets['gndTile'], (i, self.windowHeight - self.tileSize))
                self.window.blit(self.assets['gndTile'], (i, self.windowHeight - (2 * self.tileSize)))

    def nextLevel(self):
        self.window.blit(self.assets['door'], (self.windowWidth - (2 * self.tileSize) + 6, self.windowHeight - (6 * self.tileSize) + 14))
        if self.playerRect.colliderect(self.nextLevelDoorRect):
            self.run = False
            self.showScore()

    def drawGameWindow(self):
        self.window.fill(self.skyBlue)
        self.drawCloudAndSun()
        self.drawCoin()
        self.playerMove()
        self.nextLevel()
        self.updateScore()
        self.drawPlayer()
        self.drawTile()
        # drawGrid()

    def gameLoop(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == KEYDOWN and (event.key == K_ESCAPE):
                    self.run = False

            self.drawGameWindow()

            pygame.display.update()
            self.clock.tick(self.fps)

        pygame.quit()


game = GameVar()

game.gameLoop()
