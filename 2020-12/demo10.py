# import package
import turtle

# set turtle
turtle.speed(1)
turtle.up()
turtle.setpos(-50, 50)
turtle.down()

# motion
for i in range(4):
    turtle.forward(100)
    turtle.right(90)

# undo
for i in range(8):
    turtle.undo()


