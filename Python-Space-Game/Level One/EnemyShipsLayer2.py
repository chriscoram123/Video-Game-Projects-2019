"""
@author: Christopher S Coram
Python Space Game / Level One / Enemy Ships Layer 2 / Module
7-5-2019 2:03PM
"""
# -------- IMPORTS --------
import pygame

# -------- PROGRAM VARIABLES --------
pygame.init()
# Open window
size = [800, 600]
screen = pygame.display.set_mode(size)
blue = (0,0,255)

# Background variable
background_image = pygame.image.load("SPoW_82318_01.png")

# Total enemy ships
# Ship one
EnemyShipOne = pygame.image.load("alien1.png").convert()
EnemyShipOne = pygame.transform.scale(EnemyShipOne, (80,80))
# Ship Two
EnemyShipTwo = pygame.image.load("alien1.png").convert()
EnemyShipTwo = pygame.transform.scale(EnemyShipTwo, (80,80))
# Ship Three
EnemyShipThree = pygame.image.load("alien1.png").convert()
EnemyShipThree = pygame.transform.scale(EnemyShipThree, (80,80))
# Ship Four
EnemyShipFour = pygame.image.load("alien1.png").convert()
EnemyShipFour = pygame.transform.scale(EnemyShipFour, (80,80))
# Ship Five
EnemyShipFive = pygame.image.load("alien1.png").convert()
EnemyShipFive = pygame.transform.scale(EnemyShipFive, (80,80))
# Ship Six
EnemyShipSix = pygame.image.load("alien1.png").convert()
EnemyShipSix = pygame.transform.scale(EnemyShipSix, (80,80))

# Enemy ship L2 x, y coordinates for bullets....
# Enemy ship y coordinates
ship_ycord = 100
ship_ycord2 = 100
ship_ycord3 = 100
ship_ycord4 = 100
ship_ycord5 = 100
ship_ycord6 = 100
# Enemy ship x coordinates
ship_xcord = 40
ship_xcord2 = 120
ship_xcord3 = 200
ship_xcord4 = 520
ship_xcord5 = 600
ship_xcord6 = 680


# Enemy L2 bullets, x y coordinates
# Bullet y coordinates
ship_ycord_rect = 200
ship_ycord_rect2 = 200
ship_ycord_rect3 = 200
ship_ycord_rect4 = 200
ship_ycord_rect5 = 200
ship_ycord_rect6 = 200
# Bullet x coordinates
ship_xcord_rect = 70
ship_xcord_rect2 = 150
ship_xcord_rect3 = 230
ship_xcord_rect4 = 550
ship_xcord_rect5 = 630
ship_xcord_rect6 = 710

# Rect variables for Enemy ship L2 Bullets
EL2B_ship1 = pygame.Rect(ship_xcord_rect, ship_ycord_rect, 20, 10)
EL2B_ship2 = pygame.Rect(ship_xcord_rect2, ship_ycord_rect3, 20, 10)
EL2B_ship3 = pygame.Rect(ship_xcord_rect3, ship_ycord_rect3, 20, 10)
EL2B_ship4 = pygame.Rect(ship_xcord_rect4, ship_ycord_rect4, 20, 10)
EL2B_ship5 = pygame.Rect(ship_xcord_rect5, ship_ycord_rect5, 20, 10)
EL2B_ship6 = pygame.Rect(ship_xcord_rect6, ship_ycord_rect6, 20, 10)

# Function loads rect objs on screen when called in main file
def L2B_load():
    pygame.draw.rect(screen, blue, EL2B_ship1)
    pygame.draw.rect(screen, blue, EL2B_ship2)
    pygame.draw.rect(screen, blue, EL2B_ship3)
    pygame.draw.rect(screen, blue, EL2B_ship4)
    pygame.draw.rect(screen, blue, EL2B_ship5)
    pygame.draw.rect(screen, blue, EL2B_ship6)
    pygame.display.update()
###################

# -------- CLASSES
class LayerTwo():
    def __init__(self):
        print("Testing when called upon")

    def EnemyLayer(self):
        # Spaceship One
        screen.blit(EnemyShipOne, (ship_xcord,ship_ycord)) # updates screen with enemy ship
        # Spaceship Two
        screen.blit(EnemyShipTwo, (ship_xcord2,ship_ycord2)) # updates screen with enemy ship
        # Spaceship Three
        screen.blit(EnemyShipThree, (ship_xcord3,ship_ycord3)) # updates screen with enemy ship
        # Spaceship Four
        screen.blit(EnemyShipFour, (ship_xcord4,ship_ycord4)) # updates screen with enemy ship
        # Spaceship Five
        screen.blit(EnemyShipFive, (ship_xcord5,ship_ycord5)) # updates screen with enemy ship
        # Spaceship Six
        screen.blit(EnemyShipSix, (ship_xcord6,ship_ycord6)) # updates screen with enemy ship


    def bullet_load(self):
        L2B_load()
