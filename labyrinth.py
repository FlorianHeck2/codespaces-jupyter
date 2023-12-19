import turtle
wn = turtle.Screen()
wn.bgcolor("light green")
skk = turtle.Turtle()
skk.speed(10000)
skk.color("purple")
rounds = 10
def sqrfunc(size):
    for i in range(4):
        skk.fd(size)
        skk.left(90)
        size = size + 5
for i in range(rounds):
    a = i*20+6
    sqrfunc(a)
turtle.done()
