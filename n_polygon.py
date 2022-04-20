import turtle as t
import math

def polygon(t, n, r):
    angle = 360/n
    for i in range(0, n):
        isosceles(t, r ,angle/2)
        t.rt(angle)
    return

def isosceles(t, r, angle):
    y = r * math.sin(angle * math.pi / 180)

    t.rt(angle)
    t.fd(r)
    t.lt(90+angle)
    t.fd(2*y)
    t.lt(90+angle)
    t.fd(r)
    t.lt(180-angle)

polygon(t, 5, 50)
t.penup()
t.home()
t.fd(100)
t.pendown()
polygon(t, 6, 50)
t.penup()
t.fd(100)
t.pendown()
polygon(t, 7, 50)
t.mainloop()