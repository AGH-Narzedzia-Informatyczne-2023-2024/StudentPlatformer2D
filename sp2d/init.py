import pygame

def main():

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0
    v = 0
    G = 2
    V_JUMP = 40 
    BASE_POS = screen.get_height() * 2 / 3

    player_pos = pygame.Vector2(screen.get_width() / 2 - 500, BASE_POS)


    while running:
        # poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        v -= G*dt
        player_pos.y = min(player_pos.y - v*dt, BASE_POS) 

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and BASE_POS == player_pos.y:
            v=V_JUMP
            
        # if keys[pygame.K_s]:
        #     player_pos.y += 300 * dt
        # if keys[pygame.K_a]:
        #     player_pos.x -= 300 * dt
        # if keys[pygame.K_d]:
        #     player_pos.x += 300 * dt

        pygame.display.flip()


        screen.fill("black")
        
        pygame.draw.line(screen, "blue", (0,BASE_POS+42), (screen.get_width(), BASE_POS+42), 4)
        pygame.draw.circle(screen, "green", player_pos, 40)

        dt = clock.tick(60) / 10

    pygame.quit()