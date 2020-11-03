from random import randrange as rnd, choice
import tkinter as tk
import math
import time

# print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)
k = 0.04  # Вязкость среды
l = 0.7  # Восстановление энергии при ударе
t = 0.04 # FPS
g = 10
V = 2 # Скорость целей

class ball():
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball
        Args:
            x - начальное положение мяча по горизонтали
            y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = 10

    def set_coords(self):
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self):
        """
            Переместить мяч по прошествии единицы времени.
            Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
            self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
            и стен по краям окна (размер окна 800х600).
        """
        canv.delete(self.id)
        self.x += self.vx
        self.y -= self.vy
        self.vy -= g * t + k * self.vy
        self.vx -= k * self.vx

        if self.x + self.r > 800 or self.x - self.r < 0:
            self.vx = l * -self.vx
            self.x += self.vx
        if self.y + self.r > 600 or self.y - self.r < 0:
            self.vy = l * - self.vy
            self.y -= self.vy
        if (-0.5 <= self.vx <= 0.5) and (590 <= self.y + self.r <= 605) and (-0.5 <= self.vy <= 0.5):
            self.vy = 0
            self.vx = 0
        if self.vx == 0 and self.vy == 0 and self.live > 0:
            self.live -= 1

        if self.live > 0:
            self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
            )


    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (self.r + obj.r) ** 2:
            return True
        return False


class gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20, 450, 50, 420, width=7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class target():
    def __init__(self):
        self.points = 0
        self.vx = 0
        self.vy = 0
        self.live = 1
        self.id = canv.create_oval(0, 0, 0, 0)
        #self.id_points = canv.create_text(30, 30, text=self.points, font='28')
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        vx = self.vx = rnd(V,3*V)
        y = self.y = rnd(300, 550)
        vy = self.vy = rnd(V,3*V)
        r = self.r = rnd(2, 50)
        color = self.color = 'yellow'
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        #canv.itemconfig(self.id_points, text=self.points)

    def move(self):
        """
            Переместить мяч по прошествии единицы времени.
            Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
            self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
            и стен по краям окна (размер окна 800х600).
        """
        canv.delete(self.id)
        self.x += self.vx
        self.y -= self.vy

        if self.x + self.r > 800 or self.x - self.r < 0:
            self.vx = l * -self.vx
            self.x += self.vx
        if self.y + self.r > 600 or self.y - self.r < 0:
            self.vy = l * - self.vy
            self.y -= self.vy


        if self.live > 0:
            self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
            )


t1 = target()
t2 = target()
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
bullet = 0
balls = []


def new_game(event=''):
    global gun, t1,t2, screen1, balls, bullet
    t2.new_target()
    t1.new_target()
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    t1.live = 1
    t2.live = 1
    while t1.live or t2.live or OK != 0:
        t1.move()
        t2.move()
        p = t1.points + t2.points
        for b in balls:
            b.move()
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
                canv.create_rectangle(0, 0, 60, 60, fill="white", outline="white")
                canv.itemconfig(screen1, text='Вы уничтожили цель 1 за ' + str(bullet) + ' выстрелов')

            if b.hittest(t2) and t2.live:
                t2.live = 0
                t2.hit()
                canv.itemconfig(screen1, text='Вы уничтожили цель 2 за ' + str(bullet) + ' выстрелов')
                canv.create_rectangle(0, 0, 60, 60, fill="white", outline="white")

            if t2.live == 0 and t1.live == 0:
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
        if t1.points + t2.points != p:
            canv.create_text(30, 30, text=t1.points + t2.points, font='28')
        OK = 0
        for k in balls:
            if k.live != 0:
                OK += 1
        canv.update()
        time.sleep(t)
        g1.targetting()
        g1.power_up()
        gun.f2_power = 0
    canv.itemconfig(screen1, text='')
    canv.delete(gun)
    root.after(new_game(), 750)


new_game()
mainloop()

