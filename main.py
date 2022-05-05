#imports
from turtle import Turtle, Screen
from random import randint

#screen and dimensions
screen = Screen()
screen.setup(width=500, height=400)

#initialize essential variables
user_bet = screen.textinput(title="Place your bet", prompt="Which turtle will win the race? Choose a color: ")
decided = False
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
turtles = []

#initialize turtles
for i in range(0, 7):
    turt = Turtle(shape="turtle")
    turt.color(colors[i])
    turt.penup()
    turt.goto(-230, (150-(i*50)))
    turtles.append(turt)

#starts game
if user_bet:
    decided = True

#completes loop and functionality of game
while decided:
    for turt in turtles:
        if turt.xcor() > 230:
            decided = False
            winning_color = turt.pencolor()
            if winning_color == user_bet:
                print("Congrats! You've won! {0} is the winner!".format(winning_color))
            else:
                print("Oops, you've lost :( {0} is the winner!".format(winning_color))
        else:
            rand_dist = randint(1,10)
            turt.forward(rand_dist)

screen.exitonclick()