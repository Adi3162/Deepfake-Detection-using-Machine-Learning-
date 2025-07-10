import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time

global fn
fn = ""

# Create main window
root = tk.Tk()
root.configure(background="brown")

# Get screen width and height
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("DeepFake Detection")

# Set background image
image2 = Image.open('df2.jpg')
image2 = image2.resize((w, h))
background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0)

# Define functions for buttons
def reg():
    from subprocess import call
    call(["python", "registration.py"])

def log():
    from subprocess import call
    call(["python", "login.py"])

def logout():
    root.destroy()

# Button configuration
button_width = 12
button_height = 1
btn_font = ('times', 18, 'bold')

# Positioning buttons at the center bottom, slightly up
button_spacing = 190
total_width = 3 * (button_spacing)  # total horizontal space for all 3 buttons
start_x = (w - total_width) // 2
btn_y = h - 150  # slightly above the bottom

# Login Button
button1 = tk.Button(root, text="Login", command=log, width=button_width, height=button_height,
                    font=btn_font, bg="blue", fg="white")
button1.place(x=start_x, y=btn_y)

# Register Button
button2 = tk.Button(root, text="Register", command=reg, width=button_width, height=button_height,
                    font=btn_font, bg="green", fg="white")
button2.place(x=start_x + button_spacing, y=btn_y)

# Exit Button
button3 = tk.Button(root, text="Exit", command=logout, width=button_width, height=button_height,
                    font=('times', 15, 'bold'), bg="red", fg="white")
button3.place(x=start_x + 2 * button_spacing, y=btn_y)

# Start GUI loop
root.mainloop()
