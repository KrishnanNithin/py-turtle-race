from turtle import Turtle, Screen

red = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your bet", prompt="Which turtle will win the race? Choose a color: ")
print(user_bet)


screen.exitonclick()