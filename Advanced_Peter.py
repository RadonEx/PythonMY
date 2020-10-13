import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000, 600))  # Установка размеров экрана

# Определим используемые цвета

Yellow = (255, 247, 15)
Blue = (66, 103, 237)
Grey = (219, 218, 204)
Milk_with_coffee = (227, 215, 109)
Green = (38, 207, 23)
Dark_Grey = (74, 73, 66)
Oxra = (196, 142, 4)
Dark_Oxra = (110, 86, 25)
Pink = (214, 21, 160)
Purple = (138, 28, 166)
Orange = (255,183,0)
Crimson = (214, 21, 21)
Emerald = (5, 122, 44)

# Рисуем фон

rect(screen, Blue, (0, 0, 1000, 600))  # Рисуем воду  *Первый слой

polygon(screen, Grey, ((0, 400), (0, 0), (1000, 0), (1000, 375), (0, 400)), 0)  # Облака

polygon(screen, Milk_with_coffee, ((0, 400), (0, 125), (600, 115), (1000, 135), (1000, 375), (0, 400)), 0)  # Небо

polygon(screen, Green, ((0, 400), (0, 250), (375, 230), (1000, 240), (1000, 375), (0, 400)), 0)  # Трава

polygon(screen, Dark_Grey, ((10, 258), (30, 250), (35, 230), (40, 200), (120, 175), (300, 120), (400, 50), (550, 110)
                               , (560, 130), (570, 200), (610, 250), (680, 200), (750, 128), (770, 100), (890, 200),
                               (1000, 260), (10, 258)), 0)  # Горы на заднем плане

polygon(screen, Oxra, ((0, 410), (0, 260), (20, 260), (50, 280), (65, 310), (160, 200), (200, 240), (290, 190)
                                , (300, 200), (490, 280), (750, 380), (940, 180), (1000, 420), (0, 410)), 0)  # Горы на среднем плане

polygon(screen, Dark_Oxra, ((0, 340), (150, 360), (200, 370), (210, 372), (225, 380), (240, 520), (300, 490),
                                (310, 480), (320, 460), (340, 400), (360, 440), (500, 500), (700, 490), (770, 400),
                                (780, 390), (790, 370), (820, 320), (825, 310), (880, 305), (920, 325), (1000, 400),
                                (1000, 600), (0, 600)), 0)  # Горы на переднем плане

circle(screen, Yellow, (700, 70), 60, 0)  # Солнце

def body(x, y, n, body_col):
    """
        Функция рисует тело птички на экране.
        x, y - координаты центра изображения
        n - размер изображения
        body_col - цвет, заданный в формате, подходящем для pygame.Color
    """
    polygon(screen, body_col,
            ((x, y), (x - 20 * n, y - 10 * n), (x - 21 * n, y - 11 * n), (x - 21.3 * n, y - 11.2 * n),
             (x - 20.6 * n, y - 11.6 * n),
             (x - 20 * n, y - 13 * n), (x - 2 * n, y - 6 * n), (x + 3 * n, y - 5.5 * n), (x + 6 * n, y - 7 * n),
             (x + 18 * n, y - 12 * n)
             , (x + 19 * n, y - 12.5 * n),
             (x + 19.5 * n, y - 12.6 * n), (x + 20.7 * n, y - 12.3 * n), (x + 21.8 * n, y - 12 * n),
             (x + 22 * n, y - 10 * n),
             (x + 22.1 * n, y - 9.6 * n), (x + 19.6 * n, y - 9 * n), (x, y)), 0)


def head(x, y, n, head_col, beak_col):
    """
        Функция голову птички на экране.
        x, y - координаты центра изображения
        n - размер изображения
        head_col - цвет, заданный в формате, подходящем для pygame.Color
    """
    circle(screen, head_col, (x, y - 4 * n), 7 * n)
    polygon(screen, beak_col, ((x, y - 4 * n), (x + 5 * n, y + 3 * n), (x - 2 * n, y), (x, y - 4 * n)), 0)


def eyes(x, y, n, rcl1, rcl2):
    """
        Функция рисует глаза птички на экране.
        x, y - координаты центра изображения
        n - размер изображения
        rcl1, rcl2 - цвета глаз, заданные в формате, подходящем для pygame.Color
    """
    circle(screen, rcl1, (x - 4 * n, y - 4 * n), 2 * n)
    circle(screen, rcl2, (x + 4 * n, y - 4 * n), 2 * n)
    circle(screen, (0, 0, 0), (x - 4 * n, y - 4 * n), 1 * n)
    circle(screen, (0, 0, 0), (x + 4 * n, y - 4 * n), 1 * n)


def bird(x, y, n, body_col, head_col, beak_col, rcl1, rcl2):
    """
        Функция рисует птичку на экране.
        x, y - координаты центра изображения
        n - размер изображения
        body_col - цвет тела птички, заданный в формате, подходящем для pygame.Color
        head_col - цвет головы птички, заданный в формате, подходящем для pygame.Color
        rcl1, rcl2 - цвета глаз, заданные в формате, подходящем для pygame.Color
    """
    body(x, y, n, body_col)
    head(x, y, n, head_col, beak_col)
    eyes(x, y, n, rcl1, rcl2)


bird(200, 200, 1, Pink, Purple, Orange, Crimson, Emerald)
bird(250, 230, 1, Pink, Purple, Orange, Crimson, Emerald)
bird(185, 170, 1, Pink, Purple, Orange, Crimson, Emerald)
bird(180, 260, 1, Pink, Purple, Orange, Crimson, Emerald)
bird(400, 400, 4, Pink, Purple, Orange, Crimson, Emerald)
bird(480, 460, 4, Pink, Purple, Orange, Crimson, Emerald)
bird(600, 160, 1, Pink, Purple, Orange, Crimson, Emerald)
bird(630, 170, 1, Pink, Purple, Orange, Crimson, Emerald)
bird(590, 140, 1, Pink, Purple, Orange, Crimson, Emerald)
bird(610, 190, 1, Pink, Purple, Orange, Crimson, Emerald)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
