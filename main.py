import turtle
import time

name = input("What is your first name?")
song = input("What is your favorite CAS song?")
clr = input("What is your favorite color?")
if name.lower() == "allan" and song.lower() == "cry" and clr.lower() == "purple":
    print("Wow my wonderful girlfriend knows me so well! But I want you to see what I made for you!")

elif name.lower() != "pia" or song.lower() != "heavenly" or clr.lower() != "green":

    wn = turtle.Screen()
    wn.bgcolor("white")
    allan = turtle.Turtle()
    allan.color("red")
    allan.pensize(0)
    allan.penup()
    my_font = ("Times New Roman", 20, "bold")
    my_font2 = ("Times New Roman", 15, "bold")
    allan.write("THIS IS NOT FOR YOUR EYES!!!!!!!!!", True, align = "center", font = my_font)
    allan.right(90)
    allan.forward(60)
    allan.right(90)
    allan.forward(230)
    allan.write("YOU ARE (PROBABLY) NOT MY AMAZING GIRLFRIEND! TRY AGAIN!",align = "center", font = my_font2)
    allan.hideturtle()
    wn.mainloop()


else:
    print("Hello there Pia! There is a wide array of colors you can choose the turtle to be, but you can't input a space before the color name.")

    print("The thickness should range from 1 to 10.")
    print("The speed of the turtle ranges from 1 to 10, but 0 makes it go the fastest(I recommend 1)!")
    def make_turtle (color,pensize,speed):
        t = turtle.Turtle()
        t.shape("turtle")
        t.color(color)
        t.pensize(pensize)
        t.speed(speed)
        return t

time.sleep(2)


clr = input("What color do you want the turtle to be?")
thck = input("How THICK should the turtle be?")
fst = input("How fast should the turtle be?")


allan = make_turtle("purple", int(thck), int(fst))
pia = make_turtle(clr, int(thck), int(fst ))

us = make_turtle("red", int(thck),1 )

us.hideturtle()

wn = turtle.Screen()
wn.bgcolor("lightgreen")

def make_right_half_of_a_heart(w):
    w.begin_fill()
    w.left(50)
    w.forward(170)
    w.write ("     You")
    w.circle(80, 167)
    w.end_fill()
    w.hideturtle()

def make_left_half_of_a_heart(w):
    w.begin_fill()
    w.left(130)
    w.forward(170)
    w.penup()
    w.left(50)
    w.forward(25)
    w.write("Me")
    w.forward(-25)
    w.right(50)
    w.pendown()
    w.circle(-80, 167)
    w.end_fill()
    w.hideturtle()

def make_full_heart(w):
    us.showturtle()
    w.begin_fill()
    w.left(50)
    w.forward(170)
    w.circle(80, 167)
    w.right(75)
    w.circle(80, 167)
    w.forward(172)
    w.end_fill()
    w.right(36)
    w.penup()
    w.forward(30)
    time.sleep(1)
    us.hideturtle()
    w.write("I love you so much!", align = "center", font = ("Times New Roman", 15))
    w.forward(20)
    time.sleep(2)
    w.write("u da best fr", align="center", font=("Times New Roman", 15))
    w.forward(20)
    time.sleep(2)
    w.write("Much love,", align="center", font=("Times New Roman", 15))
    w.forward(20)
    w.write("Allan", align="center", font=("Times New Roman", 15))

make_right_half_of_a_heart(pia)
time.sleep(2)
make_left_half_of_a_heart(allan)
time.sleep(2)
make_full_heart(us)

wn.mainloop()

