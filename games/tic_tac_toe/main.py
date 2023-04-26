import pygame
from pygame.locals import *

pygame.init()

grey = (128, 128, 128)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
aqua = (0, 255, 255)

window_width = 400
window_Height = window_width
window = pygame.display.set_mode((window_width, window_Height))
pygame.display.set_caption("TIC-TAC-TOE")
print("*** Tic-Tac_Toe ***")
print("press Right Mouse Button for new game.")

gap = window_width // 3  # 133
mouse_x = 0
mouse_y = 0
pos = None
turn = "circle"
print("First Turn: ", turn)
win = False

place_1_1 = 0
place_1_2 = 0
place_1_3 = 0
place_2_1 = 0
place_2_2 = 0
place_2_3 = 0
place_3_1 = 0
place_3_2 = 0
place_3_3 = 0
cross_1 = 0
cross_2 = 0
cross_3 = 0
cross_4 = 0
cross_5 = 0
cross_6 = 0
cross_7 = 0
cross_8 = 0
cross_9 = 0
circle_1 = 0
circle_2 = 0
circle_3 = 0
circle_4 = 0
circle_5 = 0
circle_6 = 0
circle_7 = 0
circle_8 = 0
circle_9 = 0

h_1 = 0
h_2 = 0
h_3 = 0
v_1 = 0
v_2 = 0
v_3 = 0
d_1 = 0
d_2 = 0


# row_1 = [1, 2, 3]
# row_2 = [4, 5, 6]
# row_3 = [7, 8, 9]


def Reset():
    global pos, turn, win, place_1_1, place_2_2, place_3_3, place_1_2, place_1_3, place_2_1, place_2_3, place_3_1, place_3_2, cross_1, cross_2, cross_3, cross_4, cross_5, cross_6, cross_7, cross_8, \
        cross_9, circle_9, circle_8, circle_7, circle_6, circle_5, circle_4, circle_3, circle_2, circle_1, h_1, h_2, h_3, v_1, v_2, v_3, d_1, d_2

    if pygame.mouse.get_pressed(3)[2]:
        pos = None
        turn = "cross"
        print("New Game Started...")
        print("First Turn: ", turn)
        win = False

        place_1_1 = 0
        place_1_2 = 0
        place_1_3 = 0
        place_2_1 = 0
        place_2_2 = 0
        place_2_3 = 0
        place_3_1 = 0
        place_3_2 = 0
        place_3_3 = 0
        cross_1 = 0
        cross_2 = 0
        cross_3 = 0
        cross_4 = 0
        cross_5 = 0
        cross_6 = 0
        cross_7 = 0
        cross_8 = 0
        cross_9 = 0
        circle_1 = 0
        circle_2 = 0
        circle_3 = 0
        circle_4 = 0
        circle_5 = 0
        circle_6 = 0
        circle_7 = 0
        circle_8 = 0
        circle_9 = 0
        h_1 = 0
        h_2 = 0
        h_3 = 0
        v_1 = 0
        v_2 = 0
        v_3 = 0
        d_1 = 0
        d_2 = 0


