import pygame
import random
import math

pygame.init()
width = 1920
height = 1080
display = pygame.display.set_mode((width,height))
pygame.display.update()

pygame.display.set_caption('Learning Project: Snake Game')
white = (255,255,255)
black = (0,0,0)
blue = (50,153,213)
red = (255,0,0)
yellow = (255,255,0)
green = (0,255,0)

snakeBlock = 10
snakeSpeed = 10

clock = pygame.time.Clock()

fontStyle = pygame.font.SysFont("verdania",50)
scoreFont = pygame.font.SysFont("arial",35,True)

def playerScore(score):
    value = scoreFont.render("Score: "+str(score),True,yellow)
    display.blit(value,[10,0])

def playerChar(snakeBlock, snakeList):
    for x in snakeList:
        pygame.draw.rect(display,blue,[x[0],x[1],snakeBlock,snakeBlock])

def message(msg,color):
    mesg = fontStyle.render(msg,True,color)
    position = mesg.get_rect(center=(width/2,height/2))
    display.blit(mesg,position)

def roundUp(x):
    return int(math.ceil(x/10.0))*10

def gameLoop():
    gameOver = False
    gameClose = False

    x1 = width/2
    y1 = height/2

    left = False
    right = False
    up = False
    down = False

    x1Change = 0
    y1Change = 0

    snakeList = []
    snakeLength = 1

    foodX = roundUp((random.randrange(0, width - snakeBlock) / 10.0) * 10.0)
    foodY = roundUp((random.randrange(0, height - snakeBlock) / 10.0) * 10.0)

    while gameOver != True:

        while gameClose == True:
            display.fill(black)
            message("Fission Mailed! Escape to Quit or Space to play again", red)
            playerScore(snakeLength-1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        gameOver = True
                        gameClose = False
                    if event.key == pygame.K_SPACE:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and left == False:
                    x1Change = -snakeSpeed
                    y1Change = 0
                    right = True
                    left = False
                    down = False
                    up = False
                if event.key == pygame.K_RIGHT and right == False:
                    x1Change = snakeSpeed
                    y1Change = 0
                    left = True
                    right = False
                    down = False
                    up = False
                if event.key == pygame.K_UP and up == False:
                    x1Change = 0
                    y1Change = -snakeSpeed
                    right = False
                    left = False
                    up = False
                    down = True
                if event.key == pygame.K_DOWN and down == False:
                    x1Change = 0
                    y1Change = snakeSpeed
                    left = False
                    right = False
                    up = True
                    down = False
                if event.key == pygame.K_ESCAPE:
                    gameOver = True

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            gameClose = True

        x1 += x1Change
        y1 += y1Change
        display.fill(black)

        pygame.draw.rect(display,white,[foodX,foodY,snakeBlock,snakeBlock])
        snakeHead = []
        snakeHead.append(x1)
        snakeHead.append(y1)
        snakeList.append(snakeHead)
        
        if len(snakeList) > snakeLength:
            del snakeList[0]
        
        for x in snakeList[:-1]:
            if x == snakeHead:
                gameClose = True
        
        playerChar(snakeBlock,snakeList)
        playerScore(snakeLength-1)

        pygame.display.update()

        if x1 == foodX and y1 == foodY:#borked
            foodX = roundUp((random.randrange(0, width - snakeBlock) / 10.0) * 10.0)
            foodY = roundUp((random.randrange(0, height - snakeBlock) / 10.0) * 10.0)
            snakeLength += 1

        clock.tick(30)

    pygame.quit
    quit()

gameLoop()