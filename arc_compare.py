import turtle as t
import math

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def arc2(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def one(t, r, angle):
    for i in range(0, 2):
        arc(t, r, angle)
        t.lt(180-angle)

def one2(t, r, angle):
    for i in range(0, 2):
        arc2(t, r, angle)
        t.lt(180-angle)

def stack_of_one(t, n, r, angle):
    for i in range(0, n):
        one(t, r, angle)
        t.lt(360/n)

def stack_of_one2(t, n, r, angle):
    for i in range(0, n):
        one2(t, r, angle)
        t.lt(360/n)


t.speed(0)
stack_of_one(t, 7, 60, 60)
t.penup()
t.fd(120)
t.pendown()
stack_of_one2(t, 7, 60, 60)
t.mainloop()