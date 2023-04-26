import pygame
import random
import time

pygame.init()

clock = pygame.time.Clock()
fps = 30

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)

font = pygame.font.SysFont("Helvetica", 16, True, False)

window_width = 700
window_height = 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake-Game")
print("*** Snake Game ***")

snake_dimension = 10
snake_block = pygame.Rect(10, 30, snake_dimension, snake_dimension)
snake_list = [snake_block]
snakeVel = snake_dimension + 1
move_left = False
move_right = False
move_up = False
move_down = False

food_dimension = 10
food_rect = pygame.Rect(70, 100, food_dimension, food_dimension)

score = 0

snake_dead = False


def food_score():
    global score, snake_list, move_down, move_left, move_right, move_up

    # update the score and food and snake
    if snake_block.colliderect(food_rect):
        random_x = random.randrange(start=0, stop=window_width - food_rect.width)
        random_y = random.randrange(start=0, stop=window_height - food_rect.height)
        food_rect.x = random_x
        food_rect.y = random_y
        score += 1

        if move_left:
            left_rect = pygame.Rect(snake_list[-1][0] + snake_dimension + 1, snake_list[-1][1], snake_dimension, snake_dimension)
            snake_list.append(left_rect)
        if move_right:
            right_rect = pygame.Rect(snake_list[-1][0] - snake_dimension - 1, snake_list[-1][1], snake_dimension, snake_dimension)
            snake_list.append(right_rect)
        if move_up:
            up_rect = pygame.Rect(snake_list[-1][0], snake_list[-1][1] + snake_dimension + 1, snake_dimension, snake_dimension)
            snake_list.append(up_rect)
        if move_down:
            down_rect = pygame.Rect(snake_list[-1][0], snake_list[-1][1] - snake_dimension - 1, snake_dimension, snake_dimension)
            snake_list.append(down_rect)

    # show the score
    msg = font.render(f"Score: {score}", True, yellow, None)
    window.blit(msg, (0, 0))

    pygame.draw.rect(window, green, food_rect, border_radius=15)


def snake():
    global move_up, move_down, move_left, move_right, snakeVel, snake_dead

    keys = pygame.key.get_pressed()

    # check which key is pressed
    if keys[pygame.K_LEFT]:
        move_left = True
        move_right = False
        move_up = False
        move_down = False
    elif keys[pygame.K_RIGHT]:
        move_left = False
        move_right = True
        move_up = False
        move_down = False
    elif keys[pygame.K_UP]:
        move_left = False
        move_right = False
        move_up = True
        move_down = False
    elif keys[pygame.K_DOWN]:
        move_left = False
        move_right = False
        move_up = False
        move_down = True

    # continuously move the snake
    if move_left:
        snake_list[0].x -= snakeVel
        time.sleep(0.1)
    if move_right:
        snake_list[0].x += snakeVel
        time.sleep(0.1)
    if move_up:
        snake_list[0].y -= snakeVel
        time.sleep(0.1)
    if move_down:
        snake_list[0].y += snakeVel
        time.sleep(0.1)

    # stop the game if snake moves outside walls
    if snake_block.x <= 0 or snake_block.x >= window_width - snake_dimension:
        snakeVel *= 0
        snake_dead = True
    elif snake_block.y <= 0 or snake_block.y >= window_height - snake_dimension:
        snakeVel *= 0
        snake_dead = True
    else:
        snake_dead = False

    # stop if snake eats itself
    for j in snake_list[1:]:
        if snake_list[0].colliderect(j):
            snakeVel *= 0
            snake_dead = True

    # draw the snake
    for snake_parts in snake_list:
        pygame.draw.rect(window, white, snake_parts)

    # update the body
    if not snake_dead:
        for i in range(len(snake_list) - 1, 0, -1):
            snake_list[i].x = snake_list[i - 1].x
            snake_list[i].y = snake_list[i - 1].y


def Reset():
    global snake_dead, snake_block, snake_list, snakeVel, move_down, move_left, move_right, move_up, food_rect, score

    if snake_dead:
        if pygame.mouse.get_pressed(3)[2]:
            snake_block = pygame.Rect(10, 30, snake_dimension, snake_dimension)
            snake_list = [snake_block]
            snakeVel = snake_dimension + 1
            move_left = False
            move_right = False
            move_up = False
            move_down = False
            food_rect = pygame.Rect(70, 100, food_dimension, food_dimension)
            score = 0
            snake_dead = False


def re_drawGameWindow():
    window.fill(black)
    Reset()
    snake()
    food_score()


def mainLoop():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
        re_drawGameWindow()
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()


if __name__ == "__main__":
    mainLoop()
