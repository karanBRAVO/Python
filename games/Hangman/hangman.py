import pygame
import pyttsx3

pygame.init()
engine = pyttsx3.init()

text = "Welcome to Hangman computer version. find the four letter body part Name before the hangman hangs you."

engine.say(text)
engine.runAndWait()

green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
grey = (192, 192, 192)

font = pygame.font.SysFont("serif", 20, True, True)
font2 = pygame.font.SysFont("fantasy", 45, True)

windowWidth = 700
windowHeight = 500
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Hangman")
print("*** HANGMAN ***")
print("find the body part Name before the hangman hangs you...\nfour letter word")

box_dimension = 30
var_rect = {}
lst_alphabets = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
                 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                 'z', 'x', 'c', 'v', 'b', 'n', 'm']

# five words
words = ['head', 'neck', 'hand', 'nose', 'palm']

mouse_x = 0
mouse_y = 0
x_pos = [40, 60, 80, 100]  # position of words in text box
letter = None
word_1 = None
word_2 = None
word_3 = None
word_4 = None
letter_1 = 0
letter_2 = 0
letter_3 = 0
letter_4 = 0

wrong_click_count = 0
clicked = 'correct'

head_isDrawn = False
stomach_isDrawn = False
leftLeg_isDrawn = False
rightLeg_isDrawn = False
leftHand_isDrawn = False
rightHand_isDrawn = False

level = 1
Ans = None

for i in range(1, 27):
    if i <= 10:
        var_rect[f"alphabet_{i}"] = pygame.Rect(i * (box_dimension + 10), box_dimension * 7, box_dimension, box_dimension)
    elif i <= 19:
        var_rect[f"alphabet_{i}"] = pygame.Rect((i - 10) * (box_dimension + 10 + 3.5), (box_dimension * 7) + 50, box_dimension, box_dimension)
    elif i > 19:
        var_rect[f"alphabet_{i}"] = pygame.Rect((i - 19) * (box_dimension + 10 + 13.5), (box_dimension * 7) + 100, box_dimension, box_dimension)


def drawHead():
    pygame.draw.circle(window, white, center=(windowWidth - 100, 220), radius=20, width=3)  # head


def drawStomach():
    pygame.draw.line(window, white, start_pos=(windowWidth - 100, 240), end_pos=(windowWidth - 100, 310), width=3)  # stomach


def drawLegLeft():
    pygame.draw.line(window, white, start_pos=(windowWidth - 100, 310), end_pos=(windowWidth - 130, 340), width=3)  # left leg


def drawLegRight():
    pygame.draw.line(window, white, start_pos=(windowWidth - 100, 310), end_pos=(windowWidth - 70, 340), width=3)  # right leg


def drawHandLeft():
    pygame.draw.line(window, white, start_pos=(windowWidth - 100, 270), end_pos=(windowWidth - 130, 280), width=3)  # left hand


def drawHandRight():
    pygame.draw.line(window, white, start_pos=(windowWidth - 100, 270), end_pos=(windowWidth - 70, 280), width=3)  # right hand


def drawAlphabets():
    for rect_num in range(1, 27):
        pygame.draw.rect(window, green, var_rect[f"alphabet_{rect_num}"], border_radius=3, width=2)

    for alphabets in lst_alphabets:
        letters = font.render(f"{alphabets}", True, white, None)
        window.blit(letters, [var_rect[f"alphabet_{lst_alphabets.index(alphabets) + 1}"].x + 9, var_rect[f"alphabet_{lst_alphabets.index(alphabets) + 1}"].y + 1])


def drawHanger():
    pygame.draw.line(window, white, start_pos=(windowWidth - 190, 150), end_pos=(windowWidth - 50, 150), width=10)
    pygame.draw.line(window, white, start_pos=(windowWidth - 170, 130), end_pos=(windowWidth - 170, 360), width=10)
    pygame.draw.line(window, white, start_pos=(windowWidth - 200, 360), end_pos=(windowWidth - 40, 360), width=15)
    pygame.draw.line(window, white, start_pos=(windowWidth - 100, 150), end_pos=(windowWidth - 100, 200), width=6)


def answer(which_level, ans):
    if level == which_level:
        return ans


def Reset():
    global mouse_x, mouse_y, letter, letter_1, letter_2, letter_3, letter_4, word_1, word_2, word_3, word_4, level, wrong_click_count, clicked, head_isDrawn, stomach_isDrawn, leftLeg_isDrawn,\
        rightLeg_isDrawn, leftHand_isDrawn, rightHand_isDrawn, Ans

    if pygame.mouse.get_pressed(3)[2]:
        letter = None
        word_1 = None
        word_2 = None
        word_3 = None
        word_4 = None
        letter_1 = 0
        letter_2 = 0
        letter_3 = 0
        letter_4 = 0
        mouse_y = 0
        mouse_x = 0
        level += 1
        wrong_click_count = 0
        clicked = 'correct'
        head_isDrawn = False
        stomach_isDrawn = False
        leftLeg_isDrawn = False
        rightLeg_isDrawn = False
        leftHand_isDrawn = False
        rightHand_isDrawn = False
        if level > 5:
            level = 1


