import turtle
import random
import time

screen = turtle.Screen()
screen.title("Turtle Race")
screen.bgcolor("black")
screen.setup(width=800, height=500)

border = turtle.Turtle()
border.speed(0)
border.color("white")
border.penup()
border.goto(-350, 200)
border.pendown()
border.pensize(3)
for _ in range(2):
    border.forward(700)
    border.right(90)
    border.forward(400)
    border.right(90)
border.hideturtle()

colors = ["red", "blue", "green", "yellow", "purple", "orange"]
turtles = []
start_y = 150

for color in colors:
    racer = turtle.Turtle()
    racer.shape("turtle")
    racer.color(color)
    racer.penup()
    racer.goto(-330, start_y)
    turtles.append(racer)
    start_y -= 50

line = turtle.Turtle()
line.color("white")
line.penup()
line.goto(330, 200)
line.pendown()
line.goto(330, -200)
line.hideturtle()

time.sleep(1)

winner = None
race_on = True

while race_on:
    for racer in turtles:
        distance = random.randint(1, 10)
        racer.forward(distance)

        if racer.xcor() >= 330:
            winner = racer.color()[0]
            race_on = False
            break

message = turtle.Turtle()
message.hideturtle()
message.color("white")
message.penup()
message.goto(0, 0)
message.write(f"{winner.capitalize()} Turtle Wins!", align="center", font=("Courier", 24, "bold"))

screen.mainloop()
