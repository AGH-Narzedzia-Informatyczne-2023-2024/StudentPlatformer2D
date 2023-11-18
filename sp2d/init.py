import pygame
import random

# constants

G = 15
V_JUMP = 100
# screen dimensions
WIDTH, HEIGHT = 1280, 720
# player starting position
BASE_POS_X, BASE_POS_Y = WIDTH * 1 / 5, HEIGHT * 3 / 4
PLAYER_RADIUS = 40
OBSTACLE_SPAWN_RATE = 5  # try to spawn an obstacle every n ticks
OBSTACLE_SPAWN_CHANCE = 1 / 12
OBSTACLE_SPEED = 50
OBSTACLE_WIDTH = 50


def main():
    # pygame setup
    pygame.init()
    pygame.display.set_caption("Student Platformer 2D")  # window name
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True
    dt = 0  # delta time
    ticks = 0

    player_v = 0  # velocity
    player_y = BASE_POS_Y

    obstacles_x: list[float] = []

    while running:
        # poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player_v -= G * dt
        player_y = min(player_y - player_v * dt, BASE_POS_Y)

        keys = pygame.key.get_pressed()
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and BASE_POS_Y == player_y:
            player_v = V_JUMP
        if keys[pygame.K_F11]:
            pygame.display.toggle_fullscreen()

        if ticks % OBSTACLE_SPAWN_RATE == 0 and random.random() < OBSTACLE_SPAWN_CHANCE:
            obstacles_x.append(WIDTH)
        obstacles_x = [x - OBSTACLE_SPEED * dt for x in obstacles_x if x >= -OBSTACLE_WIDTH]

        screen.fill("black")

        # ground
        pygame.draw.line(screen, "blue", (0, BASE_POS_Y + PLAYER_RADIUS), (WIDTH, BASE_POS_Y + PLAYER_RADIUS), 4)

        # player
        pygame.draw.circle(screen, "green", (BASE_POS_X, player_y), PLAYER_RADIUS)
        player_hitbox = pygame.Rect(
            BASE_POS_X - PLAYER_RADIUS * 0.7,
            player_y - PLAYER_RADIUS * 0.7,
            PLAYER_RADIUS * 1.4, PLAYER_RADIUS * 1.4
        )
        # pygame.draw.rect(screen, "orange", player_hitbox)

        # obstacles
        for obstacle in obstacles_x:
            rect = pygame.Rect(obstacle, BASE_POS_Y + PLAYER_RADIUS - OBSTACLE_WIDTH, OBSTACLE_WIDTH, OBSTACLE_WIDTH)
            if player_hitbox.colliderect(rect):  # game over
                running = False
            pygame.draw.rect(screen, "red", rect)

        pygame.display.flip()  # update screen

        ticks += 1
        dt = clock.tick(60) / 100

    pygame.quit()
