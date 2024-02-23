import turtle as t


pen = t.Turtle()
t.color('red')
t.delay(8)
pen.color('red')
pen.begin_fill()
pen.left(40)
pen.forward(120)
pen.circle(80, 190)
pen.right(100)
pen.circle(80, 180)
pen.forward(160)
pen.left(90)
pen.forward(50)
pen.setpos(-60, 100)
pen.end_fill()



def txt():
    pen.up()
    pen.setpos(-155, 100)
    pen.color('yellow')
    pen.write('eshgham valentine mobark<3', font=("Comic Sans MS", 16))

txt()

pen.end_fill()
t.exitonclick()
