import pygame, sys
from player import Player

pygame.init()

#basic colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (239, 34, 20)
blue = (54, 89, 239)

#Open a window
screenSize = (720, 360)
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Pong")

playerA = Player(blue, 10, 100)
playerA.rect.x = 20
playerA.rect.y = 130

playerB = Player(red, 10, 100)
playerB.rect.x = 690
playerB.rect.y = 130

#List of all sprites
allSpritesList = pygame.sprite.Group()

#Add sprites to list
allSpritesList.add(playerA)
allSpritesList.add(playerB)

isRunning = True
clock = pygame.time.Clock()

# ---------- Main Loop ------------
while isRunning:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: #Pressing the x Key will quit the game
                     isRunning=False  


    # --- Game logic
    allSpritesList.update()

    # --- Drawing code
    screen.fill(black)
    pygame.draw.line(screen, white, [359, 0], [359, 360], 5)

    allSpritesList.draw(screen) 
    
    # --- Update
    pygame.display.flip()

    # --- Frame limit
    clock.tick(60)


pygame.quit