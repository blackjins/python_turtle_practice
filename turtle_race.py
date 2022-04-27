import turtle
import random

color_list = ("red", "blue", "yellow", "BlueViolet", "brown", "beige", "green", "LightYellow", "LimeGreen", "SkyBlue" )
num_list = ("two", "thr", "for", "fiv", "six", "sev", "eig", "nin", "ten")
die =[1,2,3,4,5,6]

player_one = turtle.Turtle()
player_one.color(color_list[0])
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200,380)
player_two = player_one.clone()
player_two.color(color_list[1])
player_two.penup()
player_two.goto(-200,300)
player_thr = player_one.clone()
player_thr.color(color_list[2])
player_thr.penup()
player_thr.goto(-200,-100)
player_for = player_one.clone()
player_for.color(color_list[3])
player_for.penup()
player_for.goto(-200,-100)
player_fiv = player_one.clone()
player_fiv.color(color_list[4])
player_fiv.penup()
player_fiv.goto(-200,-100)
player_six = player_one.clone()
player_six.color(color_list[5])
player_six.penup()
player_six.goto(-200,-100)
player_sev = player_one.clone()
player_sev.color(color_list[6])
player_sev.penup()
player_sev.goto(-200,-100)
player_eig = player_one.clone()
player_eig.color(color_list[7])
player_eig.penup()
player_eig.goto(-200,-100)
player_nin = player_one.clone()
player_nin.color(color_list[8])
player_nin.penup()
player_nin.goto(-200,-100)
player_ten = player_one.clone()
player_ten.color(color_list[9])
player_ten.penup()
player_ten.goto(-200,-100)

player_list = [player_one, player_two, player_thr, player_for, player_fiv, player_six, player_sev, player_eig, player_nin, player_ten]


def player_setting(player, x, y):
    player.goto(x,y)
    player.pendown()
    player.circle(40)
    player.penup()
    player.goto(x-500,y+40)

player_setting(player_one, 300, 340)
player_setting(player_two, 300, 260)
player_setting(player_thr, 300, 180)
player_setting(player_for, 300, 100)
player_setting(player_fiv, 300, 20)
player_setting(player_six, 300, -60)
player_setting(player_sev, 300, -140)
player_setting(player_eig, 300, -220)
player_setting(player_nin, 300, -300)
player_setting(player_ten, 300, -380)

def checking():
    for i in range(10):
        if player_list[i].pos() >=(300,0):
            print ("Player ", i+1, "is winner!")
            return True
    return False
        
def dice(player):
    player.fd(20 * random.choice(die))
    if checking():
        return True
    return False

end = False
while not end:
    for i in player_list:
        if dice(i):
            end = True
            break

turtle.mainloop()