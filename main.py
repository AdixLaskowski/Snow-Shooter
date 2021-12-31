import pygame
from sys import exit
from Player import Player
from Snowman import Enemy
import random

def main():

    pygame.init()

    # Setting up window
    SCR_WIDTH = 900
    SCR_HEIGHT = 600

    window = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
    pygame.display.set_caption('SnowShooter')

    # Loading images
    BackgroundIMG = pygame.image.load('images/background.png')
    Panel = pygame.image.load('images/panel.png')

    GameOverIMG = pygame.image.load('images/gameOver.png')
    PlayAgainBTN = pygame.image.load('images/PlayAgainBTN.png')

    # game status
    game = True

    # Loading font
    fnt = pygame.font.SysFont('Arial', 24)

    # Creating player object
    player = Player()

    # Crating array for enemies
    enemies = []

    # Collision check

    def Collide(obj1, obj2):
        offset_x = obj2.pos_x - obj1.pos_x
        offset_y = obj2.pos_y - obj1.pos_y
        if - 20 < offset_x < 20 and -80 < offset_y < 15:
            return True


    # main loop
    while True:

        # Framerate
        pygame.time.Clock().tick(60)

        # basic events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


        window.fill((90, 150, 220))
        window.blit(BackgroundIMG, (0, 0))
        window.blit(Panel, (0, 0))

        # Display points and health status
        ScoreText = fnt.render(str(player.points), 1, (250, 250, 250))
        HealthText = fnt.render(str(player.health), 1, (250, 250, 250))

        window.blit(ScoreText, (560, 32))
        window.blit(HealthText, (310, 32))

        if game == True:

            # Player
            player.DrawIt(window)
            player.Move()

            # enemies

            r = random.randint(1, 30)

            if r == 3:
                enemies.append(Enemy())

            for enemy in enemies:
                enemy.DrawIt(window)
                enemy.Strike()

                if enemy.Die():
                    player.LoseHealth()
                    enemies.remove(enemy)

                for snow in player.snowballs:
                    if Collide(snow, enemy):
                        enemies.remove(enemy)
                        player.AddPoints()
                        player.snowballs.remove(snow)

        # Game Over
        if player.isGameOver() == True:
            game = False
            window.blit(GameOverIMG, (0, 0))
            PlayAgain = window.blit(PlayAgainBTN, (300, 150))

            # Restart game
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PlayAgain.collidepoint(event.pos):
                    player.Restart()
                    enemies = []
                    game = True

            
    
        pygame.display.update()

if __name__ == '__main__':
    main()