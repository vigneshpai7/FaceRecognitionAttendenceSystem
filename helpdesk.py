from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import webbrowser

class Help:
	def __init__(self, root):
		self.root=root
		self.root.geometry("1530x790+0+0")
		self.root.title("Face Recongnition System")


		#Image in top bar
		img_top=Image.open(r"Images\Register.png")
		
		img_top=img_top.resize((1530,790),Image.ANTIALIAS)
		self.photoimg_top=ImageTk.PhotoImage(img_top)

		#Mail label
		f_lbl=Label(self.root,image=self.photoimg_top)
		f_lbl.place(x=0,y=0,width=1530,height=720) 
		dev_label=Label(f_lbl,text="Abc@gmail.com",font=("times new roman",24,"bold"),bg="white",fg="navyblue")
		dev_label.place(x=450,y=220)



if __name__=="__main__":
	root=Tk()
	obj=Help(root)
	root.mainloop()