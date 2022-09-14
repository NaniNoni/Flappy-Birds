import pygame
import player

pygame.init()

WIDTH, HEIGHT = 800, 600

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
CLOCK = pygame.time.Clock()
run = True

WHITE = (255, 255, 255)

# Setting up the player
player = player.Player()
pygame.display.set_icon(player.texture)

def draw_window():
    WINDOW.fill(WHITE)
    WINDOW.blit(player.texture, (player.position.x, player.position.y))
    pygame.display.update()


def update():
    #Setting up deltatime
    deltatime = CLOCK.tick(999999999999999999999)
    
    player.position.y += player.velocity * deltatime
    player.velocity += player.acceleration * deltatime
    player.position.x += 0.25 * deltatime
    
    print(player.position.y)

while run:
    update()
    draw_window()
    
    if player.position.y >= HEIGHT:
        run = False
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.flap()
        

pygame.quit()