from tkinter import *
from turtle import bgcolor, width 
from PIL import Image,ImageTk
from cv2 import COLOR_BAYER_BG2GRAY, FONT_HERSHEY_COMPLEX
from numpy import column_stack
from tkinter import messagebox
from tkinter import ttk
import cv2
import os
import numpy as np
import mysql.connector
from time import strftime
from datetime import datetime
import os
import csv
# from 

mydata=[]
class Attendence:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x750+0+0")
        self.root.title('Face recognition System')
        AttendenceImage=Image.open(r"Images\Attendence1.jpg")
        AttendenceImage = AttendenceImage.resize((1350,750),Image.LANCZOS) 
        self.pic=ImageTk.PhotoImage(AttendenceImage) 
        AttendenceImage = Label(self.root,image=self.pic)
        AttendenceImage.place(width=1350,height=750)

        main_frame=Frame(AttendenceImage,bd=2,bg="white")
        main_frame.place(x=20, y=135,width=1300,height=650)

        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendence Details",font=("cambria",12,"bold"),bg="white")
        Left_frame.place(x=10,y=10,width=657,height=540)

        # label and entry
        # student id
        attendenceId_label=Label(Left_frame,text="Attendence ID :",font=("cambria",12,"bold"),bg="white")
        attendenceId_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        self.attendenceId_entry=Entry(Left_frame,font=("cambria",12,"bold"),bd=5)
        self.attendenceId_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        # student name
        studentName_label=Label(Left_frame,text="Student Name :",font=("cambria",12,"bold"),bg="white")
        studentName_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        self.studentName_entry=Entry(Left_frame,font=("cambria",12,"bold"),bd=5)
        self.studentName_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        # Rollno
        date_label=Label(Left_frame,text="Roll No :",font=("cambria",12,"bold"),bg="white")
        date_label.grid(row=2,column=0,padx=10,pady=10,sticky=W)
        self.date_entry=Entry(Left_frame,font=("cambria",12,"bold"),bd=5)
        self.date_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        #course
        course_label=Label(Left_frame,text="Course :",font=("cambria",12,"bold"),bg="white")
        course_label.grid(row=3,column=0,padx=10,pady=10,sticky=W)
        self.course_entry=Entry(Left_frame,font=("cambria",12,"bold"),bd=5)
        self.course_entry.grid(row=3,column=1,padx=10,pady=10,sticky=W)

        # time
        time_label=Label(Left_frame,text="Time :",font=("cambria",12,"bold"),bg="white")
        time_label.grid(row=4,column=0,padx=10,pady=10,sticky=W)
        self.time_entry=Entry(Left_frame,font=("cambria",12,"bold"),bd=5)
        self.time_entry.grid(row=4,column=1,padx=10,pady=10,sticky=W)

        #date
        date_label=Label(Left_frame,text="Date :",font=("cambria",12,"bold"),bg="white")
        date_label.grid(row=6,column=0,padx=10,pady=10,sticky=W)
        self.date_entry=Entry(Left_frame,font=("cambria",12,"bold"),bd=5)
        self.date_entry.grid(row=6,column=1,padx=10,pady=10,sticky=W)


        # attendence combobox
        attendence_label=Label(Left_frame,text="Attendence :",font=("cambria",12,"bold"),bg="white")
        attendence_label.grid(row=5,column=0,padx=10,pady=10,sticky=W)
        self.attendence_entry=ttk.Combobox(Left_frame,font=("cambria",12,"bold"),state="readonly",width=10)
        self.attendence_entry['values']=("Present","Absent")
        self.attendence_entry.grid(row=5,column=1,padx=10,pady=10,sticky=W)

        # button frame
        btn_frame=Frame(Left_frame,bd=2,relief=FLAT,bg="white")
        btn_frame.place(x=5,y=400,width=549,height=40)
        #save button
        save_btn=Button(btn_frame,text="Import Csv",width=10,font =( " Cambria" , 13 , " bold " ) , bg ="#2E8BC0" , fg ="white")
        save_btn.grid(row=0,column=0,padx=4,pady=3)

        update_btn=Button(btn_frame,text="Export Csv",width=10,font =( " Cambria " , 13 , " bold " ) , bg ="#2E8BC0" , fg ="white")
        update_btn.grid(row=0,column=1,padx=4,pady=3)

        delete_btn=Button(btn_frame,text="Update",width=10,font =( " cambria" , 13 , " bold " ) , bg ="#90ee90" , fg ="white")
        delete_btn.grid(row=0,column=2,padx=4,pady=3)

        reset_btn=Button(btn_frame,text="Reset",width=10,font =( " cambria " , 13 , " bold " ) , bg ="white" , fg ="Black" )
        reset_btn.grid(row=0,column=3,padx=4,pady=3)


        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendence Details",font=("cambria",12,"bold"),bg="white")
        right_frame.place(x=600,y=10,width=657,height=540)

        #frame inside right frame
        right_frame_inside=Frame(right_frame,bd=2,relief=FLAT,bg="white")
        right_frame_inside.place(x=10,y=5,width=627,height=510)

        #scroll bar table
        scroll_x=Scrollbar(right_frame_inside,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=Scrollbar(right_frame_inside,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        #table
        self.attendtable=ttk.Treeview(right_frame_inside,columns=("ID","Rollno","Name","time","date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.attendtable.xview)
        scroll_y.config(command=self.attendtable.yview)

        self.attendtable.heading("ID",text="ID")
        self.attendtable.heading("Rollno",text="Rollno")
        self.attendtable.heading("Name",text="Name")
        self.attendtable.heading("time",text="time")
        self.attendtable.heading("date",text="date")
        self.attendtable.heading("attendence",text="attendence")

        #width to the column
        self.attendtable.column("ID",width=100)
        self.attendtable.column("Rollno",width=100)
        self.attendtable.column("Name",width=100)
        self.attendtable.column("time",width=100)
        self.attendtable.column("date",width=100)
        self.attendtable.column("attendence",width=100)


        self.attendtable["show"]="headings"


        self.attendtable.pack(fill=BOTH,expand=1)






        
   

    #fetching data
    def fetch_data(self):
        global mydata






if __name__ =="__main__":
    root=Tk()
    obj=Attendence(root)
    root.mainloop()
