import pygame
from pygame.draw import *
import math as m

pygame.init()

FPS = 30
p=800
n=500
screen = pygame.display.set_mode((p, n))

rect(screen, (31,191,157), (0,n//2, p, n//2))
rect(screen, (135,255,255), (0,0, p, n//2))
def solar(i,r,p,x0,y0): #Рисуем солнышко. i -число лучей, r - радиус короны солнца, p - длина лучей. (x0,y0) - координаты центра
    for j in range(i):
        phi = 2 * m.pi/i*j
        a=x0+r*m.cos(phi)
        b=y0+r*m.sin(phi)
        x1=p*m.cos(phi)
        y1=p*m.sin(phi)
        x2=p*m.cos(m.pi/2-phi)
        y2=p*m.sin(m.pi/2-phi)
        A = [(a-x2,b+y2),(a+10*x1,b+10*y1),(a+x2,b-y2),(a-x2,b+y2)]
        polygon(screen, (251, 255, 0), A, 0)
def oblachko(x0,y0,m): #(x0,y0) - координаты центра, m - масштаб. m=1 полагается для R=20 облачков, 1 облачко из 5 тучек.
    r=int(20*m)
    a=x0
    b=y0+r
    circle(screen,(255, 255, 255),(a,b),r,0)
    circle(screen, (171, 171, 171), (a, b), r+1, 1)
    a=x0+r
    circle(screen, (255, 255, 255), (a, b), r, 0)
    circle(screen, (171, 171, 171), (a, b), r + 1, 1)
    a = x0 + 2 * r
    b = y0 + r
    circle(screen, (255, 255, 255), (a, b), r, 0)
    circle(screen, (171, 171, 171), (a, b), r + 1, 1)
    a = x0 + 3 * r
    b=y0+r-2
    circle(screen, (255, 255, 255), (a, b), r, 0)
    circle(screen, (171, 171, 171), (a, b), r + 1, 1)
    a = x0 + 2* r
    b = y0
    circle(screen, (255, 255, 255), (a, b), r, 0)
    circle(screen, (171, 171, 171), (a, b), r + 1, 1)
    a = x0 +r
    b = y0+1
    circle(screen, (255, 255, 255), (a, b), r, 0)
    circle(screen, (171, 171, 171), (a, b), r + 1, 1)
def dom_with_derevo(x0,y0,m): #Рисует домик с деревом, (x0,y0) - координаты верхней левой точки, m - масштаб.
    # Рисуем Дом
    p=int(150*m)
    B = [(x0, y0), (x0+ p, y0), (x0 + p // 2, y0 - p // 2), (x0, y0)]
    polygon(screen, (250, 12, 12), B, 0) #Крыша
    rect(screen, (255, 128, 74), (x0, y0, p,p//1.2), 0) #Тело домика
    rect(screen, (10, 6, 6), (x0, y0, p, p // 1.2), 2)
    B=[(x0,y0),(x0+p,y0),(x0+p//2,y0-p//2),(x0,y0)]
    polygon(screen, (10, 6, 6), B, 2)
    rect(screen, (212, 255, 41), (x0 + p // 3, y0 + p // 3 - int(p * 0.05), p // 3, p // 1.2 // 3), 0)
    rect(screen, (10, 6, 6), (x0+p//3, y0+p//3-int(p*0.05), p//3,p//1.2//3), 2)
    line(screen,(10, 6, 6),(x0+p//3+p//6,y0+p//3-int(p*0.05)),(x0+p//3+p//6,y0+p//3-int(p*0.05)+p//1.2//3),2)
    line(screen,(10, 6, 6),(x0+p//3,y0+p//3-int(p*0.05)+p//1.2//6),(x0+2*p//3,y0+p//3-int(p*0.05)+p//1.2//6),2)
    #Рисуем дерево
    rect(screen,(148, 44, 0),(x0+p+p//2,y0+2*p//3,p//9,p//1.7), 0) #Тело дерева
    rect(screen, (10, 6, 6), (x0 + p + p // 2, y0 + 2 * p // 3, p // 9, p // 1.7), 1)
    x1=x0 + p + p // 2 # координаты вершины дерева
    y1=y0 + 2 * p // 3 #
    circle(screen, (17, 130, 7), (x1-p//12, y1-p//8), int(p//5.6), 0)
    circle(screen, (10, 6, 6), (x1 - p // 12, y1 - p // 8), int(p // 5.6)+1, 1)
    circle(screen, (17, 130, 7), (x1 + p // 6, y1 - p // 8++int(0.02*p)), int(p // 5), 0)
    circle(screen, (10, 6, 6), (x1 + p // 6, y1 - p // 8+int(0.02*p)), int(p // 5) + 1, 1)
    circle(screen, (17, 130, 7), (x1 - p // 20, y1 - int(p // 2.6)), int(p // 5), 0)
    circle(screen, (10, 6, 6), (x1 - p // 20, y1 - int(p // 2.6)), int(p // 5), 1)
    circle(screen, (17, 130, 7), (x1 + p // 5, y1 - int(p // 2.7)), int(p // 5), 0)
    circle(screen, (10, 6, 6), (x1 + p // 5, y1 - int(p // 2.7)), int(p // 5), 1)
    circle(screen, (17, 130, 7), (x1+p//14, y1 - int(p // 1.75)), int(p / 5.5), 0)
    circle(screen, (10, 6, 6), (x1+p//14, y1 - int(p // 1.75)), int(p / 5.5), 1)

solar(60,0,7,80,80) #Солнышко
dom_with_derevo(100,300,0.95)
dom_with_derevo(510,250,0.58)
oblachko(200,100,1.2)
oblachko(400,120,0.9)
oblachko(620,50,1.4)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()