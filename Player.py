import pygame

class Snow:
    image = pygame.image.load('images/snow.png')
    speed = 40
    pos_x = 10
    pos_y = 200

    def __init__(self, pos_y):
        self.pos_y = pos_y + 30

    def DrawIt(self, window):
        pygame.surface.Surface.blit(window, self.image, (self.pos_x, self.pos_y))

    def Fly(self):
        self.pos_x += self.speed

class Player:
    image = pygame.image.load('images/player.png')
    speed = 12
    pos_x = 10
    pos_y = 200
    points = 0
    health = 100
    snowballs = []
    cooldown = 60
    cooldown_time = 10

    def CooldownHandler(self):
        if self.cooldown != 0:
            self.cooldown -= 1

    def DrawIt(self, window):
        self.CooldownHandler()

        for snow in self.snowballs:
            snow.DrawIt(window)
            snow.Fly()
            if snow.pos_x >= 900:
                self.snowballs.remove(snow)
        
        pygame.surface.Surface.blit(window, self.image, (self.pos_x, self.pos_y))

    def Move(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and self.pos_y > 70:
            self.pos_y -= self.speed

        if keys[pygame.K_s] and self.pos_y < 500:
            self.pos_y += self.speed

        if keys[pygame.K_SPACE]:
            if self.cooldown == 0:
                self.Shoot()

    def Shoot(self):
        self.snowballs.append(Snow(self.pos_y))
        self.cooldown = self.cooldown_time

    def AddPoints(self):
        self.points += 10

    def LoseHealth(self):
        self.health -= 10

    def isGameOver(self):
        if self.health < 1:
            return True

    def Restart(self):
        self.points = 0
        self.health = 100