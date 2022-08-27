# -*- coding: UTF-8 -*-
# 递归可视化：分形树--自相似递归图形

import turtle

# 螺旋
def drawSpiral(t, linelen):
    if linelen > 0:
        t.forward(linelen)
        t.right(90)
        drawSpiral(t, linelen - 5)

# 分形树
def tree(branch_len):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 15)
        t.left(40)
        tree(branch_len - 15)
        t.right(20)
        t.backward(branch_len)

t = turtle.Turtle()
t.left(90)
t.penup()
t.backward(100)
t.pendown()
t.pencolor("green")
t.pensize(2)
tree(75)
t.hideturtle()
turtle.done