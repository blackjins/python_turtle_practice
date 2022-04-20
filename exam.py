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




t.speed(0)
arc(t, 60 , 150)
t.penup()
t.home()
t.pendown()
arc2(t, 60, 150)
t.mainloop()