def showWords():
    global mouse_x, mouse_y, letter, letter_1, letter_2, letter_3, letter_4, word_1, word_2, word_3, word_4, level, wrong_click_count, clicked, head_isDrawn, stomach_isDrawn, leftLeg_isDrawn,\
        rightLeg_isDrawn, leftHand_isDrawn, rightHand_isDrawn, Ans
    # get the mouse position
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

    for j in range(1, 27):
        if var_rect[f"alphabet_{j}"].collidepoint(mouse_x, mouse_y):
            word = f"{lst_alphabets[j - 1]}"
            letter = font.render(word, False, white, None)

            if level == 1:
                if word == 'h':
                    letter_1 = 1
                    word_1 = letter
                if word == 'e':
                    letter_2 = 1
                    word_2 = letter
                if word == 'a':
                    letter_3 = 1
                    word_3 = letter
                if word == 'd':
                    letter_4 = 1
                    word_4 = letter

                if word != 'h' and word != 'e' and word != 'a' and word != 'd':
                    clicked = "wrong"

            if level == 2:
                if word == 'n':
                    letter_1 = 1
                    word_1 = letter
                if word == 'e':
                    letter_2 = 1
                    word_2 = letter
                if word == 'c':
                    letter_3 = 1
                    word_3 = letter
                if word == 'k':
                    letter_4 = 1
                    word_4 = letter

                if word != 'n' and word != 'e' and word != 'c' and word != 'k':
                    clicked = "wrong"

            if level == 3:
                if word == 'h':
                    letter_1 = 1
                    word_1 = letter
                if word == 'a':
                    letter_2 = 1
                    word_2 = letter
                if word == 'n':
                    letter_3 = 1
                    word_3 = letter
                if word == 'd':
                    letter_4 = 1
                    word_4 = letter

                if word != 'h' and word != 'a' and word != 'n' and word != 'd':
                    clicked = "wrong"

            if level == 4:
                if word == 'n':
                    letter_1 = 1
                    word_1 = letter
                if word == 'o':
                    letter_2 = 1
                    word_2 = letter
                if word == 's':
                    letter_3 = 1
                    word_3 = letter
                if word == 'e':
                    letter_4 = 1
                    word_4 = letter

                if word != 'n' and word != 'o' and word != 's' and word != 'e':
                    clicked = "wrong"

            if level == 5:
                if word == 'p':
                    letter_1 = 1
                    word_1 = letter
                if word == 'a':
                    letter_2 = 1
                    word_2 = letter
                if word == 'l':
                    letter_3 = 1
                    word_3 = letter
                if word == 'm':
                    letter_4 = 1
                    word_4 = letter

                if word != 'p' and word != 'a' and word != 'l' and word != 'm':
                    clicked = "wrong"

            mouse_x = 0
            mouse_y = 0

    if clicked == "wrong":
        wrong_click_count += 1
        clicked = "correct"

    if wrong_click_count == 1:
        head_isDrawn = True
    if wrong_click_count == 2:
        stomach_isDrawn = True
    if wrong_click_count == 3:
        leftLeg_isDrawn = True
    if wrong_click_count == 4:
        rightLeg_isDrawn = True
    if wrong_click_count == 5:
        leftHand_isDrawn = True
    if wrong_click_count == 6:
        rightHand_isDrawn = True

    if head_isDrawn:
        drawHead()
    if stomach_isDrawn:
        drawStomach()
    if leftLeg_isDrawn:
        drawLegLeft()
    if rightLeg_isDrawn:
        drawLegRight()
    if leftHand_isDrawn:
        drawHandLeft()
    if rightHand_isDrawn:
        drawHandRight()
        if level == 1:
            Ans = words[0]
        if level == 2:
            Ans = words[1]
        if level == 3:
            Ans = words[2]
        if level == 4:
            Ans = words[3]
        if level == 5:
            Ans = words[4]
        Text = answer(level, Ans)
        msg = font2.render(f"answer: {Text} \nTry Again!", True, red, None)
        window.blit(msg, (190, 110))
        Reset()

    if letter_1 == 1:
        window.blit(word_1, (x_pos[0], 125))
    if letter_2 == 1:
        window.blit(word_2, (x_pos[1], 125))
    if letter_3 == 1:
        window.blit(word_3, (x_pos[2], 125))
    if letter_4 == 1:
        window.blit(word_4, (x_pos[3], 125))

    if letter_1 == 1 and letter_2 == 1 and letter_3 == 1 and letter_4 == 1:
        # got correct word
        msg = font2.render("Nice!", True, red, None)
        window.blit(msg, (190, 110))
        # go to next level
        Reset()


def beautify():
    # fill the screen background
    window.fill(black)
    # heading and line at top
    heading = font2.render("HANGMAN", True, red, None)
    window.blit(heading, ((windowWidth // 2) - 80, 10))
    pygame.draw.line(window, white, start_pos=(0, 40), end_pos=(windowWidth, 40))
    # keyboard
    pygame.draw.rect(window, white, (30, 200, box_dimension * 13 + 20, box_dimension * 5), border_radius=3, width=2)
    # draw the text box
    pygame.draw.rect(window, grey, (30, 110, 130, 50), border_radius=3)


def reDrawGameWindow():
    beautify()
    drawHanger()
    drawAlphabets()
    showWords()


def mainloop():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False
        reDrawGameWindow()
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    mainloop()
