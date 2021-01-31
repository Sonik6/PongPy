import pygame, sys
pygame.init()

#basic colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (239, 34, 20)
blue = (54, 89, 239)

#Open a window
screenSize = (720, 360)
screen = pygame.display.set_mode()
pygame.display.set_caption("Pong")


isRunning = True
clock = pygame.time.Clock()

#----------Main Loop------------
while isRunning:
    #Main event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False