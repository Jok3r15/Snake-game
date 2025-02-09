import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Snake and food setup
snake = [(100, 100), (90, 100), (80, 100)]
direction = (GRID_SIZE, 0)
food = (random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
        random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE)

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, GRID_SIZE):
                direction = (0, -GRID_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -GRID_SIZE):
                direction = (0, GRID_SIZE)
            elif event.key == pygame.K_LEFT and direction != (GRID_SIZE, 0):
                direction = (-GRID_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-GRID_SIZE, 0):
                direction = (GRID_SIZE, 0)

    # Move the snake
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # Check for collisions
    if (new_head in snake or new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT):
        running = False
        break

    snake.insert(0, new_head)

    # Check if the snake eats food
    if new_head == food:
        food = (random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
                random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE)
    else:
        snake.pop()

    # Draw food
    pygame.draw.rect(screen, RED, (food[0], food[1], GRID_SIZE, GRID_SIZE))

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
