
from tkinter import *
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
from face_recognition import FaceRecognition
from student import Student
import os
from a import Attendence
from train import Train
from face_recognition import FaceRecognition
import tkinter
from time import strftime
from helpdesk import Help


class Face_recognition_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x750+0+0")
        self.root.title('Face recognition System')
        # bgimages
        img = Image.open(r"Images\image1.png")
        # LANCZOS is used for conversion of high level image to low level image
        img = img.resize((1350, 750), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        # setting of image in window with the help of label
        bgimage = Label(self.root, image=self.photoimg)
        bgimage.place(width=1350, height=750)
  # time
        self.time_labelname = Label(bgimage, text="Time:", font=(
            "Comic Sans MS", 20), fg="black", bg="white")
        self.time_labelname.place(x=5, y=0)
        self.time_label = Label(bgimage, text="", font=(
            "Comic Sans MS", 20), fg="black", bg="white")
        self.time_label.place(x=75, y=0, width=120, height=45)
        self.time_label.after(1000, self.time_func)

        # adding title project
        title_label = Label(bgimage, text="FACE RECONITION ATTENDENCE SYSTEM SOFTWARE", font=(
            "Comic Sans MS", 25), fg="#4d4dff")
        title_label.place(x=0, y=600, width=1430, height=45)

        # student Button 1
        img2 = Image.open(r"Images\students.jpg")
        img2 = img2.resize((180, 180), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b1 = Button(bgimage, image=self.photoimg2,
                    command=self.student_details, borderwidth=0, cursor=" hand2 ")
        b1.place(x=150, y=180, width=180, height=180)
        b1_1 = Button(bgimage, text="Student Details", command=self.student_details,
                      cursor=" hand2 ", font=("Cambria", 15, "bold"), fg="#4d4dff")
        b1_1.place(x=150, y=350, width=180, height=40)
        # face recognition button
        img3 = Image.open(r"Images\face.png")
        img3 = img3.resize((200, 220), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b2 = Button(bgimage, image=self.photoimg3, borderwidth=0,
                    cursor=" hand2 ", command=self.faceR)
        b2.place(x=450, y=180, width=180, height=180)
        b2_2 = Button(bgimage, text="Mark Attendence", cursor=" hand2 ", font=(
            "Cambria", 15, "bold"), fg="#4d4dff", command=self.faceR)
        b2_2.place(x=450, y=350, width=180, height=40)
        #Attendence -button
        img4 = Image.open(r"Images\attendence.jpg")
        img4 = img4.resize((180, 180), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b3 = Button(bgimage, image=self.photoimg4, borderwidth=0,
                    cursor=" hand2 ", command=self.Attendence)
        b3.place(x=750, y=180, width=180, height=180)
        b3_3 = Button(bgimage, text="Export", cursor=" hand2 ", font=(
            "Cambria", 15, "bold"), fg="#4d4dff", command=self.Attendence)
        b3_3.place(x=750, y=350, width=180, height=40)
        # Helpdesk Button

# train face button
        img6 = Image.open(r"Images\train.png")
        img6 = img6.resize((180, 180), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b5 = Button(bgimage, image=self.photoimg6, borderwidth=0,
                    cursor=" hand2 ", command=self.Train_data)
        b5.place(x=150, y=400, width=180, height=180)
        b5_5 = Button(bgimage, text="Train", cursor=" hand2 ", font=(
            "Cambria", 15, "bold"), fg="#4d4dff", command=self.Train_data)
        b5_5.place(x=150, y=550, width=180, height=40)
# photo face button
        img7 = Image.open(r"Images\photo.png")
        img7 = img7.resize((180, 180), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b6 = Button(bgimage, image=self.photoimg7, borderwidth=0,
                    cursor=" hand2 ", command=self.open_img)
        b6.place(x=450, y=400, width=180, height=180)
        b6_6 = Button(bgimage, text="Photos", cursor=" hand2 ", font=(
            "Cambria", 15, "bold"), fg="#4d4dff", command=self.open_img)
        b6_6.place(x=450, y=550, width=180, height=40)
# help desk button
        img5 = Image.open(r"Images\help.jpg")
        img5 = img5.resize((180, 180), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b4 = Button(bgimage, image=self.photoimg5,
                    borderwidth=0, cursor=" hand2 ", command=self.help_desk)
        b4.place(x=750, y=400, width=180, height=180)
        b4_4 = Button(bgimage, text="Helpdesk", cursor=" hand2 ",
                      font=("Cambria", 15, "bold"), fg="#4d4dff", command=self.help_desk)
        b4_4.place(x=750, y=550, width=180, height=40)


#exit- button
        img9 = Image.open(r"Images\exit.png")
        img9 = img9.resize((180, 180), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b8 = Button(bgimage, image=self.photoimg9, borderwidth=0,
                    cursor=" hand2 ", command=self.iexit)
        b8.place(x=1050, y=300, width=180, height=180)
        b8_8 = Button(bgimage, text="Exit", cursor=" hand2 ", font=(
            "Cambria", 15, "bold"), fg="#4d4dff", command=self.iexit)
        b8_8.place(x=1050, y=450, width=180, height=40)

    def open_img(self):
        os.startfile("data")

    def iexit(self):
        self.exit = tkinter.messagebox.askyesno("Exit", "Do you want to exit?")
        if self.exit > 0:
            self.root.destroy()
        else:
            return
# =================================function buttons================

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def Train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def faceR(self):
        self.new_window = Toplevel(self.root)
        self.app = FaceRecognition(self.new_window)

    def Attendence(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendence(self.new_window)

    def time_func(self):
        self.time_label.config(text=strftime("%H:%M:%S"))
        self.time_label.after(1000, self.time_func)
    def help_desk(self):
        self.helpwindow = Toplevel(self.root)
        self.app = Help(self.helpwindow)        


if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition_system(root)
    root.mainloop()
