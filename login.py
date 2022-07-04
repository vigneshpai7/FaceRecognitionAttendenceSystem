from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from matplotlib import image
import mysql.connector
from student import Student
import os

from datetime import datetime
from tkinter import *
from main import Face_recognition_system
from register import Register
from tkinter import *
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
from face_recognition import FaceRecognition
import os
from face_recognition import FaceRecognition
import tkinter




def main():
    win = Tk()
    app = Login_window(win)
    win.mainloop()


class Login_window(object):
    """docstring for login"""

    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        #bg image
        bgimg = Image.open(r"Images\login.png")
        # LANCZOS is used for conversion of high level image to low level image
        bgimg = bgimg.resize((1350, 750), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(bgimg)

        # setting of image in window with the help of label
        bgimage1 = Label(self.root, image=self.photoimg)
        bgimage1.place(width=1350, height=750)
        # Farme for login field
        frame = Frame(self.root, bg="white")
        frame.place(x=610, y=170, width=340, height=450)

       #image for login
        get_str = Label(frame, text="Get Started", font=(
            "times new roman", 20, "bold"), fg="black", bg="white")
        get_str.place(x=95, y=100)

        # Labels for user and password
        username = lbl = Label(frame, text="Username", font=(
            "times new roman", 15, "bold"), fg="black", bg="white")
        username.place(x=70, y=155)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        # For password label
        password = lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="black", bg="white")
        password.place(x=70, y=225)

        self.txtpass = ttk.Entry(frame, font=(
            "times new roman", 15, "bold"), show="*")
        self.txtpass.place(x=40, y=250, width=270)


        # =====log in button=====
        loginbtn = Button(frame, text="Login", command=self.login, font=("times new roman", 15, "bold"),
                          bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=330, width=120, height=35)

        # =====Register button=====
        registerbtn = Button(frame, text="New User Register", command=self.register_window, font=(
            "times new roman", 10, "bold"), borderwidth=0, fg="white", bg="#751aff", activeforeground="white", activebackground="black")
        registerbtn.place(x=15, y=370, width=160)

        # =====Forget password button=====
        loginbtn = Button(frame, text="Forget Password", command=self.forgot_password_window, font=(
            "times new roman", 10, "bold"), borderwidth=0, fg="white", bg="#751aff", activeforeground="white", activebackground="black")
        loginbtn.place(x=15, y=410, width=160)

    # For new user func
    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    #Log in function

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "all fields required")
        elif self.txtuser.get() == "palash" and self.txtpass.get() == "123":
            messagebox.showinfo(
                "Success", "Welcome to Face Recognition System")
        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="root", database="facerecogniser")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and pass=%s", (
                self.txtuser.get(),
                self.txtpass.get()
            ))
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid Username & Password")
            else:
                open_main = messagebox.askyesno("YesNo", "Access only Admin")
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = Face_recognition_system(self.new_window)

                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    # ==================Reset Button Function=============

    def reset_pass(self):
        if self.combo_security_Q.get() == "Select":
            messagebox.showerror(
                "Error", "Select Security Question", parent=self.root2)
        elif self.txt_security.get() == "":
            messagebox.showerror(
                "Error", "Please give the Answer", parent=self.root2)

        elif self.txt_newpass.get == "":
            messagebox.showerror(
                "Error", "Please eneter the  new password", parent=self.root2)

        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="root", database="facerecogniser")
            my_cursor = conn.cursor()
            query = (
                "select * from register where email=%s and securityQ=%s and securityA=%s")
            value = (self.txtuser.get(), self.combo_security_Q.get(),
                     self.txt_security.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            # Check if the answer is correct
            if row == None:
                messagebox.showerror(
                    "Error", "Please enter the correct Answer", parent=self.root2)
            else:
                query = ("update register set pass=%s where email=%s")
                value = (self.txt_newpass.get(), self.txtuser.get())
                my_cursor.execute(query, value)

                conn.commit()
                conn.close()
                messagebox.showinfo(
                    "Info", "Your password has been reset, please login with new password ", parent=self.root2)

                self.root2.destroy()

    # ======forget password function=========
    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror(
                "Error", "Please enter the Email address to reset password")
        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="root", database="facerecogniser")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            # For correct user name or email
            if row == None:
                messagebox.showerror(
                    "My Error", "Please enter the valid user name")
            # Opening new window if correct email
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l = Label(self.root2, text="Forget Password", font=(
                    "times new roman", 20, "bold"), fg="red", bg="white")
                l.place(x=0, y=10, relwidth=1)

                security_Q = Label(self.root2, text="Select Security Questions", font=(
                    "times new roman", 15, "bold"), bg="white", fg="black")
                security_Q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2, font=(
                    "times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"] = (
                    "Select", "Your Birth Place", "Your Best Friend Name", "Your Favourite food")
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)

                security_A = Label(self.root2, text="Security Answer", font=(
                    "times new roman", 15, "bold"), bg="white", fg="black")
                security_A.place(x=50, y=150)

                self.txt_security = ttk.Entry(
                    self.root2, font=("times new roman", 15))
                self.txt_security.place(x=50, y=180, width=250)

                new_password = Label(self.root2, text="New Password", font=(
                    "times new roman", 15, "bold"), bg="white", fg="black")
                new_password.place(x=50, y=220)

                self.txt_newpass = ttk.Entry(
                    self.root2, font=("times new roman", 15))
                self.txt_newpass.place(x=50, y=250, width=250)

                # reset button
                btn = Button(self.root2, text="Reset", command=self.reset_pass, font=(
                    "times new roman", 15, "bold"), fg="white", bg="green")
                btn.place(x=100, y=290)

    # =====for login button from register page====

    def return_login(self):
        self.root.destroy()


if __name__ == "__main__":
    main()
