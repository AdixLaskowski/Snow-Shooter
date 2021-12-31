import pygame
import random

class Enemy:
    image = pygame.image.load('images/snowman.png')
    speed = 3.5
    pos_x = 900
    pos_y = 200

    def __init__(self):
        self.pos_y = random.randint(80, 500)

    def DrawIt(self, window):
        pygame.surface.Surface.blit(window, self.image, (self.pos_x, self.pos_y))

    def Strike(self):
        if self.pos_x > 0:
            self.pos_x -= self.speed

    def Die(self):
        if self.pos_x <= 5:
            return True