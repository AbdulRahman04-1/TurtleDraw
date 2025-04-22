# turtledrawlite
#
#By: AbdulRahman
#credits: Dr. Ray Klump
#
# All rights reserved.
#
#Note: Many more example can be found by searching "python turtle example" including


import turtle

print('Turle Draw Lite starting...') 


edtheturtle = turtle.Turtle()
edtheturtle.forward(100)
edtheturtle.right(90)
edtheturtle.forward(100)
edtheturtle.right(90)
edtheturtle.forward(100)
edtheturtle.right(90)
edtheturtle.forward(100)
edtheturtle.right(90)

spiral = turtle.Turtle()
for i in range(40):
    spiral.forward(i * 10)
    spiral.right(144)


turtle.done()

TEXTFILENAME = 'green 36 29.txt'

turtledrawtextfile = open(TEXTFILENAME, 'r')
line = turtledrawtextfile.readline()
while line:
    print(line, end='')
    line = turtledrawtextfile.readline()

print('\nend')

import turtle

textfilename = 'green 36 29.txt'

print('Turtle_draw_Adbulrahman.py')

spiral = turtle.Turtle()
spiral.speed(10)

'''
spiral.pencolour("purple")
for i in range(40):
 spiral.forward(i * 10)
 spiral.right(144)
'''

print('reading a text file line by line')
turtledrawtextfile = open(TEXTFILENAME, 'r')
line = turtledrawtextfile.readline()
while line:
    print(line, end='')
    parts = line.split(' ')

    if (len(parts)==3):
        colour = parts[0]
        x = int(parts[1])
        y = int(parts[2])

        draw.pendown()
        draw.goto(x,y)
