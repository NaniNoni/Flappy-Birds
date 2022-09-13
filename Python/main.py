from turtle import width
import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
CLOCK = pygame.time.Clock()

run = True

WHITE = (255, 255, 255)

def draw_window():
    WINDOW.fill(WHITE)
    pygame.display.update()

while run:
    draw_window()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()