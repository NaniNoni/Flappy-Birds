import pygame
import os

class Player:
    texture_path = os.path.join(os.path.join("assets", "textures"), "player.png")
    texture = pygame.image.load(texture_path)
    texture = pygame.transform.scale(texture, (50, 50))
    position = pygame.Vector2(300, 300)
    velocity = 0
    acceleration = 0.006
    
    flap_size = 1.2
    
    def flap(self):
        self.velocity = -self.flap_size