from cProfile import label
from msilib.schema import Verb
from tkinter import *
from tkinter import ttk
from tkinter import font
from turtle import bgcolor
from PIL import Image,ImageTk
from numpy import column_stack
from tkinter import messagebox
import mysql.connector


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x750+0+0")
        self.root.title('Face recognition System')
        #===variabls===
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_rollno=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_Mentor=StringVar()
        self.var_gender = StringVar()
        


        img=Image.open(r"C:\Users\paivi\Desktop\Face_Attendence_system\Images\student.png")
        img=img.resize((1350,750),Image.LANCZOS)  #LANCZOS is used for conversion of high level image to low level image
        self.photoimg=ImageTk.PhotoImage(img)

        #setting of image in window with the help of label
        bgimage = Label(self.root,image=self.photoimg)
        bgimage.place(width=1350,height=750)
        
        #creating frame
        main_frame=Frame(bgimage,bd=2,bg="white",relief=SUNKEN)
        main_frame.place(x=20,y=135,width=1300,height=650)
    #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("cambria",12,"bold"),bg="white")
        Left_frame.place(x=10,y=10,width=657,height=540)
      
        #current course
        current_course_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Course Info",font=("cambria",12,"bold"),bg="white")
        current_course_frame.place(x=10,y=0,width=570,height=150)

        #course-1
        dep_label = Label(current_course_frame, text="Course",font=("cambria",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0)
        dept_combo=ttk.Combobox(current_course_frame,font=("cambria",12,"bold"),textvariable=self.var_course, width=17,state="read only")
        dept_combo["values"]=("Select course","BCA","BBA","BCOM","BA","B.Ed")
        dept_combo.current(0)
        dept_combo.grid(row=0,column=1,padx=2,pady=2,sticky=W)
        
        #Year-2
        year_label = Label(current_course_frame, text="Year",font=("cambria",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,pady=10)
        year_combo=ttk.Combobox(current_course_frame,font=("cambria",12,"bold"),width=17,state="read only",textvariable=self.var_year)
        year_combo["values"]=("Select Year","2020-2021","2021-2022","2022-2023","2024-2025","2025-2026","2026-2027")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=2,sticky=W)

        #Semester-3
        sem_label = Label(current_course_frame, text="Semester",font=("cambria",12,"bold"),bg="white")
        sem_label.grid(row=2,column=0,padx=10,pady=10)
        sem_combo=ttk.Combobox(current_course_frame,font=("cambria",12,"bold"),textvariable=self.var_sem,width=17,state="read only")
        sem_combo["values"]=("Select Semester","1","2","3","4","5","6")    
        sem_combo.current(0)
        sem_combo.grid(row=2,column=1,padx=2,pady=2,sticky=W)
        
        #class student Info-4 
        class_student_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Class Student Information",font=("cambria",12,"bold"),bg="white")
        class_student_frame.place(x=10,y=160,width=570,height=350)
        #student id
        student_id_label = Label(class_student_frame, text="Student Id",font=("cambria",12,"bold"),bg="white",)
        student_id_label.grid(row=0,column=0,padx=3,pady=3,sticky=W)
        
        studentID_entry=ttk.Entry(class_student_frame,width=15,font=("cambria",12,"bold"),textvariable=self.var_id)
        studentID_entry.grid(row=0,column=1,padx=3,pady=3,sticky=W)
        
        #Student name
        student_name_label = Label(class_student_frame, text="Student Name:",font=("cambria",12,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=3,pady=3,sticky=W)
        
        student_name_entry=ttk.Entry(class_student_frame,width=15,font=("cambria",12,"bold"),textvariable=self.var_name)
        student_name_entry.grid(row=0,column=3,padx=3,pady=3,sticky=W)

        #class division
        div_label = Label(class_student_frame, text="Division:",font=("cambria",12,"bold"),bg="white")
        div_label.grid(row=1,column=0,padx=3,pady=3,sticky=W)
        
        div_entry=ttk.Combobox(class_student_frame,font=("cambria",12,"bold"),width=13,state="read only",textvariable=self.var_div)
        div_entry["values"]=("Select Division","A","B","C")
        div_entry.current(0)
        div_entry.grid(row=1,column=1,padx=3,pady=3,sticky=W)

        #Roll Number
        rollno_label = Label(class_student_frame, text="Roll No:",font=("cambria",12,"bold"),bg="white")
        rollno_label.grid(row=1,column=2,padx=3,pady=3,sticky=W)
        
        rollno_entry=ttk.Entry(class_student_frame,width=15,font=("cambria",12,"bold"),textvariable=self.var_rollno)
        rollno_entry.grid(row=1,column=3,padx=3,pady=3,sticky=W)

        #gender
        gender_label = Label(class_student_frame, text="Gender:",font=("cambria",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=3,pady=3,sticky=W)
        
        gender_combo=ttk.Combobox(class_student_frame,font=("cambria",12,"bold"),width=13,state="read only",textvariable=self.var_gender)
        gender_combo["values"]=("Select Gender","Male","Female","Not prefer to say")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=2,sticky=W)
        
        #email
        email_label = Label(class_student_frame, text="Email:",font=("cambria",12,"bold"),bg="white")
        email_label.grid(row=2,column=2,padx=3,pady=3,sticky=W)
        
        email_entry=ttk.Entry(class_student_frame,width=15,font=("cambria",12,"bold"),textvariable=self.var_email)
        email_entry.grid(row=2,column=3,padx=3,pady=3,sticky=W)

        #Address  
        address_label = Label(class_student_frame, text="Address:",font=("cambria",12,"bold"),bg="white")
        address_label.grid(row=3,column=0,padx=3,pady=3,sticky=W)
        
        address_entry=ttk.Entry(class_student_frame,width=15,font=("cambria",12,"bold"),textvariable=self.var_address)
        address_entry.grid(row=3,column=1,padx=3,pady=3,sticky=W)


        # phone number
        phone_label = Label(class_student_frame, text="Phone No:",font=("cambria",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=3,pady=3,sticky=W)
        
        phone_entry=ttk.Entry(class_student_frame,width=15,font=("cambria",12,"bold"),textvariable=self.var_phone)
        phone_entry.grid(row=3,column=3,padx=3,pady=3,sticky=W)

        #dob
        dob_label = Label(class_student_frame, text="Date OF Birth:",font=("cambria",12,"bold"),bg="white")
        dob_label.grid(row=4,column=0,padx=3,pady=3,sticky=W)
        
        dob_entry=ttk.Entry(class_student_frame,width=15,font=("cambria",12,"bold"),textvariable=self.var_dob)
        dob_entry.grid(row=4,column=1,padx=3,pady=3,sticky=W)

        #mentor
        Mentor_label = Label(class_student_frame, text="Mentor of Class:",font=("cambria",12,"bold"),bg="white")
        Mentor_label.grid(row=4,column=2,padx=3,pady=3,sticky=W)
        
        Mentor_entry=ttk.Entry(class_student_frame,width=15,font=("cambria",12,"bold"),textvariable=self.var_Mentor)
        Mentor_entry.grid(row=4,column=3,padx=3,pady=3,sticky=W)

        #radio Buttons
        self.var_radio1=StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame,text="Take Photo Sample",variable=self.var_radio1,value="Yes",)
        radiobtn1.grid(row=5,column=0)
        self.var_radio2=StringVar()
        radiobtn2 = ttk.Radiobutton(class_student_frame,text="No Photo Sample",value="NO",variable=self.var_radio1,)
        radiobtn2.grid(row=5,column=1)

        #button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=FLAT,bg="white")
        btn_frame.place(x=1,y=180,width=549,height=40)
        #save button
        save_btn=Button(btn_frame,text="Save",width=10,font =( " Cambria" , 13 , " bold " ) , bg ="#2E8BC0" , fg ="white",command=self.adddata)
        save_btn.grid(row=0,column=0,padx=4,pady=3)

        update_btn=Button(btn_frame,text="Update",width=10,font =( " Cambria " , 13 , " bold " ) , bg ="#90ee90" , fg ="white")
        update_btn.grid(row=0,column=1,padx=4,pady=3)

        delete_btn=Button(btn_frame,text="Delete",width=10,font =( " cambria" , 13 , " bold " ) , bg ="#DC143C" , fg ="white")
        delete_btn.grid(row=0,column=2,padx=4,pady=3)

        reset_btn=Button(btn_frame,text="Reset",width=10,font =( " cambria " , 13 , " bold " ) , bg ="white" , fg ="Black")
        reset_btn.grid(row=0,column=3,padx=4,pady=3)

       
        btn_frame1=Frame(class_student_frame,bd=2,relief=FLAT,bg="white")
        btn_frame1.place(x=1,y=235,width=549,height=40)
        #taking
        takepic_btn=Button(btn_frame1,text="Take Pic",width=25,font =( " cambria " , 13 , " bold " ) , bg ="#2E8BC0" , fg ="white")
        takepic_btn.grid(row=1,column=0,padx=4,pady=3)
        #uploading the pic
        upload_btn=Button(btn_frame1,text="Upload Pic",width=25,font =( " cambria " , 13 , " bold " ) , bg ="#2E8BC0" , fg ="white")
        upload_btn.grid(row=1,column=1,padx=4,pady=3)
        
          #right frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("cambria",12,"bold"),bg="white")
        right_frame.place(x=600,y=10,width=657,height=540)

        #===========================searching system=================
        search_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,text="Search System",font=("cambria",12,"bold"),bg="white")
        search_frame.place(x=10,y=00,width=628,height=70)

        search_label = Label(search_frame, text="Search By:",font=("cambria",12,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=3,pady=3,sticky=W)

    
        search_combo=ttk.Combobox(search_frame,font=("cambria",12,"bold"),width=15,state="read only")
        search_combo["values"]=("Select ","Roll No","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=2,sticky=W)
        
        search_entry=ttk.Entry(search_frame,width=15,font=("cambria",12,"bold"),)
        search_entry.grid(row=0,column=2,padx=3,pady=3,sticky=W) 

        search_btn=Button(search_frame,text="Search",width=8,font =( " Cambria " , 13 , " bold " ) , bg ="crimson" , fg ="white")
        search_btn.grid(row=0,column=3,padx=4,pady=3)

        Showall_btn=Button(search_frame,text="Show All",width=8,font =( " Cambria " , 13 , " bold " ) , bg ="crimson" , fg ="white")
        Showall_btn.grid(row=0,column=4,padx=4,pady=3)

        #=================== table frame=================
        table_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=10,y=90,width=628,height=410)
#===============>scroll bar=============
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=('course','year','sem','id','name','div','rollno','gender','dob','email','phone','address','Mentor','photo'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("course",text="COURSE")
        self.student_table.heading("year",text="YEAR")
        self.student_table.heading("sem",text="SEMESTER")
        self.student_table.heading("id",text="STUDENT ID")
        self.student_table.heading("name",text="NAME")
        self.student_table.heading("div",text="DIVISION")
        self.student_table.heading("rollno",text="ROLL NO")
        self.student_table.heading("gender",text="GENDER")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="EMAIL")
        self.student_table.heading("phone",text="PHONE")
        self.student_table.heading("address",text="ADDRESS")
        self.student_table.heading("Mentor",text="MENTOR")
        self.student_table.heading("photo",text="PHOTO")
        self.student_table["show"]="headings"
  #width detting
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("rollno",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("Mentor",width=100)
        self.student_table.column("photo",width=100)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetchdata()
      
    #===============function declration============
    def adddata(self):
        if self.var_course.get()=="Select course" or self.var_name.get()==""or self.var_id=="":
            messagebox.showerror("Error","Enter the all the Fields",parent=self.root)
        else:
            try:
                conn= mysql.connector.connect(host="localhost",username="root",password="root",database="facerecogniser")
                my_cusrsor=conn.cursor()
                my_cusrsor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_rollno.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),       
                    self.var_address.get(),
                    self.var_Mentor.get(),
                   # self.var_photo.get(),
                    self.var_gender.get(),
                    self.var_radio1.get()

                                                                                                                            
            ))
                conn.commit()
                self.fetchdata()
                conn.close()
                messagebox.showinfo("Success","Data Inserted Successfully",parent=self.root)    
            except Exception as e:
                messagebox.showerror("Error","Data Not Inserted",parent=self.root)      
#=============================fetch data to tabel+=============================
    def fetchdata(self):
        try:
            conn= mysql.connector.connect(host="localhost",username="root",password="root",database="facerecogniser")
            my_cusrsor=conn.cursor()
            my_cusrsor.execute("select * from student")
            data=my_cusrsor.fetchall()
            
            if len(data)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("",END,values=i)
                conn.commit()
                conn.close()
        except Exception as e:
            messagebox.showerror("Error","Data Not Inserted",parent=self.root) 
     #get cursor over the text box================
    def get_cursor(self,event=""):
        cursor=self.student_table.focus()
        contents=self.student_table.item(cursor)
        data=contents['values']
        self.var_course.set(data[0])
        self.var_year.set(data[1])
        self.var_sem.set(data[2])
        self.var_id.set(data[3])
        self.var_name.set(data[4])
        self.var_div.set(data[5])
        self.var_rollno.set(data[6])
        self.var_gender.set(data[7])
        self.var_email.set(data[8])
        self.var_address.set(data[9])
        self.var_phone.set(data[10])
        self.var_dob.set(data[11])
        self.var_Mentor.set(data[12])
        self.var_radio1.set(data[13])
        #self.var_photo.set(data[12])
     
    #=============================update data=============================




if __name__ =="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
