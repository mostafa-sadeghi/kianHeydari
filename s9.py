import turtle
from time import sleep
from tkinter import Button

main_surface = turtle.Screen()
main_surface.register_shape("strawberry.gif")
main_surface.bgcolor("cyan")
main_surface.title("My App")
main_surface.setup(600, 600)


turtle1 = turtle.Turtle()
turtle1.pensize(4)
turtle1.pencolor("black")
'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
turtle1.shape('turtle')
# turtle1.shape("strawberry.gif")
turtle1.shapesize(2, 2)

# COLORS = ("red", "green", "blue")


def my_func():

    sides = int(turtle.textinput("user input", "How many sides? "))

    for side in range(sides):
        turtle1.forward(100)
        turtle1.left(360/sides)


mybutton = Button(main_surface._root, text="blalalal", command=my_func)
mybutton.pack()

# for j in range(12):
#     sleep(1)
#     turtle1.fillcolor(COLORS[j % 3])
#     turtle1.begin_fill()
#     for i in range(4):
#         turtle1.forward(100)
#         turtle1.left(90)
#     turtle1.end_fill()
#     turtle1.left(30)

turtle.done()


# def is_even(num):
#     if num % 2 == 0:
#         return f"{num} is even"
#     return f"{num} is odd"

# number = int(input("enter a number: "))

# print(is_even(number))


# def add(n1, n2, n3):
#     result = 0
#     if n1 % 2 == 0:
#         result += n1
#     if n2 % 2 == 0:
#         result += n2
#     if n3 % 2 == 0:
#         result += n3
    
#     return result


# print(add(2, 4, 6))
