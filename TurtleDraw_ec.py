import turtle

TEXTFILENAME = 'colors.txt'

print('Drawing starting')

turtleScreen = turtle.Screen()
turtleScreen.setup(450, 450)

linedraw = turtle.Turtle()
linedraw.speed(20)
linedraw.penup()

turtle.title("Turtle Draw")
turtle.color("black","blue")


colortextfile = open(TEXTFILENAME, 'r')
line = colortextfile.readline()
while line:
    print(line, end='')
    parts = line.split(' ')

    if(len(parts) == 3):
        color = parts [0]
        x = int(parts[1])
        y = int(parts[2])

        
        linedraw.color(color)
        linedraw.goto(x,y)
        linedraw.pendown()
        if (len(parts) == 1):
            linedraw.penup() 
        
     





    line = colortextfile.readline()
turtle.done()
print('\nEnd')