def draw_circle(x, y):  # gap // 2 = 66
    pygame.draw.circle(window, green, radius=(gap // 2) - 2, center=(x, y), width=5)


def draw_cross(x1, y1, x2, y2):
    pygame.draw.line(window, red, (x1, y1), (x2, y2), width=5)
    pygame.draw.line(window, red, (x1, y2), (x2, y1), width=5)


def Win_line(x1, y1, x2, y2):
    pygame.draw.line(window, aqua, (x1, y1), (x2, y2), width=5)


def Game_logic():
    global mouse_x, mouse_y, pos, turn, place_1_1, place_2_2, place_3_3, place_1_2, place_1_3, place_2_1, place_2_3, place_3_1, place_3_2, cross_1, cross_2, cross_3, cross_4, cross_5, cross_6, \
        cross_7, cross_8, cross_9, circle_9, circle_8, circle_7, circle_6, circle_5, circle_4, circle_3, circle_2, circle_1

    if pygame.mouse.get_pressed(3)[0]:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        pos = [mouse_x, mouse_y]

    if pos is not None:
        # <--- Row 1 --->
        # Col 1
        if place_1_1 == 0:
            if 0 < pos[0] < gap and 0 < pos[1] < gap:
                if turn == "cross":
                    cross_1 = 1
                    turn = "circle"
                if cross_1 == 0:
                    if turn == "circle":
                        circle_1 = 1
                        turn = "cross"
                place_1_1 = 1
        # Col 2
        if place_1_2 == 0:
            if gap * 2 > pos[0] > gap > pos[1] > 0:
                if turn == "cross":
                    cross_2 = 1
                    turn = "circle"
                if cross_2 == 0:
                    if turn == "circle":
                        circle_2 = 1
                        turn = "cross"
                place_1_2 = 1
        # Col 3
        if place_1_3 == 0:
            if gap * 2 < pos[0] < gap * 3 and 0 < pos[1] < gap:
                if turn == "cross":
                    cross_3 = 1
                    turn = "circle"
                if cross_3 == 0:
                    if turn == "circle":
                        circle_3 = 1
                        turn = "cross"
                place_1_3 = 1
        # <--- Row 2 --->
        # Col 1
        if place_2_1 == 0:
            if 0 < pos[0] < gap < pos[1] < gap * 2:
                if turn == "cross":
                    cross_4 = 1
                    turn = "circle"
                if cross_4 == 0:
                    if turn == "circle":
                        circle_4 = 1
                        turn = "cross"
                place_2_1 = 1
        # Col 2
        if place_2_2 == 0:
            if gap < pos[0] < gap * 2 and gap < pos[1] < gap * 2:
                if turn == "cross":
                    cross_5 = 1
                    turn = "circle"
                if cross_5 == 0:
                    if turn == "circle":
                        circle_5 = 1
                        turn = "cross"
                place_2_2 = 1
        # Col 3
        if place_2_3 == 0:
            if gap * 3 > pos[0] > gap * 2 > pos[1] > gap:
                if turn == "cross":
                    cross_6 = 1
                    turn = "circle"
                if cross_6 == 0:
                    if turn == "circle":
                        circle_6 = 1
                        turn = "cross"
                place_2_3 = 1
        # <--- Row 3 --->
        # Col 1
        if place_3_1 == 0:
            if 0 < pos[0] < gap and gap * 2 < pos[1] < gap * 3:
                if turn == "cross":
                    cross_7 = 1
                    turn = "circle"
                if cross_7 == 0:
                    if turn == "circle":
                        circle_7 = 1
                        turn = "cross"
                place_3_1 = 1
        # Col 2
        if place_3_2 == 0:
            if gap < pos[0] < gap * 2 < pos[1] < gap * 3:
                if turn == "cross":
                    cross_8 = 1
                    turn = "circle"
                if cross_8 == 0:
                    if turn == "circle":
                        circle_8 = 1
                        turn = "cross"
                place_3_2 = 1
        # Col 3
        if place_3_3 == 0:
            if gap * 2 < pos[0] < gap * 3 and gap * 2 < pos[1] < gap * 3:
                if turn == "cross":
                    cross_9 = 1
                    turn = "circle"
                if cross_9 == 0:
                    if turn == "circle":
                        circle_9 = 1
                        turn = "cross"
                place_3_3 = 1

    # <--- Row 1 --->
    # Col 1
    if cross_1 == 1:
        draw_cross(0, 0, gap, gap)
    if circle_1 == 1:
        draw_circle(gap // 2, gap // 2)
    # Col 2
    if cross_2 == 1:
        draw_cross(gap, 0, gap * 2, gap)
    if circle_2 == 1:
        draw_circle(gap + (gap // 2), gap // 2)
    # Col 3
    if cross_3 == 1:
        draw_cross(gap * 2, 0, gap * 3, gap)
    if circle_3 == 1:
        draw_circle((gap * 2) + (gap // 2), gap // 2)
    # <--- Row 2 --->
    # Col 1
    if cross_4 == 1:
        draw_cross(gap * 0, gap, gap, gap * 2)
    if circle_4 == 1:
        draw_circle(gap // 2, gap + (gap // 2))
    # Col 2
    if cross_5 == 1:
        draw_cross(gap * 1, gap, gap * 2, gap * 2)
    if circle_5 == 1:
        draw_circle(gap + (gap // 2), gap + (gap // 2))
    # Col 3
    if cross_6 == 1:
        draw_cross(gap * 2, gap, gap * 3, gap * 2)
    if circle_6 == 1:
        draw_circle((gap * 2) + (gap // 2), gap + (gap // 2))
    # <--- Row 3 --->
    # Col 1
    if cross_7 == 1:
        draw_cross(gap * 0, gap * 2, gap, gap * 3)
    if circle_7 == 1:
        draw_circle(gap // 2, (gap * 2) + (gap // 2))
    # Col 2
    if cross_8 == 1:
        draw_cross(gap * 1, gap * 2, gap * 2, gap * 3)
    if circle_8 == 1:
        draw_circle(gap + (gap // 2), (gap * 2) + (gap // 2))
    # Col 3
    if cross_9 == 1:
        draw_cross(gap * 2, gap * 2, gap * 3, gap * 3)
    if circle_9 == 1:
        draw_circle((gap * 2) + (gap // 2), (gap * 2) + (gap // 2))


def win_logic():
    global win, cross_1, cross_2, cross_3, cross_4, cross_5, cross_6, cross_7, cross_8, cross_9, circle_9, circle_8, circle_7, circle_6, circle_5, circle_4, circle_3, circle_2, circle_1, h_1, h_2, \
        h_3, v_1, v_2, v_3, d_1, d_2

    if not win:
        # Horizontal Check
        # cross
        if cross_1 == 1 and cross_2 == 1 and cross_3 == 1:
            win = True
            print("Cross Wins")
            h_1 = 1
        if cross_4 == 1 and cross_5 == 1 and cross_6 == 1:
            win = True
            print("Cross Wins")
            h_2 = 1
        if cross_7 == 1 and cross_8 == 1 and cross_9 == 1:
            win = True
            print("Cross Wins")
            h_3 = 1
        # circle
        if circle_1 == 1 and circle_2 == 1 and circle_3 == 1:
            win = True
            print("Circle Wins")
            h_1 = 1
        if circle_4 == 1 and circle_5 == 1 and circle_6 == 1:
            win = True
            print("Circle Wins")
            h_2 = 1
        if circle_7 == 1 and circle_8 == 1 and circle_9 == 1:
            win = True
            print("Circle Wins")
            h_3 = 1

        # Vertical Check
        # cross
        if cross_1 == 1 and cross_4 == 1 and cross_7 == 1:
            win = True
            print("Cross Wins")
            v_1 = 1
        if cross_2 == 1 and cross_5 == 1 and cross_8 == 1:
            win = True
            print("Cross Wins")
            v_2 = 1
        if cross_3 == 1 and cross_6 == 1 and cross_9 == 1:
            win = True
            print("Cross Wins")
            v_3 = 1
        # circle
        if circle_1 == 1 and circle_4 == 1 and circle_7 == 1:
            win = True
            print("Circle Wins")
            v_1 = 1
            Win_line(gap // 2, 0, gap // 2, window_Height)
        if circle_2 == 1 and circle_5 == 1 and circle_8 == 1:
            win = True
            print("Circle Wins")
            v_2 = 1
            Win_line(gap + (gap // 2), 0, gap + (gap // 2), window_Height)
        if circle_3 == 1 and circle_6 == 1 and circle_9 == 1:
            win = True
            print("Circle Wins")
            v_3 = 1

        # Diagonal Check
        # cross
        if cross_1 == 1 and cross_5 == 1 and cross_9 == 1:
            win = True
            print("Cross Wins")
            d_1 = 1
        if cross_3 == 1 and cross_5 == 1 and cross_7 == 1:
            win = True
            print("Cross Wins")
            d_2 = 1
        # circle
        if circle_1 == 1 and circle_5 == 1 and circle_9 == 1:
            win = True
            print("Circle Wins")
            d_1 = 1
        if circle_3 == 1 and circle_5 == 1 and circle_7 == 1:
            win = True
            print("Circle Wins")
            d_2 = 1

    if h_1 == 1:
        Win_line(0, gap // 2, window_width, gap // 2)
    if h_2 == 1:
        Win_line(0, gap + (gap // 2), window_width, gap + (gap // 2))
    if h_3 == 1:
        Win_line(0, (gap * 2) + (gap // 2), window_width, (gap * 2) + (gap // 2))
    if v_1 == 1:
        Win_line(gap // 2, 0, gap // 2, window_Height)
    if v_2 == 1:
        Win_line(gap + (gap // 2), 0, gap + (gap // 2), window_Height)
    if v_3 == 1:
        Win_line((gap * 2) + (gap // 2), 0, (gap * 2) + (gap // 2), window_Height)
    if d_1 == 1:
        Win_line(0, 0, window_width, window_Height)
    if d_2 == 1:
        Win_line(window_width, 0, 0, window_Height)

    if win:
        Reset()
    if not win and place_1_1 == 1 and place_1_2 == 1 and place_1_3 == 1 and place_2_1 == 1 and place_2_2 == 1 and place_2_3 == 1 and place_3_1 == 1 and place_3_2 == 1 and place_3_3 == 1:
        Reset()


def drawGrid():
    for col in range(0, 4):
        pygame.draw.line(window, grey, (col * gap, 0), (col * gap, window_Height))
    for row in range(0, 4):
        pygame.draw.line(window, grey, (0, row * gap), (window_width, row * gap))


def reDrawGameWindow():
    window.fill(white)
    drawGrid()
    Game_logic()
    win_logic()
    pygame.display.update()


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                run = False
        reDrawGameWindow()
    pygame.quit()


if __name__ == "__main__":
    main()
