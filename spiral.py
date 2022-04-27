import turtle
import math
wn = turtle.Screen()
wn.bgcolor("lightyellow")
bob = turtle.Turtle()
bob.shape("turtle")        # 화살촉 대신 거북이 모양 선택
bob.color("blue")

def whirl_turtle(t):
    t.penup()
    speed = 0
    for i in range(30):
        t.stamp()             
        speed += 3
        t.forward(speed)      
        t.right(25)            
    return

whirl_turtle(bob)


wn.mainloop()