##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# Insert your code here to draw the house!

# The house outline (roof and the red house) and green grass 70pt and 100pt

house = drawpad.create_rectangle (200, 200, 610, 500, fill = "red")

grass = drawpad.create_rectangle (0, 500, 810, 600, fill = "green")

roof1 = drawpad.create_line (150, 240, 410, 50)

roof2 = drawpad.create_line (660, 240, 410, 50)

# The white square windows and a brown door 80pt

door = drawpad.create_rectangle (360, 400, 450, 500, fill = "brown")

window1 = drawpad.create_rectangle (250, 400, 300, 450, fill = "blue")

window2 = drawpad.create_rectangle (500, 400, 550, 450, fill = "blue")

window3 = drawpad.create_rectangle (250, 275, 300, 325, fill = "blue")

window4 = drawpad.create_rectangle (500, 275, 550, 325, fill = "blue")

# The yellow door handle and a black chimney 90pt

handle = drawpad.create_oval (440, 440, 450, 450, fill = "yellow")

chimney = drawpad.create_rectangle (500, 100, 550, 175, fill = "black")

root.mainloop()
