import tkinter as tk
from PIL import Image, ImageTk
from subprocess import call

# Initialize the main application
root = tk.Tk()
root.configure(background="brown")
root.geometry("1300x700")

# Set the window to dynamically adjust to full screen
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

# Create a label for the background image
bg_label = tk.Label(root)
bg_label.place(relwidth=1, relheight=1)  # Ensure the image covers the full window

# Function to resize and display the background image
def resize_bg_image(event=None):
    try:
        # Dynamically resize the image to fit the current window size
        bg_image = Image.open("M1.jpg").resize((root.winfo_width(), root.winfo_height()))
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label.config(image=bg_photo)
        bg_label.image = bg_photo  # Keep a reference to prevent garbage collection
        print("Background image resized successfully.")
    except FileNotFoundError:
        print("Background image file not found. Please check the file path.")

# Bind the window resize event to the resizing function
root.bind('<Configure>', resize_bg_image)

# Function to start the detection process
def start_detection():
    call(["python", "GUI_main.py"])  # Replace "GUI_main.py" with your actual script

# Title Label
title_label = tk.Label(
    root,
    text="Deep Fake Detection System",
    font=("Helvetica", 24, "bold"),
    bg="#1a1a3f",  # Semi-transparent navy blue background
    fg="white"
)
title_label.place(relx=0.5, rely=0.2, anchor="center")  # Centered near the top

# Add a Centered Button further up
start_button = tk.Button(
    root,
    text="Start Detection",
    command=start_detection,
    font=("Helvetica", 14, "bold"),
    bg="skyblue",
    fg="black",
    activebackground="#21a1f1",
    activeforeground="white",
    width=20,
    height=2
)
start_button.place(relx=0.5, rely=0.65, anchor="center")  # Positioned even further up

# Footer Label
footer_label = tk.Label(
    root,
    text="Developed by: [Aditya Jha ,Rohit Gadekar ,Kartik Jadhao ,Vishal Katurde  ] - Final Year Project",
    font=("Helvetica", 12),
    bg="#1a1a3f",  # Semi-transparent navy blue background
    fg="white"
)
footer_label.place(relx=0.5, rely=0.9, anchor="center")  # Centered at the bottom

# Call the resize function to display the initial image
resize_bg_image()

# Start the main event loop
root.mainloop()