import tkinter as tk
from tkinter import messagebox as ms
import sqlite3
import re
import random
import os
from subprocess import call

# Main Window
window = tk.Tk()
window.geometry("700x700+200+50")
window.title("REGISTRATION FORM")
window.configure(background="black")

# Variables
Fullname = tk.StringVar()
address = tk.StringVar()
username = tk.StringVar()
Email = tk.StringVar()
Phoneno = tk.StringVar()
var = tk.IntVar()
age = tk.IntVar()
password = tk.StringVar()
password1 = tk.StringVar()

# Password Validation
def password_check(passwd):
    SpecialSym = ['$', '@', '#', '%']
    if (len(passwd) < 6 or len(passwd) > 20 or
        not any(char.isdigit() for char in passwd) or
        not any(char.isupper() for char in passwd) or
        not any(char.islower() for char in passwd) or
        not any(char in SpecialSym for char in passwd)):
        return False
    return True

# Insert Data Function
def insert():
    fname = Fullname.get()
    addr = address.get()
    un = username.get()
    email = Email.get()
    mobile = Phoneno.get()
    gender = var.get()
    time = age.get()
    pwd = password.get()
    cnpwd = password1.get()

    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    valid_email = bool(re.search(regex, email))

    try:
        conn = sqlite3.connect('evaluation.db', timeout=10)
        cursor = conn.cursor()

        # Create table if not exists
        cursor.execute("""CREATE TABLE IF NOT EXISTS registration (
            Fullname TEXT, address TEXT, username TEXT, 
            Email TEXT, Phoneno TEXT, Gender TEXT, 
            age TEXT, password TEXT)""")

        cursor.execute('SELECT * FROM registration WHERE username = ?', (un,))
        user_exists = cursor.fetchone()

        # Validations
        if fname.strip() == "" or fname.isdigit():
            ms.showinfo("Message", "Please enter a valid name")
        elif addr.strip() == "":
            ms.showinfo("Message", "Please Enter Address")
        elif email == "" or not valid_email:
            ms.showinfo("Message", "Please Enter valid email")
        elif not mobile.isdigit() or len(mobile) != 10:
            ms.showinfo("Message", "Please Enter 10 digit mobile number")
        elif time <= 0 or time > 100:
            ms.showinfo("Message", "Please Enter valid age")
        elif user_exists:
            ms.showerror('Error!', 'Username Taken. Try a Different One.')
        elif pwd.strip() == "":
            ms.showinfo("Message", "Please Enter valid password")
        elif gender == 0:
            ms.showinfo("Message", "Please Select gender")
        elif not password_check(pwd):
            ms.showinfo("Message", "Password must have 1 uppercase, 1 lowercase, 1 digit, 1 symbol ($@#%), and 6-20 characters")
        elif pwd != cnpwd:
            ms.showinfo("Message", "Password and Confirm Password must be same")
        else:
            cursor.execute("""
                INSERT INTO registration(Fullname, address, username, Email, Phoneno, Gender, age , password)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (fname, addr, un, email, mobile, gender, time, pwd))
            conn.commit()
            ms.showinfo('Success!', 'Account Created Successfully!')
            conn.close()
            window.destroy()
            call(["python", "login.py"])

    except sqlite3.OperationalError as e:
        ms.showerror("Database Error", f"Could not complete request: {e}")
    finally:
        if conn:
            conn.close()

# --- UI Styling Config ---
label_config = {"bg": "black", "fg": "white"}
entry_config = {"bg": "black", "fg": "white", "insertbackground": "white"}

# --- UI Layout ---
tk.Label(window, text="User's Information", font=("Times new roman", 30, "bold"), **label_config).place(x=150, y=20)

tk.Label(window, text="Full Name :", font=("Times new roman", 18, "bold"), **label_config).place(x=130, y=100)
tk.Entry(window, textvar=Fullname, font=('', 15), **entry_config).place(x=330, y=100)

tk.Label(window, text="Address :", font=("Times new roman", 18, "bold"), **label_config).place(x=130, y=150)
tk.Entry(window, textvar=address, font=('', 15), **entry_config).place(x=330, y=150)

tk.Label(window, text="E-mail :", font=("Times new roman", 18, "bold"), **label_config).place(x=130, y=200)
tk.Entry(window, textvar=Email, font=('', 15), **entry_config).place(x=330, y=200)

tk.Label(window, text="Phone number :", font=("Times new roman", 18, "bold"), **label_config).place(x=130, y=250)
tk.Entry(window, textvar=Phoneno, font=('', 15), **entry_config).place(x=330, y=250)

tk.Label(window, text="Gender :", font=("Times new roman", 18, "bold"), **label_config).place(x=130, y=300)
tk.Radiobutton(window, text="Male", variable=var, value=1,
               bg="black", fg="white", font=("bold", 15), selectcolor="black").place(x=330, y=300)
tk.Radiobutton(window, text="Female", variable=var, value=2,
               bg="black", fg="white", font=("bold", 15), selectcolor="black").place(x=440, y=300)

tk.Label(window, text="Age :", font=("Times new roman", 18, "bold"), **label_config).place(x=130, y=350)
tk.Entry(window, textvar=age, font=('', 15), **entry_config).place(x=330, y=350)

tk.Label(window, text="User Name :", font=("Times new roman", 18, "bold"), **label_config).place(x=130, y=400)
tk.Entry(window, textvar=username, font=('', 15), **entry_config).place(x=330, y=400)

tk.Label(window, text="Password :", font=("Times new roman", 18, "bold"), **label_config).place(x=130, y=450)
tk.Entry(window, textvar=password, show="*", font=('', 15), **entry_config).place(x=330, y=450)

tk.Label(window, text="Confirm Password:", font=("Times new roman", 18, "bold"), **label_config).place(x=100, y=500)
tk.Entry(window, textvar=password1, show="*", font=('', 15), **entry_config).place(x=330, y=500)

tk.Button(window, text="SUBMIT", bg="green", fg="white", font=("", 20), width=9, height=1, command=insert).place(x=260, y=550)

window.mainloop()


