"""
画一个小人，学生代码
"""
import turtle

turtle.colormode(255)
t = turtle.Turtle()

# 画帽子
t.up()
t.goto(-50, 100)
pos1 = t.position()
top_point = 0, 160
t.begin_fill()
t.fillcolor(250, 109, 34)
t.down()
t.setheading(0)

t.forward(100)

t.goto(top_point)
t.goto(pos1)
t.end_fill()
t.forward(10)

# 画脸
t.begin_fill()
t.fillcolor("yellow")
t.setheading(-90)
t.circle(40, 180)
t.setheading(180)
t.forward(80)
t.end_fill()

# 画手
t.up()
t.goto(-140, 60)
t.down()
t.begin_fill()
t.fillcolor(11, 80, 153)
t.setheading(0)
t.forward(280)
t.right(90)
t.forward(30)
t.right(90)
t.forward(280)
t.right(90)
t.forward(30)
t.end_fill()
t.up()

# 画身体
t.setheading(-90)
t.up()
t.goto(-40, 60)

t.begin_fill()
t.fillcolor(133, 214, 225)
t.down()
t.setheading(0)
t.backward(10)
t.forward(100)
t.right(90)
t.forward(120)
t.right(90)
t.forward(100)
t.right(90)
t.forward(120)
t.end_fill()
t.up()

t.goto(0, 30)
t.begin_fill()
t.setheading(0)
t.fillcolor(181, 0, 40)
t.circle(5)
t.end_fill()

t.goto(0, 0)
t.begin_fill()
t.setheading(0)
t.fillcolor(181, 0, 40)
t.circle(5)
t.end_fill()
t.up()

# 画左脚
t.goto(-30, -60)
t.down()
t.begin_fill()
t.fillcolor(59, 147, 54)
t.setheading(180)
t.forward(100)
t.left(90)
t.forward(30)
t.left(90)
t.forward(100)
t.left(90)
t.forward(30)
t.end_fill()
t.up()

# 画右脚
t.goto(50, -60)
t.down()
t.begin_fill()
t.fillcolor(59, 147, 54)
t.setheading(-90)
t.forward(100)
t.right(90)
t.forward(30)
t.right(90)
t.forward(100)
t.right(90)
t.forward(30)
t.end_fill()
