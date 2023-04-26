import pygame
from pygame.locals import *

pygame.init()


class Level2:
    def __init__(self):
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.black = (0, 0, 0)
        self.skyBlue = (153, 217, 234)

        self.run = True
        self.clock = pygame.time.Clock()
        self.fps = 30
        self.windowWidth = 1000
        self.windowHeight = 500

        self.window = pygame.display.set_mode((self.windowWidth, self.windowHeight))

        self.tileWidth = 50
        self.tileHeight = 50
        self.playerWidth = 30
        self.coinSize = 25
        self.playerHeight = 50
        self.doorWidth = 45
        self.doorHeight = 90

        self.score = 0

        self.enemyWidth = 50
        self.enemyHeight = 30
        self.enemyVel = 1
        self.enemy1MoveRight = 0
        self.enemy1MoveLeft = 0
        self.enemy2MoveRight = 0
        self.enemy2MoveLeft = 0
        self.enemyWalkCount = 0
        self.enemyRect1 = pygame.Rect(self.windowWidth // 2, self.windowHeight - (1.6 * self.tileHeight), self.enemyWidth, self.enemyHeight)
        self.enemyRect2 = pygame.Rect(250, self.windowHeight - (4.6 * self.tileHeight), self.enemyWidth, self.enemyHeight)

        self.playerRect = pygame.Rect(0, self.windowHeight - (2 * self.tileHeight), self.playerWidth, self.playerHeight)
        self.walkCount = 0
        self.playerVel = 3
        self.moveLeft = 0
        self.moveRight = 0
        self.jumpCount = 10
        self.isJump = 0

        self.stop = 0
        self.enemy1Died = 0
        self.enemy2Died = 0

        self.coin1 = pygame.Rect(self.windowWidth - (1 * self.tileWidth), self.windowHeight - (2 * self.tileHeight), self.coinSize, self.coinSize)
        self.coin2 = pygame.Rect(self.windowWidth - (3 * self.tileWidth), self.windowHeight - (2 * self.tileHeight), self.coinSize, self.coinSize)
        self.coin3 = pygame.Rect(self.windowWidth - (5 * self.tileWidth), self.windowHeight - (2 * self.tileHeight), self.coinSize, self.coinSize)
        self.coin4 = pygame.Rect(10, self.windowHeight - (5 * self.tileHeight), self.coinSize, self.coinSize)
        self.coin5 = pygame.Rect(110, self.windowHeight - (5 * self.tileHeight), self.coinSize, self.coinSize)
        self.coin6 = pygame.Rect(210, self.windowHeight - (5 * self.tileHeight), self.coinSize, self.coinSize)
        self.coin7 = pygame.Rect(60, self.windowHeight - (8 * self.tileHeight), self.coinSize, self.coinSize)
        self.coin8 = pygame.Rect(160, self.windowHeight - (8 * self.tileHeight), self.coinSize, self.coinSize)
        self.coin9 = pygame.Rect(self.windowWidth - (5 * self.tileWidth), self.windowHeight - (7 * self.tileHeight), self.coinSize, self.coinSize)
        self.coin10 = pygame.Rect(self.windowWidth - (8 * self.tileWidth), self.windowHeight - (7 * self.tileHeight), self.coinSize, self.coinSize)

        self.grassRect1 = pygame.Rect(self.windowWidth // 2 - (1 * self.tileWidth), self.windowHeight - (4 * self.tileHeight), self.tileWidth, self.tileHeight)
        self.grassRect2 = pygame.Rect(self.windowWidth // 2 + (1 * self.tileWidth), self.windowHeight - (6 * self.tileHeight), self.tileWidth, self.tileHeight)
        self.grassRect3 = pygame.Rect(200, self.windowHeight - (7 * self.tileHeight), self.tileWidth, self.tileHeight)
        self.grassRect4 = pygame.Rect(self.windowWidth - (3 * self.tileWidth), self.windowHeight - (8 * self.tileHeight), self.tileWidth, self.tileHeight)
        self.grassRect5 = pygame.Rect(self.windowWidth - (3 * self.tileWidth), 3 * self.tileHeight, self.tileWidth, self.tileHeight)

        self.bulletWidth = 10
        self.bulletHeight = 5
        self.bulletVel = 25
        self.shoot = 0
        self.bulletMoveRight = 0
        self.bulletMoveLeft = 0
        self.bullet = pygame.Rect(self.playerRect.x + (self.playerWidth // 2), self.playerRect.y + (self.playerHeight // 2), self.bulletWidth, self.bulletHeight)

        self.doorRect = pygame.Rect(self.windowWidth - self.doorWidth, 10, self.doorWidth, self.doorHeight)

        self.assets = {
            'door': pygame.transform.scale(pygame.image.load("img/platformerAssets/door.png"), (self.doorWidth, self.doorHeight)),
            'gndTile': pygame.transform.scale(pygame.image.load("img/platformerAssets/gndTile.png"), (self.tileWidth, self.tileHeight)),
            'grassTile': pygame.transform.scale(pygame.image.load("img/platformerAssets/grassTile.png"), (self.tileWidth, self.tileHeight)),
            'cloud': pygame.transform.scale(pygame.image.load("img/platformerAssets/cloud.png"), (150, 90)),
            'deadEnemy': pygame.transform.scale(pygame.image.load("img/platformerAssets/deadEnemy.png"), (self.enemyWidth, self.enemyHeight)),
            'deadPlayer': pygame.transform.scale(pygame.image.load("img/platformerAssets/deadPlayer.png"), (self.playerHeight, self.playerWidth)),
            'enemyRight1': pygame.transform.scale(pygame.image.load("img/platformerAssets/enemyRight1.png"), (self.enemyWidth, self.enemyHeight)),
            'enemyRight2': pygame.transform.scale(pygame.image.load("img/platformerAssets/enemyRight2.png"), (self.enemyWidth, self.enemyHeight)),
            'enemyRight3': pygame.transform.scale(pygame.image.load("img/platformerAssets/enemyRight3.png"), (self.enemyWidth, self.enemyHeight)),
            'enemyRight4': pygame.transform.scale(pygame.image.load("img/platformerAssets/enemyRight4.png"), (self.enemyWidth, self.enemyHeight)),
            'enemyRight5': pygame.transform.scale(pygame.image.load("img/platformerAssets/enemyRight5.png"), (self.enemyWidth, self.enemyHeight)),
            'enemyLeft1': pygame.transform.scale(pygame.image.load("img/platformerAssets/enemyLeft1.png"), (self.enemyWidth, self.enemyHeight)),
            'enemyLeft2': pygame.transform.scale(pygame.image.load("img/platformerAssets/enemyLeft2.png"), (self.enemyWidth, self.enemyHeight)),
            'enemyLeft3': pygame.transform.scale(pygame.image.load("img/platformerAssets/enemyLeft3.png"), (self.enemyWidth, self.enemyHeight)),
            'enemyLeft4': pygame.transform.scale(pygame.image.load("img/platformerAssets/enemyLeft4.png"), (self.enemyWidth, self.enemyHeight)),
            'enemyLeft5': pygame.transform.scale(pygame.image.load("img/platformerAssets/enemyLeft5.png"), (self.enemyWidth, self.enemyHeight)),
            'sun': pygame.transform.scale(pygame.image.load("img/platformerAssets/sun.png"), (self.tileWidth, self.tileHeight)),
            'coin': pygame.transform.scale(pygame.image.load("img/platformerAssets/coin.png"), (self.coinSize, self.coinSize)),
            'playerStanding': pygame.transform.scale(pygame.image.load("img/platformerAssets/standingnew.png"), (self.playerWidth, self.playerHeight)),
            'R1': pygame.transform.scale(pygame.image.load("img/platformerAssets/R1new.png"), (self.playerWidth, self.playerHeight)),
            'R2': pygame.transform.scale(pygame.image.load("img/platformerAssets/R2new.png"), (self.playerWidth, self.playerHeight)),
            'R3': pygame.transform.scale(pygame.image.load("img/platformerAssets/R3new.png"), (self.playerWidth, self.playerHeight)),
            'R4': pygame.transform.scale(pygame.image.load("img/platformerAssets/R4new.png"), (self.playerWidth, self.playerHeight)),
            'R5': pygame.transform.scale(pygame.image.load("img/platformerAssets/R5new.png"), (self.playerWidth, self.playerHeight)),
            'R6': pygame.transform.scale(pygame.image.load("img/platformerAssets/R6new.png"), (self.playerWidth, self.playerHeight)),
            'R7': pygame.transform.scale(pygame.image.load("img/platformerAssets/R7new.png"), (self.playerWidth, self.playerHeight)),
            'R8': pygame.transform.scale(pygame.image.load("img/platformerAssets/R8new.png"), (self.playerWidth, self.playerHeight)),
            'R9': pygame.transform.scale(pygame.image.load("img/platformerAssets/R9new.png"), (self.playerWidth, self.playerHeight)),
            'L1': pygame.transform.scale(pygame.image.load("img/platformerAssets/L1new.png"), (self.playerWidth, self.playerHeight)),
            'L2': pygame.transform.scale(pygame.image.load("img/platformerAssets/L2new.png"), (self.playerWidth, self.playerHeight)),
            'L3': pygame.transform.scale(pygame.image.load("img/platformerAssets/L3new.png"), (self.playerWidth, self.playerHeight)),
            'L4': pygame.transform.scale(pygame.image.load("img/platformerAssets/L4new.png"), (self.playerWidth, self.playerHeight)),
            'L5': pygame.transform.scale(pygame.image.load("img/platformerAssets/L5new.png"), (self.playerWidth, self.playerHeight)),
            'L6': pygame.transform.scale(pygame.image.load("img/platformerAssets/L6new.png"), (self.playerWidth, self.playerHeight)),
            'L7': pygame.transform.scale(pygame.image.load("img/platformerAssets/L7new.png"), (self.playerWidth, self.playerHeight)),
            'L8': pygame.transform.scale(pygame.image.load("img/platformerAssets/L8new.png"), (self.playerWidth, self.playerHeight)),
            'L9': pygame.transform.scale(pygame.image.load("img/platformerAssets/L9new.png"), (self.playerWidth, self.playerHeight)),
        }

        self.playerMoveRightImgLst = [self.assets['R1'], self.assets['R2'], self.assets['R3'],
                                      self.assets['R4'], self.assets['R5'], self.assets['R6'],
                                      self.assets['R7'], self.assets['R8'], self.assets['R9']]
        self.playerMoveLeftImgLst = [self.assets['L1'], self.assets['L2'], self.assets['L3'],
                                     self.assets['L4'], self.assets['L5'], self.assets['L6'],
                                     self.assets['L7'], self.assets['L8'], self.assets['L9']]

        self.enemyMoveRightImgLst = [self.assets['enemyRight1'], self.assets['enemyRight2'],
                                     self.assets['enemyRight3'], self.assets['enemyRight3'],
                                     self.assets['enemyRight2'], self.assets['enemyRight1'],
                                     self.assets['enemyRight4'], self.assets['enemyRight5']]
        self.enemyMoveLeftImgLst = [self.assets['enemyLeft1'], self.assets['enemyLeft2'],
                                    self.assets['enemyLeft3'], self.assets['enemyLeft3'],
                                    self.assets['enemyLeft2'], self.assets['enemyLeft1'],
                                    self.assets['enemyLeft4'], self.assets['enemyLeft5']]

        self.coinLst = [self.coin1, self.coin2, self.coin3, self.coin4, self.coin5,
                        self.coin6, self.coin7, self.coin8, self.coin9, self.coin10]

        self.grassTileLst = [self.grassRect1, self.grassRect2,
                             self.grassRect3, self.grassRect4,
                             self.grassRect5]

    def drawGrid(self):
        for i in range(0, self.windowWidth - self.tileWidth + 1, 50):
            for j in range(0, self.windowHeight - self.tileWidth + 1, 50):
                pygame.draw.rect(self.window, self.red, (i, j, self.tileWidth, self.tileWidth), 1)

        pygame.draw.rect(self.window, self.blue, self.playerRect, 1)
        pygame.draw.rect(self.window, self.blue, self.enemyRect1, 1)
        pygame.draw.rect(self.window, self.blue, self.enemyRect2, 1)
        for coinPos in self.coinLst:
            pygame.draw.rect(self.window, self.white, coinPos, 2)
        for grassTilePos in self.grassTileLst:
            pygame.draw.rect(self.window, self.green, grassTilePos)
        pygame.draw.rect(self.window, self.black, self.doorRect)

    def drawLayout(self):
        for x in range(0, self.windowWidth - 50 + 1, self.tileWidth):  # bottom line
            self.window.blit(self.assets['grassTile'], (x, self.windowHeight - (1 * self.tileHeight)))

        for x in range(0, self.windowWidth // 2, self.tileWidth):  # second line left
            self.window.blit(self.assets['grassTile'], (x, self.windowHeight - (4 * self.tileHeight)))

        for x in range(0, self.windowWidth // 4, self.tileWidth):  # first line left
            self.window.blit(self.assets['grassTile'], (x, self.windowHeight - (7 * self.tileHeight)))

        for x in range(self.windowWidth // 2 + self.tileWidth, self.windowWidth - (3 * self.tileWidth), self.tileWidth):  # grass second right
            self.window.blit(self.assets['grassTile'], (x, self.windowHeight - (6 * self.tileHeight)))

        for x in range(self.windowWidth - (3 * self.tileWidth), self.windowWidth, self.tileWidth):  # top right grass
            self.window.blit(self.assets['grassTile'], (x, self.windowHeight - (8 * self.tileHeight)))

        for x in range(self.windowWidth - (3 * self.tileWidth), self.windowWidth, self.tileWidth):  # brick right
            self.window.blit(self.assets['gndTile'], (x, self.windowHeight - (7 * self.tileHeight)))

        for x in range(self.windowWidth - (3 * self.tileWidth), self.windowWidth, self.tileWidth):  # brick right
            self.window.blit(self.assets['gndTile'], (x, self.windowHeight - (6 * self.tileHeight)))

        self.window.blit(self.assets['door'], (self.windowWidth - self.doorWidth, 10))

    def drawCoin(self):
        for coinPos in self.coinLst:
            self.window.blit(self.assets['coin'], (coinPos.x, coinPos.y))

    def drawCloudAndSun(self):
        self.window.blit(self.assets['sun'], (365, 10))
        self.window.blit(self.assets['cloud'], (365, 40))
        self.window.blit(self.assets['cloud'], (50, -40))
        self.window.blit(self.assets['cloud'], (630, -10))

    def updateScore(self):
        for coinRect in self.coinLst:
            if self.playerRect.colliderect(coinRect):
                self.coinLst.pop(self.coinLst.index(coinRect))
                self.score += 10

    def showScore(self):
        print("Score: ", self.score)

    def drawBullet(self):
        pygame.draw.rect(self.window, self.black, self.bullet, border_radius=3)

        keys = pygame.key.get_pressed()

        if self.stop == 0:
            if keys[pygame.K_SPACE]:
                if self.moveRight == 1:
                    self.bulletMoveRight = 1
                if self.moveLeft == 1:
                    self.bulletMoveLeft = 1
                if self.moveLeft == 0 and self.moveRight == 0:
                    self.shoot = 0
                self.shoot = 1

            if self.shoot == 1:
                if self.bulletMoveRight == 1:
                    self.bullet.x += self.bulletVel
                if self.bulletMoveLeft == 1:
                    self.bullet.x -= self.bulletVel

    def drawEnemy(self):
        if self.stop == 0 and self.enemy1Died == 0:
            if self.enemyRect1.x <= self.windowWidth // 2:
                self.enemy1MoveRight = 1
                self.enemy1MoveLeft = 0
            if self.enemyRect1.x >= self.windowWidth - self.tileWidth:
                self.enemy1MoveRight = 0
                self.enemy1MoveLeft = 1

            if self.enemy1MoveRight == 1:
                self.enemyRect1.x += self.enemyVel
                if self.enemyWalkCount > 35:
                    self.enemyWalkCount = 0
                self.window.blit(self.enemyMoveRightImgLst[self.enemyWalkCount // 5], (self.enemyRect1.x, self.enemyRect1.y))
                self.enemyWalkCount += 1
            if self.enemy1MoveLeft == 1:
                self.enemyRect1.x -= self.enemyVel
                if self.enemyWalkCount > 35:
                    self.enemyWalkCount = 0
                self.window.blit(self.enemyMoveLeftImgLst[self.enemyWalkCount // 5], (self.enemyRect1.x, self.enemyRect1.y))
                self.enemyWalkCount += 1

        if self.stop == 0 and self.enemy2Died == 0:
            if self.enemyRect2.x <= 250:
                self.enemy2MoveRight = 1
                self.enemy2MoveLeft = 0
            if self.enemyRect2.x >= self.windowWidth // 2 - self.tileWidth:
                self.enemy2MoveRight = 0
                self.enemy2MoveLeft = 1

            if self.enemy2MoveRight == 1:
                self.enemyRect2.x += self.enemyVel
                if self.enemyWalkCount > 35:
                    self.enemyWalkCount = 0
                self.window.blit(self.enemyMoveRightImgLst[self.enemyWalkCount // 5], (self.enemyRect2.x, self.enemyRect2.y))
                self.enemyWalkCount += 1
            if self.enemy2MoveLeft == 1:
                self.enemyRect2.x -= self.enemyVel
                if self.enemyWalkCount > 35:
                    self.enemyWalkCount = 0
                self.window.blit(self.enemyMoveLeftImgLst[self.enemyWalkCount // 5], (self.enemyRect2.x, self.enemyRect2.y))
                self.enemyWalkCount += 1

        if self.enemy1Died == 0 and self.enemy2Died == 0 and self.stop == 1:
            if self.enemy1MoveRight == 1:
                self.window.blit(self.assets['enemyRight1'], (self.enemyRect1.x, self.enemyRect1.y))
            if self.enemy1MoveLeft == 1:
                self.window.blit(self.assets['enemyLeft1'], (self.enemyRect1.x, self.enemyRect1.y))
            if self.enemy2MoveRight == 1:
                self.window.blit(self.assets['enemyRight2'], (self.enemyRect2.x, self.enemyRect2.y))
            if self.enemy2MoveLeft == 1:
                self.window.blit(self.assets['enemyLeft2'], (self.enemyRect2.x, self.enemyRect2.y))
        elif self.enemy1Died == 1 and self.enemy2Died == 0 and self.stop == 1:
            self.window.blit(self.assets['deadEnemy'], (self.enemyRect1.x, self.enemyRect1.y))
            if self.enemy2MoveRight == 1:
                self.window.blit(self.assets['enemyRight2'], (self.enemyRect2.x, self.enemyRect2.y))
            if self.enemy2MoveLeft == 1:
                self.window.blit(self.assets['enemyLeft2'], (self.enemyRect2.x, self.enemyRect2.y))
        elif self.enemy2Died == 1 and self.enemy1Died == 0 and self.stop == 1:
            self.window.blit(self.assets['deadEnemy'], (self.enemyRect2.x, self.enemyRect2.y))
            if self.enemy1MoveRight == 1:
                self.window.blit(self.assets['enemyRight1'], (self.enemyRect1.x, self.enemyRect1.y))
            if self.enemy1MoveLeft == 1:
                self.window.blit(self.assets['enemyLeft1'], (self.enemyRect1.x, self.enemyRect1.y))
        if self.enemy1Died == 1:
            self.window.blit(self.assets['deadEnemy'], (self.enemyRect1.x, self.enemyRect1.y))
        if self.enemy2Died == 1:
            self.window.blit(self.assets['deadEnemy'], (self.enemyRect2.x, self.enemyRect2.y))

    def enemyKilled(self):
        if self.bullet.colliderect(self.enemyRect1):
            self.enemy1Died = 1
            self.bulletMoveRight = 0
            self.bulletMoveLeft = 0
            self.bullet.x = self.playerRect.x + self.playerWidth // 2
            self.bullet.y = self.playerRect.y + self.playerHeight // 2
            self.shoot = 0
        if self.bullet.colliderect(self.enemyRect2):
            self.enemy2Died = 1
            self.bulletMoveRight = 0
            self.bulletMoveLeft = 0
            self.bullet.x = self.playerRect.x + self.playerWidth // 2
            self.bullet.y = self.playerRect.y + self.playerHeight // 2
            self.shoot = 0
        if self.bullet.x > self.windowWidth or self.bullet.x < 0:
            self.bullet.x = self.playerRect.x + self.playerWidth // 2
            self.bullet.y = self.playerRect.y + self.playerHeight // 2
            self.shoot = 0
            self.bulletMoveRight = 0
            self.bulletMoveLeft = 0

    def drawPlayer(self):
        keys = pygame.key.get_pressed()
        if self.stop == 0:
            if keys[pygame.K_LEFT]:
                self.moveRight = 0
                self.moveLeft = 1
                self.playerRect.x -= self.playerVel
                if self.shoot == 0:
                    self.bullet.x -= self.playerVel
                if self.walkCount > 26:
                    self.walkCount = 0
                self.window.blit(self.playerMoveLeftImgLst[self.walkCount // 3], (self.playerRect.x, self.playerRect.y))
                self.walkCount += 1
            elif keys[pygame.K_RIGHT]:
                self.moveLeft = 0
                self.moveRight = 1
                self.playerRect.x += self.playerVel
                if self.shoot == 0:
                    self.bullet.x += self.playerVel
                if self.walkCount > 26:
                    self.walkCount = 0
                self.window.blit(self.playerMoveRightImgLst[self.walkCount // 3], (self.playerRect.x, self.playerRect.y))
                self.walkCount += 1
            else:
                if self.moveLeft == 1:
                    self.window.blit(self.assets['L1'], (self.playerRect.x, self.playerRect.y))
                elif self.moveRight == 1:
                    self.window.blit(self.assets['R1'], (self.playerRect.x, self.playerRect.y))
                else:
                    self.window.blit(self.assets['playerStanding'], (self.playerRect.x, self.playerRect.y))
        if self.stop == 1:
            self.bullet.x = self.windowWidth
            self.window.blit(self.assets['deadPlayer'], (self.playerRect.x + self.playerWidth // 2 - 30, self.playerRect.y + self.playerHeight // 2))

    def playerMovementRestrictions(self):
        keys = pygame.key.get_pressed()

        if self.stop == 0:
            if keys[pygame.K_UP]:
                if 0 <= self.playerRect.x <= 6 * self.tileWidth:
                    if 0 <= self.playerRect.y <= 3 * self.tileHeight:
                        self.isJump = 1
                if 5 * self.tileWidth <= self.playerRect.x <= 10 * self.tileWidth:
                    if 4 * self.tileHeight <= self.playerRect.y <= 6 * self.tileHeight:
                        self.isJump = 1
                if 10 * self.tileWidth <= self.playerRect.x <= 20 * self.tileWidth:
                    if 7 * self.tileHeight <= self.playerRect.y <= 9 * self.tileHeight:
                        self.isJump = 1
                if 11 * self.tileWidth <= self.playerRect.x + self.playerWidth <= 17 * self.tileWidth:
                    if 0 * self.tileHeight <= self.playerRect.y <= 4 * self.tileHeight:
                        self.isJump = 1
                if 16 * self.tileWidth <= self.playerRect.x <= 20 * self.tileWidth:
                    if 0 <= self.playerRect.y <= 1 * self.tileHeight:
                        self.isJump = 1

                if 0 <= self.playerRect.x <= 10 * self.tileWidth:
                    if 7 * self.tileHeight <= self.playerRect.y <= 9 * self.tileHeight:
                        self.isJump = 0
                if 0 <= self.playerRect.x <= 5 * self.tileWidth:
                    if 4 * self.tileHeight <= self.playerRect.y <= 6 * self.tileHeight:
                        self.isJump = 0
                if 0 <= self.playerRect.x <= 6 * self.tileWidth:
                    if self.playerRect.y == 2 * self.tileHeight:
                        self.isJump = 0
                if 10 * self.tileWidth <= self.playerRect.x <= 15 * self.tileWidth:
                    if self.playerRect.y == 3 * self.tileHeight:
                        self.isJump = 0
                if 16 * self.tileWidth <= self.playerRect.x <= 20 * self.tileWidth:
                    if self.playerRect.y <= 1 * self.tileHeight:
                        self.isJump = 0

            if self.isJump == 1:
                neg = 1
                add = 0
                if self.jumpCount >= -10:
                    if self.jumpCount < 0:
                        neg = -1
                        add = 0.5
                    self.playerRect.y -= (((self.jumpCount ** 2) * 0.5) + add) * neg
                    if self.shoot == 0:
                        self.bullet.y -= (((self.jumpCount ** 2) * 0.5) + add) * neg
                    self.jumpCount -= 1
                else:
                    self.jumpCount = 10
                    self.isJump = 0

        if self.playerRect.x <= 0:
            self.playerRect.x += self.playerVel
            if self.shoot == 0:
                self.bullet.x += self.playerVel
        if self.playerRect.x >= self.windowWidth - self.playerWidth:
            self.playerRect.x -= self.playerVel
            if self.shoot == 0:
                self.bullet.x -= self.playerVel

        if self.playerRect.colliderect(self.grassRect5):
            self.playerRect.x -= self.playerVel
            if self.shoot == 0:
                self.bullet.x -= self.playerVel

        if self.playerRect.colliderect(self.grassRect1):
            self.playerRect.y = self.windowHeight - (5 * self.tileHeight)
            if self.shoot == 0:
                self.bullet.y = self.playerRect.y + (self.playerHeight // 2)
        if self.playerRect.colliderect(self.grassRect2):
            self.playerRect.y = self.windowHeight - (7 * self.tileHeight)
            if self.shoot == 0:
                self.bullet.y = self.playerRect.y + (self.playerHeight // 2)
        if self.playerRect.colliderect(self.grassRect3):
            self.playerRect.y = self.windowHeight - (8 * self.tileHeight)
            if self.shoot == 0:
                self.bullet.y = self.playerRect.y + (self.playerHeight // 2)
        if self.playerRect.colliderect(self.grassRect4):
            self.playerRect.y = self.windowHeight - (9 * self.tileHeight)
            if self.shoot == 0:
                self.bullet.y = self.playerRect.y + (self.playerHeight // 2)

        if 10 * self.tileWidth <= self.playerRect.x <= 11 * self.tileWidth:
            if self.playerRect.y == 5 * self.tileHeight:
                self.playerRect.y = self.windowHeight - (2 * self.tileHeight)
                if self.shoot == 0:
                    self.bullet.y = self.playerRect.y + (self.playerHeight // 2)
        if 5 * self.tileWidth <= self.playerRect.x <= 7 * self.tileWidth:
            if self.playerRect.y == 2 * self.tileHeight:
                self.playerRect.y = self.windowHeight - (5 * self.tileHeight)
                if self.shoot == 0:
                    self.bullet.y = self.playerRect.y + (self.playerHeight // 2)
        if 10 * self.tileWidth <= self.playerRect.x + self.playerWidth <= 11 * self.tileWidth:
            if self.playerRect.y == 3 * self.tileHeight:
                self.playerRect.y = self.windowHeight - (5 * self.tileHeight)
                if self.shoot == 0:
                    self.bullet.y = self.playerRect.y + (self.playerHeight // 2)
        if 15 * self.tileWidth <= self.playerRect.x + self.playerWidth <= 17 * self.tileWidth:
            if self.playerRect.y == 1 * self.tileHeight:
                self.playerRect.y = 3 * self.tileHeight
                if self.shoot == 0:
                    self.bullet.y = self.playerRect.y + (self.playerHeight // 2)

    def gameOver(self):
        if self.playerRect.colliderect(self.enemyRect1):
            if self.enemy1Died == 1:
                self.stop = 0
            elif self.enemy1Died == 0:
                self.stop = 1
        if self.playerRect.colliderect(self.enemyRect2):
            if self.enemy2Died == 1:
                self.stop = 0
            elif self.enemy2Died == 0:
                self.stop = 1
        if self.playerRect.colliderect(self.doorRect):
            self.showScore()
            self.run = False

    def drawGameWindow(self):
        self.window.fill(self.skyBlue)
        self.playerMovementRestrictions()
        self.drawBullet()
        self.drawCloudAndSun()
        self.drawLayout()
        self.drawCoin()
        self.updateScore()
        self.drawPlayer()
        self.drawEnemy()
        self.enemyKilled()
        self.gameOver()
        # self.drawGrid()

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


level = Level2()

if __name__ == '__main__':
    level.gameLoop()
