import pygame, sys
pygame.init()
width=500
height=500
size = width, height

screen = pygame.display.set_mode(size)
x1 = 2
x2 = 2
x3 = 10
xChange = 0
def xChanger(x):
    global x1,x2,x3
    x1 += x
    x2 += x
    x3 += x
y1 = 450
y2 = 460
y3 = 452.5
yChange = 0
def yChanger(y):
    global y1,y2,y3
    y1 += y
    y2 += y
    y3 += y    
y = 1
def boid(): return pygame.draw.polygon(screen, (255,0,0), ((x1,y1),(x2,y2),(x3,y3)))

run = True
while run: 
    pygame.time.delay(1)
    for event in pygame.event.get():
        xChange =1
        xChanger(xChange)
        yChange =-1
        yChanger(yChange)
        if event.type == pygame.QUIT:
             run = False
    #screen.fill((255,255,255))
    boid()
    pygame.display.update()
pygame.quit()