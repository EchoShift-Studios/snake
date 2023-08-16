import pygame
import time
import random

pygame.init()

# Set up display
width = 640
height = 480
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Snake and food
snake_block = 10
snake_speed = 15
snake_list = []
snake_length = 1
snake_head = [width // 2, height // 2]

food_pos = [random.randrange(0, width - snake_block, snake_block),
            random.randrange(0, height - snake_block, snake_block)]

# Game loop
game_over = False
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    for key in keys:
        if keys[pygame.K_LEFT]:
            snake_head[0] -= snake_block
        if keys[pygame.K_RIGHT]:
            snake_head[0] += snake_block
        if keys[pygame.K_UP]:
            snake_head[1] -= snake_block
        if keys[pygame.K_DOWN]:
            snake_head[1] += snake_block

    # Check for collision with boundaries
    if snake_head[0] >= width or snake_head[0] < 0 or snake_head[1] >= height or snake_head[1] < 0:
        game_over = True

    # Update snake
    snake_list.append(list(snake_head))
    if len(snake_list) > snake_length:
        del snake_list[0]

    for segment in snake_list[:-1]:
        if segment == snake_head:
            game_over = True

    # Generate new food
    if snake_head == food_pos:
        food_pos = [random.randrange(0, width - snake_block, snake_block),
                    random.randrange(0, height - snake_block, snake_block)]
        snake_length += 1

    # Draw everything
    display.fill(black)
    for segment in snake_list:
        pygame.draw.rect(display, green, [segment[0], segment[1], snake_block, snake_block])
    pygame.draw.rect(display, red, [food_pos[0], food_pos[1], snake_block, snake_block])

    pygame.display.update()
    clock.tick(snake_speed)

pygame.quit()
