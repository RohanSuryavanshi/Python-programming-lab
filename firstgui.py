from easygui import *
import sys
while 1:
    msgbox("E-commerce")

    msg ="Choose the site u want to shop from"
    title = "Shopping sites"
    choices = ["Amazon", "Flipcart", "E-bay"]
    choice = choicebox(msg, title, choices)
    msgbox("You chose: " + str(choice), "Survey Result")
    msg = "categories"
    title = "Amazon"
    choices=["Electronics","clothes","staionary"]
    choice=choicebox(msg,title,choices)
    
