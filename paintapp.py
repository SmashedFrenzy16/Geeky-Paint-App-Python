import turtle
import random

wn = turtle.Screen()
wn.title("Geeky Paint Application")

turt = turtle.Turtle()

turt.hideturtle()

print("0 - Red")
print("1 - Orange")
print("2 - Yellow")
print("3 - Green")
print("4 - Blue")
print("5 - Black")
print("6 - Purple")


custom = int(input("Choose a color (relative number): "))

colorLibraryRaw = ["red", "orange", "yellow", "green", "blue", "black", "purple"]

colorLibrary = colorLibraryRaw[custom]

turt.color(colorLibrary)

def func(x, y):

    turt.goto(x, y)
    turt.write(str(x) + ", " + str(y))

wn.onclick(func)

wn.mainloop()
