import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

windowWidth = 832
windowHeight = 512
caption = "Platformer 3"
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption(caption)

bg_img = pygame.image.load("./img/platformer3Assets/Background/Gray.png")


def drawBackground():
    for x in range(0, windowWidth, bg_img.get_width()):
        for y in range(0, windowHeight - 1, bg_img.get_height()):
            window.blit(bg_img, (x, y))


def drawGameWindow():
    window.fill(white)
    drawBackground()


def mainLoop(run: bool):
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            drawGameWindow()
            pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    mainLoop(True)
