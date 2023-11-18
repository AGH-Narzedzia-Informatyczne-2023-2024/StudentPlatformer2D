import pygame

# constants

G = 15
V_JUMP = 100
# screen dimensions
WIDTH, HEIGHT = 1280, 720
# player starting position
BASE_POS_X, BASE_POS_Y = WIDTH * 1 / 5, HEIGHT * 3 / 4
PLAYER_RADIUS = 40


def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True
    dt = 0  # delta time

    player_v = 0  # velocity
    player_y = BASE_POS_Y

    while running:
        # poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player_v -= G * dt
        player_y = min(player_y - player_v * dt, BASE_POS_Y)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and BASE_POS_Y == player_y:
            player_v = V_JUMP

        screen.fill("black")
        
        pygame.draw.line(screen, "blue", (0, BASE_POS_Y + PLAYER_RADIUS), (WIDTH, BASE_POS_Y + PLAYER_RADIUS), 4)
        pygame.draw.circle(screen, "green", (BASE_POS_X, player_y), PLAYER_RADIUS)

        pygame.display.flip()  # update screen

        dt = clock.tick(60) / 100

    pygame.quit()
