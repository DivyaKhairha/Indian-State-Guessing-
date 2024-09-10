import turtle as t
import pandas as pd


scr = t.Screen()
scr.setup(800,800)
scr.bgpic(r"python\100python\State_guessing\India.gif")

table = pd.read_csv(r"python\100python\State_guessing\states.csv")
State = table.State.to_list()
y = table.y.to_list()
x = table.x.to_list()

game_in_on = True

while game_in_on:
    guess = scr.textinput("HELLO","Guess name (Leave it blank to exit: )")
    if guess == "":
        break
    if guess in State:
        i = State.index(guess)
        temp = t.Turtle()
        temp.penup()
        temp.hideturtle()
        temp.goto(x = x[i],y = y[i])
        temp.write(guess)


scr.exitonclick()