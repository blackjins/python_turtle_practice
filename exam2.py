import turtle
import random

color_list = ("red", "blue", "yellow", "BlueViolet", "brown", "beige", "green", "LightYellow", "LimeGreen", "SkyBlue" )
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

def checking():
    for i in player_list:
        if i.pos() >=(300,0):
            print (i, "is winner!")
            break
        
def dice(player):
    player.fd(20 * random.choice(die))

while True:
    for i in player_list:
        dice(i)
        checking()




for i in range(20):
     if player_one.pos() >= (300,100):
             print("Player One Wins!")
             break
     elif player_two.pos() >= (300,-100):
             print("Player Two Wins!")
             break
     else:
             player_one_turn = input("Press 'Enter' to roll the die ")
             die_outcome = random.choice(die)
             print("The result of the die roll is: ")
             print(die_outcome)
             print("The number of steps will be: ")
             print(20*die_outcome)
             player_one.fd(20*die_outcome)
             player_two_turn = input("Press 'Enter' to roll the die ")
             die_outcome = random.choice(die)
             print("The result of the die roll is: ")
             print(die_outcome)
             print("The number of steps will be: ")
             print(20*die_outcome)
             player_two.fd(20*die_outcome)

turtle.mainloop()