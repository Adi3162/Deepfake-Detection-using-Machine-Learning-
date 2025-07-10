import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re

root = tk.Tk()
root.configure(background="black")
root.geometry("590x450")
root.title("Login Form")

username = tk.StringVar()
password = tk.StringVar()

# --- Functions ---
def registration():
    from subprocess import call
    call(["python", "registration.py"])
    root.destroy()

def login():
    with sqlite3.connect('evaluation.db') as db:
        c = db.cursor()
        cursor = db.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS registration
                          (Fullname TEXT, address TEXT, username TEXT, 
                          Email TEXT, Phoneno TEXT, Gender TEXT, 
                          age TEXT , password TEXT)""")
        db.commit()
        find_entry = ('SELECT * FROM registration WHERE username = ? and password = ?')
        c.execute(find_entry, [(username.get()), (password.get())])
        result = c.fetchall()

        if result:
            ms.showinfo("Message", "Login successful!")
            root.destroy()
            from subprocess import call
            call(['python', 'GUI_Master_old.py'])
        else:
            ms.showerror('Oops!', 'Username or Password did not match.')

def logout():
    root.destroy()

# --- UI Components ---
title = tk.Label(root, text="User Login", font=("arial black", 30, "bold"),
                 bd=5, bg="black", fg="white")
title.place(x=120, y=0, width=350)

l4 = tk.Label(root, text="User Name :", width=12, font=("Times new roman", 15, "bold"), bg="black", fg="white")
l4.place(x=100, y=120)
t3 = tk.Entry(root, textvar=username, width=20, font=('times new roman', 15),
              bg="black", fg="white", insertbackground="white")
t3.place(x=250, y=120)

l9 = tk.Label(root, text="Password :", width=12, font=("Times new roman", 15, "bold"), bg="black", fg="white")
l9.place(x=100, y=170)
t9 = tk.Entry(root, textvar=password, width=20, font=('times new roman', 15),
              show="*", bg="black", fg="white", insertbackground="white")
t9.place(x=250, y=170)

button1 = tk.Button(root, text="SIGN UP", command=registration, width=10, height=1,
                    font=('times', 15, 'bold'), bg="#808000", fg="white")
button1.place(x=250, y=300)

button2 = tk.Button(root, text="SUBMIT", command=login, width=10, height=1,
                    font=('times', 15, 'bold'), bg="blue", fg="white")
button2.place(x=250, y=220)

label_hint = tk.Label(root, text="Not a member Yet??", font=("Algerian", 15, "bold"),
                      bd=5, bg="black", fg="white")
label_hint.place(x=220, y=270)

button3 = tk.Button(root, text="Logout", command=logout, width=10, height=1,
                    font=('times', 15, 'bold'), bg="red", fg="white")
button3.place(x=250, y=350)

root.mainloop()
