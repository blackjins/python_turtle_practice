import turtle as t
import math

def archi_spiral(t):
    for i in range(0, 600):
        vt = i / 40 * math.pi
        x = (vt * 5 + 5) * math.cos(vt)
        y = (vt * 5 + 5) * math.sin(vt)
        t.goto(x, y)
    return

archi_spiral(t)
t.mainloop