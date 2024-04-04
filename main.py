from tkinter.colorchooser import *
from tkinter import *
import config as c
import os
from PIL import Image, ImageTk

PATH = os.path.dirname(__file__)

brush_size = c.BRUSH_SIZE
color = c.DEFAULT_COLOR

def load_image(name):
    location = os.path.join(PATH, 'resources', 'icons', name)
    image = Image.open(location)
    image = image.resize((24, 24), Image.BILINEAR)
    return ImageTk.PhotoImage(image)

def active_paint(event):
    global brush_size
    global color
    w.bind('<B1-Motion>', draw)
    w.bind('<ButtonPress-1>', draw)

def draw(e):
    global brush_size, color
    x1 = e.x - brush_size
    y1 = e.y - brush_size
    x2 = e.x + brush_size
    y2 = e.y + brush_size
    w.create_oval(x1, y1, x2, y2, fill=color, outline=color)

def decrease_brush():
    global brush_size
    if brush_size > 5:
        brush_size -= 1

def increase_brush():
    global brush_size
    if brush_size < 15:
        brush_size += 1

def color_change(new_color):
    global color
    color = new_color

def get_color():
    global color
    color = askcolor(title='Palette')
    color_change(color[1])

window = Tk()
window.title('New Paint')
w = Canvas (window, width=c.WIDTH, height=c.HEIGHT, bg=c.BG_COLOR)

w.bind('<1>', active_paint)

eraser_icon = load_image('eraser.png')
increase_icon = load_image('inbrush.png')
decrease_icon = load_image('debrush.png')
brush_icon = load_image('brush.png')

#Buttons
decrease_button = Button(image=decrease_icon, command=lambda: decrease_brush())
increase_button = Button(image=increase_icon, command=lambda: increase_brush())

brush_button = Button(image=brush_icon, command=lambda: color_change(c.DEFAULT_COLOR))
remove_button = Button(image=eraser_icon, command=lambda: color_change (c.ERASE_COLOR))

clear_all_button = Button(text='Clear all', width=10, command=lambda: w.delete('all'))

# Color Palette
red_btn = Button(bg='#FF0000', width=2, command=lambda: color_change('#FF0000'))
deep_pink_btn = Button(bg='#FF1493', width=2, command=lambda: color_change('#FF1493'))
watermelon_button = Button(bg='#EA5F89', width=2, command=lambda: color_change('#EA5F89'))
lime_green_button = Button(bg='#32CD32', width=2, command=lambda: color_change('#32CD32'))
steel_blue_button = Button(bg='#4682B4', width=2, command=lambda: color_change('#4682B4'))
yellow_button = Button(bg='#FFFF00', width=2, command=lambda: color_change('#FFFF00'))


# Color Picker
picker_button = Button(text='Color Palette', width=10, command=get_color)

# Grid
w.grid(row=2, column=3, rowspan=50, columnspan=50, sticky=W+E+N+S, padx=5, pady=5)

decrease_button.grid(row=1, column=5)
increase_button.grid(row=1, column=6)
remove_button.grid(row=1, column=8)
brush_button.grid(row=1, column=7)
clear_all_button.grid(row=1, column=9)

red_btn.grid(row=2, column=0)
deep_pink_btn.grid(row=2, column=1)
watermelon_button.grid(row=2, column=2)
lime_green_button.grid(row=3, column=0)
steel_blue_button.grid(row=3, column=1)
yellow_button.grid(row=3, column=2)

picker_button.grid(row=7, columnspan=3)

window.mainloop()