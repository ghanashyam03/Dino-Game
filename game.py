import pygame
import random

# Initialize Pygame
pygame.init()

# Game window dimensions
WIDTH = 800
HEIGHT = 300

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the game window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Game")

clock = pygame.time.Clock()

# Dino variables
dino_width = 64
dino_height = 64
dino_x = 100
dino_y = HEIGHT - dino_height - 20
dino_vel_y = 0
jump_height = 15
gravity = 1

# Cactus variables
cactus_width = 50
cactus_height = 50
cactus_x = WIDTH + random.randint(100, 300)
cactus_y = HEIGHT - cactus_height - 20
cactus_vel_x = -8

# Game over variable
game_over = False

# Score variable
score = 0

# Load images
dino_img = pygame.image.load("dino.png")
dino_img = pygame.transform.scale(dino_img, (dino_width, dino_height))
cactus_img = pygame.image.load("cactus.png")
cactus_img = pygame.transform.scale(cactus_img, (cactus_width, cactus_height))

def reset_game():
    global dino_y, dino_vel_y, cactus_x, game_over, score
    dino_y = HEIGHT - dino_height - 20
    dino_vel_y = 0
    cactus_x = WIDTH + random.randint(100, 300)
    game_over = False
    score = 0

# Main game loop
running = True
while running:
    clock.tick(60)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and dino_y == HEIGHT - dino_height - 20 and not game_over:
                dino_vel_y = -jump_height

            if event.key == pygame.K_SPACE and game_over:
                reset_game()
    
    # Update dino's position
    dino_y += dino_vel_y
    dino_vel_y += gravity
    
    # Check for collision
    if dino_y > HEIGHT - dino_height - 20:
        dino_y = HEIGHT - dino_height - 20
        dino_vel_y = 0
    
    if cactus_x < -cactus_width:
        cactus_x = WIDTH + random.randint(100, 300)
        score += 10
    
    if dino_x + dino_width > cactus_x and dino_x < cactus_x + cactus_width and dino_y + dino_height > cactus_y and dino_y < cactus_y + cactus_height:
        game_over = True
    
    # Update cactus position
    cactus_x += cactus_vel_x
    
    # Render the game
    win.fill(WHITE)
    win.blit(dino_img, (dino_x, dino_y))
    win.blit(cactus_img, (cactus_x, cactus_y))
    
    # Render score
    font = pygame.font.Font(None, 24)
    score_text = font.render("Score: " + str(score), 1, BLACK)
    win.blit(score_text, (WIDTH - score_text.get_width() - 10, 10))
    
    if game_over:
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over! Press Space to Restart", 1, BLACK)
        win.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    
    pygame.display.update()

# Quit the game
pygame.quit()
