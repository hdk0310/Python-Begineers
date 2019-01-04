
# import the modules

import turtle
import random
import time

# create a screen
wn = turtle.Screen()
wn.bgcolor('lightblue')

# Create 2 turtle

lance = turtle.Turtle()
andy = turtle.Turtle()

lance.color('red')
andy.color('blue')

lance.shape('turtle')
andy.shape('turtle')

#4  Move the turtles to their starting point

lance.up()
andy.up()

andy.goto(-100,20)
lance.goto(-100,-20)

#a = random.randint(0,700)
#l = random.randint(0,700)
#print (a)
#print (l)
andy.forward(random.randint(0,700))
lance.forward(random.randint(0,700))

# your code goes here


finish = 800

while finish <= 800 :
    for andy in range (random.randint(0,900)):
        #print("Co'mmon Andy")
        #if andy >=800:
            #print ("Andy reached the exit point")
            #break 
wn.exitonclick()
