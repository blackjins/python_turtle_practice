import turtle


color_list = ("red", "blue", "yellow", "BlueViolet", "brown", "beige", "green", "LightYellow", "LimeGreen", "SkyBlue" )
num_list = ("player_two", "player_thr", "player_for", "player_fiv", "player_six", "player_sev", "player_eig", "player_nin", "player_ten")


player_one = turtle.Turtle()
player_one.color(color_list[0])
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200,380)

order = 1

def player_produce():
    for k in num_list:
        k = player_one.clone
        for p in range(1, 10):
            k.color(color_list[p])     
            if p == order:
                order += 1
                break
        continue

player_list = [player_one, player_two, player_thr, player_for, player_fiv, player_six, player_sev, player_eig, player_nin, player_ten]

player_produce()
print(player_list)


