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


isRunning = True
clock = pygame.time.Clock()

# ---------- Main Loop ------------
while isRunning:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False


    # --- Game logic

    # --- Drawing code
    screen.fill(black)
    pygame.draw.line(screen, white, [359, 0], [359, 360], 5)
    
    # --- Update
    pygame.display.flip()

    # --- Frame limit
    clock.tick(60)


pygame.quit