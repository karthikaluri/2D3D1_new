import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Movement with Speed Boost")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Player settings
player_size = 50
player_pos = [WIDTH // 2, HEIGHT // 2]
base_speed = 5
boost_speed = 10

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    clock.tick(60)  # 60 FPS
    screen.fill(WHITE)

    # Event handling (must come before key press handling)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Input handling
    keys = pygame.key.get_pressed()

    # Determine speed (shift for speed boost)
    speed = boost_speed if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT] else base_speed

    # Movement controls (WASD and Arrow Keys)
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player_pos[1] -= speed
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player_pos[1] += speed
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_pos[0] -= speed
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_pos[0] += speed

    # Boundary locking
    player_pos[0] = max(0, min(WIDTH - player_size, player_pos[0]))
    player_pos[1] = max(0, min(HEIGHT - player_size, player_pos[1]))

    # Draw player
    pygame.draw.rect(screen, BLUE, (*player_pos, player_size, player_size))

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
