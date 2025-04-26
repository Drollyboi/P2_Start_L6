import turtle
from random import randint

race = turtle.Screen()
race.setup(width=600, height=400)

class TurtleRacer:
    def __init__(self, kleur, index):
        self.turtle = turtle.Turtle()
        self.kleur = kleur
        self.index = index
        self.turtle.shape("turtle")
        self.turtle.color(self.kleur)
        self.turtle.penup()
        self.turtle.goto(-200, 200 - (index * 30 ))
        self.turtle.pendown()

    def race(self):
        stappen = randint(1, 25)
        self.turtle.forward(stappen)

    def circle(self):
        self.turtle.forward(20)
        self.turtle.right(6)

    def square(self):
        self.turtle.forward(200)
        self.turtle.right(90)
        self.turtle.forward(400)
        self.turtle.right(90)
        self.turtle.forward(400)
        self.turtle.right(90)
        self.turtle.forward(400)
        self.turtle.right(90)
        self.turtle.forward(200)

racers = [
    TurtleRacer("red", 1),
    TurtleRacer("blue", 2),
    TurtleRacer("green", 3)
]

for i in range(25):
    for racer in racers:
        racer.race()

for i in range(60):
   for racer in racers:
       racer.circle()

for i in range(1):
    for racer in racers:
        racer.square()

turtle.done()
