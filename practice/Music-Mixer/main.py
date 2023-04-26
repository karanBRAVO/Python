import pygame

print(" \n\t<-- Welcome to .mp3 Music Player -->")
print(" \n\tPRESS --> F1 F2 F3 F4 F5 F6 F7 F8 F9 F10 F11 F12 --> TO PLAY")
print(" \tPRESS --> Tab --> TO PAUSE")
print(" \tPRESS --> Esc --> TO EXIT")

pygame.init()
pygame.mixer.init()

screen_width = 400
screen_height = 350

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

screen_window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Music Mixer")
pygame.display.update()

font = pygame.font.SysFont(str(None), 30)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    screen_window.blit(screen_text, [x, y])


exit_window = False

while not exit_window:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_window = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit_window = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                pygame.mixer.music.load('1.mp3')
                pygame.mixer.music.play()

            if event.key == pygame.K_F2:
                pygame.mixer.music.load('2.mp3')
                pygame.mixer.music.play()

            if event.key == pygame.K_F3:
                pygame.mixer.music.load('3.mp3')
                pygame.mixer.music.play()

            if event.key == pygame.K_F4:
                pygame.mixer.music.load('4.mp3')
                pygame.mixer.music.play()

            if event.key == pygame.K_F5:
                pygame.mixer.music.load('5.mp3')
                pygame.mixer.music.play()

            if event.key == pygame.K_F6:
                pygame.mixer.music.load('6.mp3')
                pygame.mixer.music.play()

            if event.key == pygame.K_F7:
                pygame.mixer.music.load('7.mp3')
                pygame.mixer.music.play()

            if event.key == pygame.K_F8:
                pygame.mixer.music.load('8.mp3')
                pygame.mixer.music.play()

            if event.key == pygame.K_F9:
                pygame.mixer.music.load('9.mp3')
                pygame.mixer.music.play()

            if event.key == pygame.K_F10:
                pygame.mixer.music.load('10.mp3')
                pygame.mixer.music.play()

            if event.key == pygame.K_F11:
                pygame.mixer.music.load('11.mp3')
                pygame.mixer.music.play()

            if event.key == pygame.K_F12:
                pygame.mixer.music.load('12.mp3')
                pygame.mixer.music.play()

            if event.key == pygame.K_TAB:
                pygame.mixer.music.pause()

    screen_window.fill(white)
    text_screen("HELLO WORLD!", blue, 123, 150)
    pygame.draw.circle(screen_window, red, [197, 150], 100, 5)
    pygame.display.update()

pygame.quit()
quit()
