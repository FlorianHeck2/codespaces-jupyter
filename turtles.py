import turtle

ws = turtle.Turtle()
turtle.Screen()
max = 100
ws.speed(1000)
ws.color("light green")
ws.left(90)
ws.forward(100)
ws.color("purple")
for y in range(max):
    ws.left(int(180/max)*y)
    ws.left(60)
    ws.forward(25)
    ws.left(60)
    ws.forward(25)
    ws.left(60)
    ws.forward(25)
    ws.left(60)
    ws.forward(25)
    ws.left(60)
    ws.forward(25)
    ws.left(60)
    ws.forward(25)


turtle.done()