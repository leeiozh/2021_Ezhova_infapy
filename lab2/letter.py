import turtle

def zero():
    turtle.pendown()
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.penup()
    turtle.right(90)
    turtle.forward(100)

def one():
    turtle.penup()
    turtle.right(90)
    turtle.forward(50)
    turtle.pendown()
    turtle.left(135)
    turtle.forward(50 * 2 ** 0.5)
    turtle.right(135)
    turtle.forward(100)
    turtle.penup()
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)

def two():
    turtle.pendown()
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(45)
    turtle.forward(50 * 2**0.5)
    turtle.left(135)
    turtle.forward(50)
    turtle.penup()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)

def three():
    turtle.pendown()
    turtle.forward(50)
    turtle.right(135)
    turtle.forward(50 * 2 ** 0.5)
    turtle.left(135)
    turtle.forward(50)
    turtle.right(135)
    turtle.forward(50 * 2 ** 0.5)
    turtle.left(135)
    turtle.penup()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)

def four():
    turtle.pendown()
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(100)
    turtle.penup()
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)

def five():
    turtle.pendown()
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.penup()
    turtle.left(180)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)

def six():
    turtle.penup()
    turtle.right(90)
    turtle.forward(50)
    turtle.pendown()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(135)
    turtle.forward(50 * 2 ** 0.5)
    turtle.right(45)
    turtle.penup()
    turtle.forward(50)

def seven():
    turtle.pendown()
    turtle.forward(50)
    turtle.right(135)
    turtle.forward(50 * 2 ** 0.5)
    turtle.left(45)
    turtle.forward(50)
    turtle.penup()
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)

def eight():
    turtle.pendown()
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(180)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.penup()
    turtle.right(90)
    turtle.forward(50)

def nine():
    turtle.penup()
    turtle.right(90)
    turtle.forward(100)
    turtle.pendown()
    turtle.left(135)
    turtle.forward(50 * 2 ** 0.5)
    turtle.left(135)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(180)
    turtle.forward(50)
    turtle.right(90)
    turtle.penup()
    turtle.forward(50)

def print_letter(a):

    for i in a:

        if i == '0':
            zero()
        if i == '1':
            one()
        if i == '2':
            two()
        if i == '3':
            three()
        if i == '4':
            four()
        if i == '5':
            five()
        if i == '6':
            six()
        if i == '7':
            seven()
        if i == '8':
            eight()
        if i == '9':
            nine()

a = input()
print_letter(a)


