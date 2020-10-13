import pygame
import math as m
from pygame.draw import *
from random import randint

pygame.init()

FPS = 150
screen = pygame.display.set_mode((1200, 600))  # Задаём размеры экрана

# Определим цвета, используемые в работе
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
CYANN = (110, 238, 255)
WHITE = (255, 255, 255)
GREY = (171, 171, 171)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

sc = 0  # Счёт игрока
s = 0  # Число очков без штрафа за промахи
mimo = 0   # Число штрафов
N = 5  # Количество шаров на экране
K = 4 # Количество облаков на экране
V = 4  # Линейная скорость шаров и четверть линейной скорости гравитационных центров обращения облаков
W = 2  # Угловая скорость обращения облаков X100


def new_ball():
    """
        Функция рисует шары произвольного цвета, рандомной величины, в разлчных точках экрана.
        Задаёт им произвольную линейную скорость по осям и передаёт данные в список
    """
    global x, y, r, color, Vx, Vy, Array
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)
    Vx = randint(-V, V)
    Vy = randint(-V, V)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    Array = [x, y, r, color, Vx, Vy]


def new_cloud(m):
    """
       Рисует облако в произвольной точке экрана и задаёт случайные значения для скорости центра обращения
       угловой скорости обращения, радиуса кривизны и записывает данные облака в список Cloud
    """
    global Cloud
    r = int(20 * m)
    x0 = randint(100, 700)
    y0 = randint(100, 500)
    Vx = int(randint(-V, V) // 4)
    Vy = int(randint(-V, V) // 4)
    w = randint(-W, W) / 100
    varphi = 0  # Начальная фаза колебаний
    xr = randint(100, 800)
    yr = randint(100, 400)
    R = randint(50, 150)  # Радус кривизны
    a = x0
    b = y0 + r
    circle(screen, WHITE, (a, b), r, 0)
    circle(screen, GREY, (a, b), r + 1, 1)
    a = x0 + r
    circle(screen, WHITE, (a, b), r, 0)
    circle(screen, GREY, (a, b), r + 1, 1)
    a = x0 + 2 * r
    b = y0 + r
    circle(screen, WHITE, (a, b), r, 0)
    circle(screen, GREY, (a, b), r + 1, 1)
    a = x0 + 3 * r
    b = y0 + r - 2
    circle(screen, WHITE, (a, b), r, 0)
    circle(screen, GREY, (a, b), r + 1, 1)
    a = x0 + 2 * r
    b = y0
    circle(screen, WHITE, (a, b), r, 0)
    circle(screen, GREY, (a, b), r + 1, 1)
    a = x0 + r
    b = y0 + 1
    circle(screen, WHITE, (a, b), r, 0)
    circle(screen, GREY, (a, b), r + 1, 1)
    Cloud = [x0, y0, xr, yr, w, R, varphi, Vx, Vy]


def cloud(x0, y0, m):
    """
        Рисуем облако:
        (x0,y0) - координаты центра
        m - масштаб, в данной работе полагается равным 1 и не меняется по ходу исполнения программы
    """
    r = int(20 * m)
    a = x0
    b = y0 + r
    circle(screen, WHITE, (a, b), r, 0)
    circle(screen, GREY, (a, b), r + 1, 1)
    a = x0 + r
    circle(screen, WHITE, (a, b), r, 0)
    circle(screen, GREY, (a, b), r + 1, 1)
    a = x0 + 2 * r
    b = y0 + r
    circle(screen, WHITE, (a, b), r, 0)
    circle(screen, GREY, (a, b), r + 1, 1)
    a = x0 + 3 * r
    b = y0 + r - 2
    circle(screen, WHITE, (a, b), r, 0)
    circle(screen, GREY, (a, b), r + 1, 1)
    a = x0 + 2 * r
    b = y0
    circle(screen, WHITE, (a, b), r, 0)
    circle(screen, GREY, (a, b), r + 1, 1)
    a = x0 + r
    b = y0 + 1
    circle(screen, WHITE, (a, b), r, 0)
    circle(screen, GREY, (a, b), r + 1, 1)


def score():
    """
            Функция выводит на экран очки игрока и условия игры
    """
    polygon(screen, CYANN, [(0, 0), (300, 0), (300, 110), (0, 110)])
    rect(screen, YELLOW, (0, 0, 300, 110), 3)
    rect(screen, YELLOW, (0, 0, 150, 110), 3)
    rect(screen, YELLOW, (0, 0, 150, 45), 3)
    inscription_font = pygame.font.SysFont('Arial Black', 12)
    inscription = inscription_font.render("Попал: " + str(s), 5, BLACK)
    inscription1 = inscription_font.render("Мимо: " + str(mimo), 5, BLACK)
    inscription2 = inscription_font.render("Счёт: " + str(sc), 5, BLACK)
    inscription3 = inscription_font.render("За промахи будут", 5, BLACK)
    inscription4 = inscription_font.render("вычитаться очки!", 5, BLACK)
    inscription5 = inscription_font.render("При попадании по", 5, BLACK)
    inscription6 = inscription_font.render("облакам +2 очка", 5, BLACK)
    screen.blit(inscription, (4, 0))
    screen.blit(inscription1, (4, 20))
    screen.blit(inscription2, (4, 60))
    screen.blit(inscription3, (154, 0))
    screen.blit(inscription4, (154, 20))
    screen.blit(inscription5, (154, 40))
    screen.blit(inscription6, (154, 60))


D = []  # Список, содержащий параметры шаров
C = []  # Список, содержащий параметры облаков


def start():
    """
        Функция задаёт стартовые параметры для облаков и шаров до начала игры
    """
    for i in range(0, N):
        new_ball()
        D.append(Array)
    for h in range(0, K):
        new_cloud(1)
        C.append(Cloud)


def click(event):
    """
        Функция обрабатывает нажатие пользователя на элементы игры
        Если одновременно попасть по 2 шарам/облакам, в рейтинг игрока будет засчитано лишь 1 попадание
        по облаку. Из-за сложной формы облака, критерием попадания считается окружность, огибающая большую
        часть облака. Крайние области облачка при этом не охватываются.
    """
    global s, mimo, sc
    Mim = True
    p = 0  # Переменная отвечает за число попаданий по шарам.
    z = 0  # Переменная отвечает за число попаданий по облакам.
    for j in range(0, N):
        if ((event.pos[0] - D[j][0]) ** 2 + (event.pos[1] - D[j][1]) ** 2) <= D[j][2] ** 2:
            p += 1
            pygame.display.update()
            D[j][0] = randint(100, 700)
            D[j][1] = randint(100, 500)
            D[j][4] = randint(-V, V)
            D[j][5] = randint(-V, V)
            D[j][3] = COLORS[randint(0, 5)]
            Mim = False
    for h in range(0, K):
        if ((event.pos[0] - (C[h][0]+25)) ** 2 + (event.pos[1] - (C[h][1]+18)) ** 2) <= 35 ** 2:
            z += 1
            pygame.display.update()
            C[h][0] = randint(100, 700)
            C[h][1] = randint(100, 500)
            C[h][2] = randint(100, 800)
            C[h][3] = randint(100, 400)
            C[h][4] = randint(-W, W) / 100
            C[h][5] = randint(50, 150)
            C[h][7] = int(randint(-V, V) // 4)
            C[h][8] = int(randint(-V, V) // 4)
            Mim = False
    if Mim:
        mimo += 1
    if p > 0 and z == 0 :
        s += 1
    elif p == 0 and z > 0:
        s += 2
    elif p > 0 and z > 0:
        s += 2
    sc = s - mimo


start()  # Начало работы основной программы


pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
    screen.fill(BLACK)  # Обновление экрана
    # Рисуем дивжение шаров
    for i in range(0, N):
        D[i][0] += D[i][4]
        D[i][1] += D[i][5]
        # Условия для отражения линейных скоростей шаров со сменой цвета при ударе о стену
        if (D[i][0] + D[i][2] > 1200) or (D[i][0] < 0 + D[i][2]):
            D[i][4] = -D[i][4]
            D[i][3] = COLORS[randint(0, 5)]
        if (D[i][1] + D[i][2] > 600) or (D[i][1] < 0 + D[i][2]):
            D[i][5] = -D[i][5]
            D[i][3] = COLORS[randint(0, 5)]
        circle(screen, D[i][3], (D[i][0], D[i][1]), D[i][2])
    # Рисуем движение облаков в виде суммы поступательного и колебательного движений
    for i in range(0, K):
        C[i][2] += C[i][7]
        C[i][3] += C[i][8]
        C[i][6] += C[i][4]
        C[i][0] = C[i][2] + int(C[i][5] * m.cos(C[i][6]))
        C[i][1] = C[i][3] + int(C[i][5] * m.sin(2 * C[i][6]))
        # Условия для отражения линейных скоростей центров обращения облаков
        if (C[i][0] + 60 > 1200) or (C[i][0] - 30 < 0):
            C[i][7] = -C[i][7]
        if (C[i][1] + 30 > 600) or (C[i][1] - 30 < 0):
            C[i][8] = -C[i][8]
        # Условия для отражения угловых скоростей для облаков
        if (C[i][0] + 60 > 1200) or (C[i][0] - 30 < 0):
            C[i][4] = -C[i][4]
        if (C[i][1] + 30 > 600) or (C[i][1] - 30 < 0):
            C[i][4] = -C[i][4]
        cloud(C[i][0], C[i][1], 1)
    score()  # Выводим обновлённую таблицу счёта
    pygame.display.update()
pygame.quit()
