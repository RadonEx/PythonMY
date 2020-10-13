import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 100
screen = pygame.display.set_mode((1200, 600))  # Задаём размеры экрана

# Определим возможные цвета шариков
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

s = 0  # Число очков игрока
N = 5

def new_ball():  # Функция рисует шары произвольного цвета, рандомной величины, в разлчных точках экрана
    global x, y, r, color
    for i in range(0,N):
        x = randint(100, 700)
        y = randint(100, 500)
        r = randint(30, 50)
        color = COLORS[randint(0, 5)]
        circle(screen, color, (x, y), r)


def New_ballXYZ(x, y, r, color):  # Функция рисует шар заданого цвета по заданным координатам
    circle(screen, color, (x, y), r)


def score():  # Функция рисует счёт на экране
    inscription_font = pygame.font.SysFont('Arial Black', 64)
    inscription = inscription_font.render("Попал = " + str(s), 5, [255, 255, 0])
    screen.blit(inscription, (450, 0))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

# Зададим начальную скорость стартового шара и его положение
Vx1 = randint(-5, 5)
Vy1 = randint(-5, 5)
new_ball()


def click(event):
    global s, Vx1, Vy1
    if ((event.pos[0] - x) ** 2 + (event.pos[1] - y) ** 2) <= r ** 2:
        s += 1
        screen.fill(BLACK)
        pygame.display.update()
        new_ball()
        score()
        Vx1 = randint(-5, 5)
        Vy1 = randint(-5, 5)


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
    x += Vx1
    y += Vy1
    if (x + r > 1200) or (x < 0 + r):
        Vx1 = -Vx1
    if (y + r > 600) or (y < 0 + r):
        Vy1 = -Vy1
    screen.fill(BLACK)
    New_ballXYZ(x, y, r, color)
    score()
    pygame.display.update()

pygame.quit()
