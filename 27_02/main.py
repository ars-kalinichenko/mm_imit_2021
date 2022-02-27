import pygame

from consts import *
from snake import Snake, Direction


def handle_moving(snake: Snake):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake.steer(Direction.LEFT)
    elif keys[pygame.K_RIGHT]:
        snake.steer(Direction.RIGHT)
    elif keys[pygame.K_UP]:
        snake.steer(Direction.UP)
    elif keys[pygame.K_DOWN]:
        snake.steer(Direction.DOWN)


def main():
    pygame.init()
    font = pygame.font.SysFont('comicsans', TEXT_SIZE, True)
    window = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    snake = Snake(block_size=BLOCK_SIZE, bounds=WINDOW_SIZE)

    is_run = True

    while is_run:
        pygame.time.delay(DELAY_MS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_run = False

        handle_moving(snake)
        snake.move()

        if snake.check_bounds_collision():
            text = font.render('Game Over', True, TEXT_COLOR)
            window.blit(text, (100, 200))
            pygame.display.update()
            pygame.time.delay(3000)
            snake.spawn()

        window.fill(BACK_COLOR)
        snake.draw(game=pygame, window=window)
        pygame.display.update()


main()
