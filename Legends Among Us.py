from sre_constants import JUMP
import pygame
import random
import math

pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRAVITY = 1.5
PLAYER_WIDTH = 250
PLAYER_HEIGHT = 250
PLAYER_SURF_JUMP = -19
PLAYER2_WIDTH = 200
PLAYER2_HEIGHT = 200
PLAYER2_SURF_JUMP = -19
BG_WIDTH = 800
BG_HEIGHT = 595
CLOUD_SPEED = 4
B_WIDTH = 100
B_HEIGHT = 100
B_RECT_SPEED = 20
E_WIDTH = 150
E_HEIGHT = 150
E_RECT_SPEED = 20
NUM_INITIAL_CLOUDS = 50  # Adjust this to increase the number of initial clouds

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY_BLUE = (13, 255, 255)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("I don't know")
clock = pygame.time.Clock()


bg_image = pygame.image.load("C:/Users/zspea/bg1.png").convert_alpha()
bg_image = pygame.transform.scale(bg_image, (BG_WIDTH, BG_HEIGHT))
bg_rect = bg_image.get_rect()
scroll = 0
scroll_speed = 10

player_surf = pygame.image.load("C:/Users/zspea/amo3.png").convert_alpha()
player_surf2 = pygame.image.load("C:/Users/zspea/amo4.png").convert_alpha()
player_surf1 = pygame.image.load("C:/Users/zspea/amo3.png").convert_alpha()
player_surf = pygame.transform.scale(player_surf, (PLAYER_WIDTH, PLAYER_HEIGHT))
player_surf2 = pygame.transform.scale(player_surf2, (PLAYER_WIDTH, PLAYER_HEIGHT))
player_surf1 = pygame.transform.scale(player_surf1, (PLAYER_WIDTH, PLAYER_HEIGHT))
player_rect = player_surf.get_rect()
player_rect2 = player_surf2.get_rect()
player_rect1 = player_surf1.get_rect()
player_rect.bottomleft = (100, 600)
player_rect2.bottomleft = (0, SCREEN_HEIGHT - PLAYER2_HEIGHT - SCREEN_HEIGHT/2)
player_y_momentum = 0
player_on_ground = False
player2_y_momentum = 0
player2_on_ground = False
player_on_ground1 = False
current_image_index1 = False

b_surf = pygame.image.load("C:/Users/zspea/amo5.png").convert_alpha()
b_surf = pygame.transform.scale(b_surf, (B_WIDTH, B_HEIGHT))
b_rect = b_surf.get_rect()
b_rect.bottomleft = (100, SCREEN_HEIGHT - B_HEIGHT - SCREEN_HEIGHT/3)
b_y_momentum = 0

e_surf = pygame.image.load("C:/Users/zspea/ufoo.png").convert_alpha()
e_surf = pygame.transform.scale(e_surf, (E_WIDTH, E_HEIGHT))
e_rect = e_surf.get_rect()
e_rect.bottomleft = (100, 100)
e_x_momentum = 0
e_on_ground = False

clouds = []

def generate_cloud(x):
    cloud = pygame.Rect(x, random.randint(50, 300), 100, 50)
    return cloud

# Generate initial clouds
for x in range(0, SCREEN_WIDTH * 2, 150):
    clouds.append(generate_cloud(x))

# Animation variables
current_image_index = 0
current_image_index1 = 0
images = [player_surf, player_surf, player_surf2, player_surf2, player_surf1, player_surf1]
images2 = [player_surf2]

clock = pygame.time.Clock()
FPS = 20

run = True
e_timer = 0  # Timer variable
e_timer_limit = 1500  # Time limit in milliseconds (1 second)

while run:
    clock.tick(FPS)

    # Scroll background
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        scroll -= scroll_speed
    if keys[pygame.K_LEFT]:
        scroll += scroll_speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                current_image_index = 0
            if event.key == pygame.K_RIGHT:
                current_image_index = 0
    # Apply gravity to the player
    player_y_momentum += GRAVITY
    player_rect.y += player_y_momentum

    e_x_momentum += GRAVITY
    e_rect.y += e_x_momentum


    if player_rect.bottom > SCREEN_HEIGHT:
        player_rect.bottom = SCREEN_HEIGHT
        player_y_momentum = 0  # Reset y-momentum when player touches the ground
        player_on_ground = True


    if e_rect.bottom > SCREEN_HEIGHT:
        e_rect.bottom = SCREEN_HEIGHT
        e_y_momentum = 0  # Reset y-momentum when player touches the ground
        e_on_ground = True

    # Move clouds and triangles when arrow keys are pressed
    if keys[pygame.K_RIGHT]:
        for cloud in clouds:
            cloud.x -= CLOUD_SPEED
            current_image_index = (current_image_index + 1) % len(images)

    if keys[pygame.K_LEFT]:
        for cloud in clouds:
            cloud.x += CLOUD_SPEED
            current_image_index = (current_image_index + 1) % len(images)

    # Handle player jump
    if keys[pygame.K_SPACE] and player_on_ground:
        player_y_momentum += PLAYER_SURF_JUMP
        player_on_ground = False

    # Update the timer
    e_timer += clock.get_time()

    screen.fill(SKY_BLUE)
    # Draw clouds
    for cloud in clouds:
        pygame.draw.ellipse(screen, WHITE, cloud)

    # Loop the background image
    for x in range(-BG_WIDTH, SCREEN_WIDTH, BG_WIDTH):
        screen.blit(bg_image, (scroll % BG_WIDTH + x, 0))

    screen.blit(b_surf, b_rect)

    # Check if the timer has reached the time limit
    if e_timer >= e_timer_limit:
        e_on_ground = True
        screen.blit(images[current_image_index], player_rect)
    else:
        screen.blit(e_surf, e_rect)

    pygame.display.update()

pygame.quit()
exit()
