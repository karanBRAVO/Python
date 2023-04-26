import pygame
from pygame.locals import *
import random

pygame.init()
clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

windowWidth = 500
windowHeight = 400
fps = 60
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Snake and Ladder")
print("*** Snake and Ladder ***")

image_width = 30
image_height = 30
img = {
    'p1': pygame.transform.scale(pygame.image.load("img/player1.png"), (image_width, image_height)),
    'p2': pygame.transform.scale(pygame.image.load("img/player2.png"), (image_width, image_height)),
}

button_width = 50
button_height = 30
spinButton_1 = pygame.Rect(420, 120, button_width, button_height)
spinButton_2 = pygame.Rect(420, 250, button_width, button_height)

player1_rect = pygame.Rect(470, 120, image_width, image_height)
player2_rect = pygame.Rect(470, 250, image_width, image_height)
player1_active = 1
player2_active = 0
player1_start = 0
player2_start = 0

run = True

mouse_x = 0
mouse_y = 0

number1 = 0
number2 = 0
number1_blit = 0
number2_blit = 0

boxWidth = 40
boxHeight = boxWidth
correction = 10


class Box:
    def __init__(self):

        # box rect
        box_1 = pygame.Rect(0 * boxWidth, 0 * boxHeight, boxWidth, boxHeight)
        box_2 = pygame.Rect(1 * boxWidth, 0 * boxHeight, boxWidth, boxHeight)
        box_3 = pygame.Rect(2 * boxWidth, 0 * boxHeight, boxWidth, boxHeight)
        box_4 = pygame.Rect(3 * boxWidth, 0 * boxHeight, boxWidth, boxHeight)
        box_5 = pygame.Rect(4 * boxWidth, 0 * boxHeight, boxWidth, boxHeight)
        box_6 = pygame.Rect(5 * boxWidth, 0 * boxHeight, boxWidth, boxHeight)
        box_7 = pygame.Rect(6 * boxWidth, 0 * boxHeight, boxWidth, boxHeight)
        box_8 = pygame.Rect(7 * boxWidth, 0 * boxHeight, boxWidth, boxHeight)
        box_9 = pygame.Rect(8 * boxWidth, 0 * boxHeight, boxWidth, boxHeight)
        box_10 = pygame.Rect(9 * boxWidth, 0 * boxHeight, boxWidth, boxHeight)

        box_11 = pygame.Rect(0 * boxWidth, 1 * boxHeight, boxWidth, boxHeight)
        box_12 = pygame.Rect(1 * boxWidth, 1 * boxHeight, boxWidth, boxHeight)
        box_13 = pygame.Rect(2 * boxWidth, 1 * boxHeight, boxWidth, boxHeight)
        box_14 = pygame.Rect(3 * boxWidth, 1 * boxHeight, boxWidth, boxHeight)
        box_15 = pygame.Rect(4 * boxWidth, 1 * boxHeight, boxWidth, boxHeight)
        box_16 = pygame.Rect(5 * boxWidth, 1 * boxHeight, boxWidth, boxHeight)
        box_17 = pygame.Rect(6 * boxWidth, 1 * boxHeight, boxWidth, boxHeight)
        box_18 = pygame.Rect(7 * boxWidth, 1 * boxHeight, boxWidth, boxHeight)
        box_19 = pygame.Rect(8 * boxWidth, 1 * boxHeight, boxWidth, boxHeight)
        box_20 = pygame.Rect(9 * boxWidth, 1 * boxHeight, boxWidth, boxHeight)

        box_21 = pygame.Rect(0 * boxWidth, 2 * boxHeight, boxWidth, boxHeight)
        box_22 = pygame.Rect(1 * boxWidth, 2 * boxHeight, boxWidth, boxHeight)
        box_23 = pygame.Rect(2 * boxWidth, 2 * boxHeight, boxWidth, boxHeight)
        box_24 = pygame.Rect(3 * boxWidth, 2 * boxHeight, boxWidth, boxHeight)
        box_25 = pygame.Rect(4 * boxWidth, 2 * boxHeight, boxWidth, boxHeight)
        box_26 = pygame.Rect(5 * boxWidth, 2 * boxHeight, boxWidth, boxHeight)
        box_27 = pygame.Rect(6 * boxWidth, 2 * boxHeight, boxWidth, boxHeight)
        box_28 = pygame.Rect(7 * boxWidth, 2 * boxHeight, boxWidth, boxHeight)
        box_29 = pygame.Rect(8 * boxWidth, 2 * boxHeight, boxWidth, boxHeight)
        box_30 = pygame.Rect(9 * boxWidth, 2 * boxHeight, boxWidth, boxHeight)

        box_31 = pygame.Rect(0 * boxWidth, 3 * boxHeight, boxWidth, boxHeight)
        box_32 = pygame.Rect(1 * boxWidth, 3 * boxHeight, boxWidth, boxHeight)
        box_33 = pygame.Rect(2 * boxWidth, 3 * boxHeight, boxWidth, boxHeight)
        box_34 = pygame.Rect(3 * boxWidth, 3 * boxHeight, boxWidth, boxHeight)
        box_35 = pygame.Rect(4 * boxWidth, 3 * boxHeight, boxWidth, boxHeight)
        box_36 = pygame.Rect(5 * boxWidth, 3 * boxHeight, boxWidth, boxHeight)
        box_37 = pygame.Rect(6 * boxWidth, 3 * boxHeight, boxWidth, boxHeight)
        box_38 = pygame.Rect(7 * boxWidth, 3 * boxHeight, boxWidth, boxHeight)
        box_39 = pygame.Rect(8 * boxWidth, 3 * boxHeight, boxWidth, boxHeight)
        box_40 = pygame.Rect(9 * boxWidth, 3 * boxHeight, boxWidth, boxHeight)

        box_41 = pygame.Rect(0 * boxWidth, 4 * boxHeight, boxWidth, boxHeight)
        box_42 = pygame.Rect(1 * boxWidth, 4 * boxHeight, boxWidth, boxHeight)
        box_43 = pygame.Rect(2 * boxWidth, 4 * boxHeight, boxWidth, boxHeight)
        box_44 = pygame.Rect(3 * boxWidth, 4 * boxHeight, boxWidth, boxHeight)
        box_45 = pygame.Rect(4 * boxWidth, 4 * boxHeight, boxWidth, boxHeight)
        box_46 = pygame.Rect(5 * boxWidth, 4 * boxHeight, boxWidth, boxHeight)
        box_47 = pygame.Rect(6 * boxWidth, 4 * boxHeight, boxWidth, boxHeight)
        box_48 = pygame.Rect(7 * boxWidth, 4 * boxHeight, boxWidth, boxHeight)
        box_49 = pygame.Rect(8 * boxWidth, 4 * boxHeight, boxWidth, boxHeight)
        box_50 = pygame.Rect(9 * boxWidth, 4 * boxHeight, boxWidth, boxHeight)

        box_51 = pygame.Rect(0 * boxWidth, 5 * boxHeight, boxWidth, boxHeight)
        box_52 = pygame.Rect(1 * boxWidth, 5 * boxHeight, boxWidth, boxHeight)
        box_53 = pygame.Rect(2 * boxWidth, 5 * boxHeight, boxWidth, boxHeight)
        box_54 = pygame.Rect(3 * boxWidth, 5 * boxHeight, boxWidth, boxHeight)
        box_55 = pygame.Rect(4 * boxWidth, 5 * boxHeight, boxWidth, boxHeight)
        box_56 = pygame.Rect(5 * boxWidth, 5 * boxHeight, boxWidth, boxHeight)
        box_57 = pygame.Rect(6 * boxWidth, 5 * boxHeight, boxWidth, boxHeight)
        box_58 = pygame.Rect(7 * boxWidth, 5 * boxHeight, boxWidth, boxHeight)
        box_59 = pygame.Rect(8 * boxWidth, 5 * boxHeight, boxWidth, boxHeight)
        box_60 = pygame.Rect(9 * boxWidth, 5 * boxHeight, boxWidth, boxHeight)

        box_61 = pygame.Rect(0 * boxWidth, 6 * boxHeight, boxWidth, boxHeight)
        box_62 = pygame.Rect(1 * boxWidth, 6 * boxHeight, boxWidth, boxHeight)
        box_63 = pygame.Rect(2 * boxWidth, 6 * boxHeight, boxWidth, boxHeight)
        box_64 = pygame.Rect(3 * boxWidth, 6 * boxHeight, boxWidth, boxHeight)
        box_65 = pygame.Rect(4 * boxWidth, 6 * boxHeight, boxWidth, boxHeight)
        box_66 = pygame.Rect(5 * boxWidth, 6 * boxHeight, boxWidth, boxHeight)
        box_67 = pygame.Rect(6 * boxWidth, 6 * boxHeight, boxWidth, boxHeight)
        box_68 = pygame.Rect(7 * boxWidth, 6 * boxHeight, boxWidth, boxHeight)
        box_69 = pygame.Rect(8 * boxWidth, 6 * boxHeight, boxWidth, boxHeight)
        box_70 = pygame.Rect(9 * boxWidth, 6 * boxHeight, boxWidth, boxHeight)

        box_71 = pygame.Rect(0 * boxWidth, 7 * boxHeight, boxWidth, boxHeight)
        box_72 = pygame.Rect(1 * boxWidth, 7 * boxHeight, boxWidth, boxHeight)
        box_73 = pygame.Rect(2 * boxWidth, 7 * boxHeight, boxWidth, boxHeight)
        box_74 = pygame.Rect(3 * boxWidth, 7 * boxHeight, boxWidth, boxHeight)
        box_75 = pygame.Rect(4 * boxWidth, 7 * boxHeight, boxWidth, boxHeight)
        box_76 = pygame.Rect(5 * boxWidth, 7 * boxHeight, boxWidth, boxHeight)
        box_77 = pygame.Rect(6 * boxWidth, 7 * boxHeight, boxWidth, boxHeight)
        box_78 = pygame.Rect(7 * boxWidth, 7 * boxHeight, boxWidth, boxHeight)
        box_79 = pygame.Rect(8 * boxWidth, 7 * boxHeight, boxWidth, boxHeight)
        box_80 = pygame.Rect(9 * boxWidth, 7 * boxHeight, boxWidth, boxHeight)

        box_81 = pygame.Rect(0 * boxWidth, 8 * boxHeight, boxWidth, boxHeight)
        box_82 = pygame.Rect(1 * boxWidth, 8 * boxHeight, boxWidth, boxHeight)
        box_83 = pygame.Rect(2 * boxWidth, 8 * boxHeight, boxWidth, boxHeight)
        box_84 = pygame.Rect(3 * boxWidth, 8 * boxHeight, boxWidth, boxHeight)
        box_85 = pygame.Rect(4 * boxWidth, 8 * boxHeight, boxWidth, boxHeight)
        box_86 = pygame.Rect(5 * boxWidth, 8 * boxHeight, boxWidth, boxHeight)
        box_87 = pygame.Rect(6 * boxWidth, 8 * boxHeight, boxWidth, boxHeight)
        box_88 = pygame.Rect(7 * boxWidth, 8 * boxHeight, boxWidth, boxHeight)
        box_89 = pygame.Rect(8 * boxWidth, 8 * boxHeight, boxWidth, boxHeight)
        box_90 = pygame.Rect(9 * boxWidth, 8 * boxHeight, boxWidth, boxHeight)

        box_91 = pygame.Rect(0 * boxWidth, 9 * boxHeight, boxWidth, boxHeight)
        box_92 = pygame.Rect(1 * boxWidth, 9 * boxHeight, boxWidth, boxHeight)
        box_93 = pygame.Rect(2 * boxWidth, 9 * boxHeight, boxWidth, boxHeight)
        box_94 = pygame.Rect(3 * boxWidth, 9 * boxHeight, boxWidth, boxHeight)
        box_95 = pygame.Rect(4 * boxWidth, 9 * boxHeight, boxWidth, boxHeight)
        box_96 = pygame.Rect(5 * boxWidth, 9 * boxHeight, boxWidth, boxHeight)
        box_97 = pygame.Rect(6 * boxWidth, 9 * boxHeight, boxWidth, boxHeight)
        box_98 = pygame.Rect(7 * boxWidth, 9 * boxHeight, boxWidth, boxHeight)
        box_99 = pygame.Rect(8 * boxWidth, 9 * boxHeight, boxWidth, boxHeight)
        box_100 = pygame.Rect(9 * boxWidth, 9 * boxHeight, boxWidth, boxHeight)

        # boxes in list
        self.boxLst = [box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10,
                       box_11, box_12, box_13, box_14, box_15, box_16, box_17, box_18, box_19, box_20,
                       box_21, box_22, box_23, box_24, box_25, box_26, box_27, box_28, box_29, box_30,
                       box_31, box_32, box_33, box_34, box_35, box_36, box_37, box_38, box_39, box_40,
                       box_41, box_42, box_43, box_44, box_45, box_46, box_47, box_48, box_49, box_50,
                       box_51, box_52, box_53, box_54, box_55, box_56, box_57, box_58, box_59, box_60,
                       box_61, box_62, box_63, box_64, box_65, box_66, box_67, box_68, box_69, box_70,
                       box_71, box_72, box_73, box_74, box_75, box_76, box_77, box_78, box_79, box_80,
                       box_81, box_82, box_83, box_84, box_85, box_86, box_87, box_88, box_89, box_90,
                       box_91, box_92, box_93, box_94, box_95, box_96, box_97, box_98, box_99, box_100]

        self.boxLst_num = [box_91, box_92, box_93, box_94, box_95, box_96, box_97, box_98, box_99, box_100,
                           box_90, box_89, box_88, box_87, box_86, box_85, box_84, box_83, box_82, box_81,
                           box_71, box_72, box_73, box_74, box_75, box_76, box_77, box_78, box_79, box_80,
                           box_70, box_69, box_68, box_67, box_66, box_65, box_64, box_63, box_62, box_61,
                           box_51, box_52, box_53, box_54, box_55, box_56, box_57, box_58, box_59, box_60,
                           box_50, box_49, box_48, box_47, box_46, box_45, box_44, box_43, box_42, box_41,
                           box_31, box_32, box_33, box_34, box_35, box_36, box_37, box_38, box_39, box_40,
                           box_30, box_29, box_28, box_27, box_26, box_25, box_24, box_23, box_22, box_21,
                           box_11, box_12, box_13, box_14, box_15, box_16, box_17, box_18, box_19, box_20,
                           box_10, box_9, box_8, box_7, box_6, box_5, box_4, box_3, box_2, box_1]

    def msg(self):
        font = pygame.font.SysFont('serif', 16, True, False)
        for num in range(1, 101):
            message = font.render(f'{num}', True, black)
            window.blit(message, (self.boxLst_num[num - 1].x + (boxWidth // 2) - correction, self.boxLst_num[num - 1].y + (boxHeight // 2) - correction, boxWidth, boxHeight))

    def drawBox(self):
        for pos in self.boxLst:
            pygame.draw.rect(window, black, pos, width=1)

        self.msg()


box = Box()


def layout():
    font2 = pygame.font.SysFont("fantasy", 16, True, False)
    message3 = font2.render("player 1", True, green)
    message4 = font2.render("player 2", True, green)
    message5 = font2.render(f'{number1_blit}', True, black)
    message6 = font2.render(f'{number2_blit}', True, black)

    window.blit(img['p1'], (470, 120))
    window.blit(message3, (435, 105))
    window.blit(img['p2'], (470, 250))
    window.blit(message4, (435, 235))

    window.blit(message5, (475, 155))
    window.blit(message6, (475, 285))

    window.blit(pygame.transform.scale(pygame.image.load("img/ladder1.png"), (20, 217)), (8, 126))
    window.blit(pygame.transform.scale(pygame.image.load("img/ladder1.png"), (20, 185)), (370, 10))
    window.blit(pygame.transform.scale(pygame.image.load("img/ladderTilted1.png"), (50, 105)), (52, 10))
    window.blit(pygame.transform.scale(pygame.image.load("img/ladderTilted1.png"), (50, 105)), (213, 290))

    window.blit(pygame.transform.scale(pygame.image.load("img/snake.png"), (50, 105)), (320, 265))
    window.blit(pygame.transform.scale(pygame.image.load("img/snake2.png"), (50, 319)), (105, 14))
    window.blit(pygame.transform.scale(pygame.image.load("img/snake3.png"), (50, 170)), (9, 50))
    window.blit(pygame.transform.scale(pygame.image.load("img/snake3.png"), (51, 83)), (50, 290))
    window.blit(pygame.transform.scale(pygame.image.load("img/snake4.png"), (97, 255)), (170, 130))


def spinButtons():
    font1 = pygame.font.SysFont("fantasy", 16, True, False)
    message1 = font1.render("SPIN", True, blue)
    message2 = font1.render("SPIN", True, green)
    message1Rect = message1.get_rect()
    message1Rect.center = (444, 135)
    message2Rect = message2.get_rect()
    message2Rect.center = (444, 265)

    pygame.draw.rect(window, green, spinButton_1, border_radius=3)
    window.blit(message1, message1Rect)
    pygame.draw.rect(window, blue, spinButton_2, border_radius=3)
    window.blit(message2, message2Rect)

    window.blit(img['p1'], player1_rect)
    window.blit(img['p2'], player2_rect)


def player1_logic():
    global player1_rect, player1_start, player1_active, number1, run

    if player1_start == 0:
        if number1 == 6:
            player1_rect = box.boxLst_num[0]
            player1_start = 1
            number1 = 0

    if player1_start == 1:
        if player1_active == 1:
            if box.boxLst_num.index(player1_rect) + number1 < 100:
                player1_rect = box.boxLst_num[box.boxLst_num.index(player1_rect) + number1]
                # got ladder
                if player1_rect == box.boxLst_num[7 - 1]:
                    player1_rect = box.boxLst_num[26 - 1]
                if player1_rect == box.boxLst_num[20 - 1]:
                    player1_rect = box.boxLst_num[61 - 1]
                if player1_rect == box.boxLst_num[51 - 1]:
                    player1_rect = box.boxLst_num[91 - 1]
                if player1_rect == box.boxLst_num[78 - 1]:
                    player1_rect = box.boxLst_num[99 - 1]
                # got snake bite
                if player1_rect == box.boxLst_num[97 - 1]:
                    player1_rect = box.boxLst_num[18 - 1]
                if player1_rect == box.boxLst_num[82 - 1]:
                    player1_rect = box.boxLst_num[41 - 1]
                if player1_rect == box.boxLst_num[67 - 1]:
                    player1_rect = box.boxLst_num[5 - 1]
                if player1_rect == box.boxLst_num[32 - 1]:
                    player1_rect = box.boxLst_num[9 - 1]
                if player1_rect == box.boxLst_num[23 - 1]:
                    player1_rect = box.boxLst_num[2 - 1]
            if player1_rect == box.boxLst_num[99]:
                print("Player 1 is WINNER!")
            number1 = 0


def player2_logic():
    global player2_rect, player2_start, player2_active, number2, run

    if player2_start == 0:
        if number2 == 6:
            player2_rect = box.boxLst_num[0]
            player2_start = 1
            number2 = 0

    if player2_start == 1:
        if player2_active == 1:
            if box.boxLst_num.index(player2_rect) + number2 < 100:
                player2_rect = box.boxLst_num[box.boxLst_num.index(player2_rect) + number2]
                if player2_rect == box.boxLst_num[7 - 1]:
                    player2_rect = box.boxLst_num[26 - 1]
                if player2_rect == box.boxLst_num[20 - 1]:
                    player2_rect = box.boxLst_num[61 - 1]
                if player2_rect == box.boxLst_num[51 - 1]:
                    player2_rect = box.boxLst_num[91 - 1]
                if player2_rect == box.boxLst_num[78 - 1]:
                    player2_rect = box.boxLst_num[99 - 1]

                if player2_rect == box.boxLst_num[97 - 1]:
                    player2_rect = box.boxLst_num[18 - 1]
                if player2_rect == box.boxLst_num[82 - 1]:
                    player2_rect = box.boxLst_num[41 - 1]
                if player2_rect == box.boxLst_num[67 - 1]:
                    player2_rect = box.boxLst_num[5 - 1]
                if player2_rect == box.boxLst_num[32 - 1]:
                    player2_rect = box.boxLst_num[9 - 1]
                if player2_rect == box.boxLst_num[23 - 1]:
                    player2_rect = box.boxLst_num[2 - 1]
            if player2_rect == box.boxLst_num[99]:
                print("Player 2 is WINNER!")
            number2 = 0


if __name__ == '__main__':
    while run:
        window.fill(white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

        if player1_active == 1:
            if spinButton_1.collidepoint(mouse_x, mouse_y):
                number1 = random.randint(1, 6)
                number1_blit = number1
                player1_logic()
                player1_active = 0
                player2_active = 1
        if player2_active == 1:
            if spinButton_2.collidepoint(mouse_x, mouse_y):
                number2 = random.randint(1, 6)
                number2_blit = number2
                player2_logic()
                player1_active = 1
                player2_active = 0

        layout()
        box.drawBox()
        spinButtons()

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
