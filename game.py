import pygame, sys
from player import Player
from ball import Ball
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
playerA.rect.y = 160

playerB = Player(red, 10, 100)
playerB.rect.x = 690
playerB.rect.y = 160

ball = Ball(white, 10, 10)
ball.rect.x = 360
ball.rect.y = 180

#List of all sprites
allSpritesList = pygame.sprite.Group()

#Add sprites to list
allSpritesList.add(playerA)
allSpritesList.add(playerB)
allSpritesList.add(ball)

isRunning = True
clock = pygame.time.Clock()

#Initialise player scores
scoreA = 0
scoreB = 0

# ---------- Main Loop ------------
while isRunning:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: #Pressing the x Key will quit the game
                     isRunning=False  

    #Moving up and down
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        playerA.moveUp(5)
    if keys[pygame.K_s]:
        playerA.moveDown(5)
    if keys[pygame.K_UP]:
        playerB.moveUp(5)
    if keys[pygame.K_DOWN]:
        playerB.moveDown(5)    
    # --- Game logic
    allSpritesList.update()

    #Bouncing ball
    if ball.rect.x>=710:
        scoreA+=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        scoreB+=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>350:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<60:
        ball.velocity[1] = -ball.velocity[1] 

     #Detect collisions between the ball and the paddles
    if pygame.sprite.collide_mask(ball, playerA) or pygame.sprite.collide_mask(ball, playerB):
      ball.bounce()

    # --- Drawing code
    screen.fill(black)
    pygame.draw.line(screen, white, [359, 0], [359, 55], 5)
    pygame.draw.line(screen, white, [0, 55], [720, 55], 5)

    allSpritesList.draw(screen) 
    

     #Display scores:
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, blue)
    screen.blit(text, (250,10))
    text = font.render(str(scoreB), 1, red)
    screen.blit(text, (420,10))

    # --- Update
    pygame.display.flip()

    # --- Frame limit
    clock.tick(60)

    
pygame.quit