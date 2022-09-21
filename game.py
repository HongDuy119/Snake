
import pygame,random,time,sys
pygame.init()   
#load image
m = 20
Imgbody = pygame.transform.scale(pygame.image.load('body.jpg'),(m,m))
Imghead = pygame.transform.scale(pygame.image.load('head.jpg'),(m,m))
Imgfood = pygame.transform.scale(pygame.image.load('food.png'),(m,m))
# create window
gameSurface = pygame.display.set_mode((735,475))
pygame.display.set_caption("HongDuy")
#color
red = pygame.Color(255,0,0)
blue = pygame.Color(65,105,255)
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
gray = pygame.Color(128,128,128)
#declare 
snakepos = [100,60]
snakebody = [[100,60],[80,60],[60,60]]
foodx = random.randrange(1,71)
foody = random.randrange(1,45)
if foodx%2==1: foodx += 1
if foody%2==1 : foody += 1
foodpos =[foodx*10 , foody*10]
foodflat = True
direction = 'RIGHT'
changeto = direction
score = 0
#function gameover and show score 
def game_over():
    gfont = pygame.font.SysFont('cosolas',40)
    gsurf = gfont.render('Game over!',True,red)
    grect = gsurf.get_rect()
    grect.midtop = (360,150)
    gameSurface.blit(gsurf,grect)
    show_score(0)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
def show_score(choice = 1):
    sfont = pygame.font.SysFont('cosolas',20)
    ssurf = sfont.render('Score: {0}'.format(score),True,black)
    srect = ssurf.get_rect()
    if choice == 1:
        srect.midtop = (350,-1)
    else:
        srect.midtop = (360,230)
    gameSurface.blit(ssurf,srect)
    
# main for
while True:
    pygame.time.delay(200)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
    # gameSurface.blit(Imgbody,pygame.Rect(50,50,m,m))
    #handle key
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            changeto = 'RIGHT'
        if event.key == pygame.K_LEFT:
            changeto = 'LEFT'
        if event.key == pygame.K_UP:
            changeto = 'UP'
        if event.key == pygame.K_DOWN:
            changeto = 'DOWN'
        if event.key == pygame.K_ESCAPE:
            pygame.event.post(pygame.event.Event(pygame.QUIT))
    #direction
    if changeto == 'RIGHT' and not direction== 'LEFT':
        direction = 'RIGHT'
    if changeto == 'LEFT' and not direction== 'RIGHT':
        direction = 'LEFT'
    if changeto == 'UP' and not direction== 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and not direction== 'UP':
        direction = 'DOWN'
    # update location
    if direction == 'RIGHT':
        snakepos[0] += m
    if direction == 'LEFT':
        snakepos[0] -= m
    if direction == 'DOWN':
        snakepos[1] += m
    if direction == 'UP':
        snakepos[1] -= m
    # eat food
    snakebody.insert(0,list(snakepos))
    if snakepos[0] == foodpos[0] and snakepos[1]==foodpos[1]:
        score += 10
        foodflat = False
    else:
        snakebody.pop()
    # creat eat
    if foodflat == False:
        foodx = random.randrange(1,71)
        foody = random.randrange(1,45)
        if foodx%2==1: foodx += 1
        if foody%2==1 : foody += 1
        foodpos =[foodx*10 , foody*10]
        foodflat = True
    # update in windown
    gameSurface.fill(white)
    for pos in snakebody:
        gameSurface.blit(Imgbody,pygame.Rect(pos[0],pos[1],m,m))
    gameSurface.blit(Imghead,pygame.Rect(snakebody[0][0],snakebody[0][1],m,m))
    gameSurface.blit(Imgfood,pygame.Rect(foodpos[0],foodpos[1],m,m))
    # handle over scope
    if snakepos[0]>710 or snakepos[0]<10:
        game_over()
    if snakepos[1]>450 or snakepos[1]<10:
        game_over()
    for b in snakebody[1:]:
        if snakepos[0] == b[0] and snakepos[1] == b[1]:
            game_over()
    # border
    pygame.draw.rect(gameSurface,gray,(10,10,715,455),2)
    show_score()
    pygame.display.flip()