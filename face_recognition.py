from tkinter import *
from turtle import bgcolor 
from PIL import Image,ImageTk
from numpy import column_stack
from tkinter import messagebox
import cv2
import os
import numpy as np

class FaceRecognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x750+0+0")
        self.root.title('Face recognition System')
        frbgimage=Image.open(r"Images\fcsection.jpg")
        frbgimage=frbgimage.resize((1350,750),Image.LANCZOS)  #LANCZOS is used for conversion of high level image to low level image
        self.photo_img=ImageTk.PhotoImage(frbgimage) 
        frbgimage = Label(self.root,image=self.photo_img)
        frbgimage.place(width=1350,height=750)
        




           



if __name__ =="__main__":
    root=Tk()
    obj=FaceRecognition(root)
    root.mainloop()

