import turtle as t
from random import *
from random import randint
t.speed(1000)
t.penup()
t.goto(-200,200)
t.pendown()
t.width(9)
t.forward(400)
t.right(90)
t.forward(400)
t.right(90)
t.forward(400)
t.right(90)
t.forward(400)
t.right(90)
t.hideturtle()
t.isvisible()


x=0
y=0
p=70
dt=1
k = 11
ay=-10


Vx=p*random()
Vy=p*random()
Vx1=p*random()
Vy1=p*random()
Vx2=p*random()
Vy2=p*random()
Vx3=p*random()
Vy3=p*random()
Vx4=p*random()
Vy4=p*random()
Vx5=p*random()
Vy5=p*random()
Vx6=p*random()
Vy6=p*random()
Vx7=p*random()
Vy7=p*random()
Vx8=p*random()
Vy8=p*random()
Vx9=p*random()
Vy9=p*random()
Vx10=p*random()
Vy10=p*random()




d = 10000000


pool = [t.Turtle(shape='circle') for i in range(k)]
for unit in pool:
    unit.shapesize(0.5)
    unit.penup()
    unit.speed(100)
    unit.goto(randint(-190, 190), randint(-190, 190))


for i in range(d):
    (x, y) = pool[0].pos()
    x += Vx * dt
    y += Vy * dt + ay * dt ** 2 / 2
    Vy += ay * dt
    if x > 195 or x < -195:
        Vx = -Vx
        if x > 195:
            x = 195
        else:
            x = -195
    if y > 195 or y < -195:
        Vy = -Vy
        if y > 195:
            y = 195
        else:
            y = -195
    pool[0].goto(x, y)

    (x, y) = pool[1].pos()
    x += Vx1 * dt
    y += Vy1 * dt + ay * dt ** 2 / 2
    Vy += ay * dt
    if x > 195 or x < -195:
        Vx1 = -Vx1
        if x > 195:
            x = 195
        else:
            x = -195
    if y > 195 or y < -195:
        Vy1 = -Vy1
        if y > 195:
            y = 195
        else:
            y = -195
    pool[1].goto(x, y)

    (x, y) = pool[2].pos()
    x +=Vx2 * dt
    y +=Vy2 * dt + ay * dt ** 2 / 2
    Vy += ay * dt
    if x > 195 or x < -195:
        Vx2 = -Vx2
        if x > 195:
            x = 195
        else:
            x = -195
    if y > 195 or y < -195:
        Vy2 = -Vy2
        if y > 195:
            y = 195
        else:
            y = -195
    pool[2].goto(x, y)

    (x, y) = pool[3].pos()
    x += Vx3 * dt
    y += Vy3 * dt + ay * dt ** 2 / 2
    Vy += ay * dt
    if x > 195 or x < -195:
        Vx3 = -Vx3
        if x > 195:
            x = 195
        else:
            x = -195
    if y > 195 or y < -195:
        Vy3 = -Vy3
        if y > 195:
            y = 195
        else:
            y = -195
    pool[3].goto(x, y)

    (x, y) = pool[4].pos()
    x += Vx4 * dt
    y += Vy4 * dt + ay * dt ** 2 / 2
    Vy += ay * dt
    if x > 195 or x < -195:
        Vx4 = -Vx4
        if x > 195:
            x = 195
        else:
            x = -195
    if y > 195 or y < -195:
        Vy4 = -Vy4
        if y > 195:
            y = 195
        else:
            y = -195
    pool[4].goto(x, y)

    (x, y) = pool[5].pos()
    x += Vx5 * dt
    y += Vy5 * dt + ay * dt ** 2 / 2
    Vy += ay * dt
    if x > 195 or x < -195:
        Vx5 = -Vx5
        if x > 195:
            x = 195
        else:
            x = -195
    if y > 195 or y < -195:
        Vy5 = -Vy5
        if y > 195:
            y = 195
        else:
            y = -195
    pool[5].goto(x, y)

    (x, y) = pool[6].pos()
    x += Vx6 * dt
    y += Vy6 * dt + ay * dt ** 2 / 2
    Vy += ay * dt
    if x > 195 or x < -195:
        Vx6 = -Vx6
        if x > 195:
            x = 195
        else:
            x = -195
    if y > 195 or y < -195:
        Vy6 = -Vy6
        if y > 195:
            y = 195
        else:
            y = -195
    pool[6].goto(x, y)

    (x, y) = pool[7].pos()
    x += Vx7 * dt
    y += Vy7 * dt + ay * dt ** 2 / 2
    Vy += ay * dt
    if x > 195 or x < -195:
        Vx7 = -Vx7
        if x > 195:
            x = 195
        else:
            x = -195
    if y > 195 or y < -195:
        Vy7 = -Vy7
        if y > 195:
            y = 195
        else:
            y = -195
    pool[7].goto(x, y)

    (x, y) = pool[8].pos()
    x += Vx8 * dt
    y += Vy8 * dt + ay * dt ** 2 / 2
    Vy += ay * dt
    if x > 195 or x < -195:
        Vx8 = -Vx8
        if x > 195:
            x = 195
        else:
            x = -195
    if y > 195 or y < -195:
        Vy8 = -Vy8
        if y > 195:
            y = 195
        else:
            y = -195
    pool[8].goto(x, y)

    (x, y) = pool[9].pos()
    x += Vx9 * dt
    y += Vy9 * dt + ay * dt ** 2 / 2
    Vy += ay * dt
    if x > 195 or x < -195:
        Vx9 = -Vx9
        if x > 195:
            x = 195
        else:
            x = -195
    if y > 195 or y < -195:
        Vy9 = -Vy9
        if y > 195:
            y = 195
        else:
            y = -195
    pool[9].goto(x, y)

    (x, y) = pool[10].pos()
    x += Vx10 * dt
    y += Vy10 * dt + ay * dt ** 2 / 2
    Vy += ay * dt
    if x > 195 or x < -195:
        Vx10 = -Vx10
        if x > 195:
            x = 195
        else:
            x = -195
    if y > 195 or y < -195:
        Vy10 = -Vy10
        if y > 195:
            y = 195
        else:
            y = -195
    pool[10].goto(x, y)

t.exitonclick()