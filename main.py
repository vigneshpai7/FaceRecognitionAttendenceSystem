
from tkinter import *
from tkinter import ttk
from tkinter import font
from PIL import Image,ImageTk



class Face_recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x750+0+0")
        self.root.title('Face recognition System')
         #bgimages 
        img=Image.open(r"C:\Users\paivi\Desktop\Face_Attendence_system\Images\image1.png")
        img=img.resize((1350,750),Image.LANCZOS)  #LANCZOS is used for conversion of high level image to low level image
        self.photoimg=ImageTk.PhotoImage(img)

        #setting of image in window with the help of label
        bgimage = Label(self.root,image=self.photoimg)
        bgimage.place(width=1350,height=750)
        #adding title project
        title_label  = Label(bgimage,text="FACE RECONITION ATTENDENCE SYSTEM SOFTWARE", font=("Comic Sans MS",25),fg="#4d4dff")
        title_label.place(x=0,y=600,width=1430,height=45)



        #student Button 1
        img2=Image.open(r"C:\Users\paivi\Desktop\Face_Attendence_system\Images\students.jpg")
        img2=img2.resize((180,180),Image.LANCZOS)  
        self.photoimg2=ImageTk.PhotoImage(img2)

        b1 = Button(bgimage,image=self.photoimg2,borderwidth=0,cursor = " hand2 ")
        b1.place(x=150,y=180,width=180,height=180)
        b1_1 =Button( bgimage ,text="Student Details", cursor = " hand2 ",font=("Cambria",15,"bold"),fg="#4d4dff")
        b1_1.place( x = 150 , y = 350 , width = 180 , height = 40 )
        #face recognition button
        img3=Image.open(r"C:\Users\paivi\Desktop\Face_Attendence_system\Images\face.png")
        img3=img3.resize((200,220),Image.LANCZOS)  
        self.photoimg3=ImageTk.PhotoImage(img3)

        b2 = Button(bgimage,image=self.photoimg3,borderwidth=0,cursor = " hand2 ")
        b2.place(x=450,y=180,width=180,height=180)
        b2_2 =Button( bgimage ,text="Face Recognition", cursor = " hand2 ",font=("Cambria",15,"bold"),fg="#4d4dff")
        b2_2.place( x = 450 , y = 350 , width = 180 , height = 40 )
        #Attendence -button
        img4=Image.open(r"C:\Users\paivi\Desktop\Face_Attendence_system\Images\attendence.jpg")
        img4=img4.resize((180,180),Image.LANCZOS)  
        self.photoimg4=ImageTk.PhotoImage(img4)

        b3 = Button(bgimage,image=self.photoimg4,borderwidth=0,cursor = " hand2 ")
        b3.place(x=750,y=180,width=180,height=180)
        b3_3 =Button( bgimage ,text="Attendence", cursor = " hand2 ",font=("Cambria",15,"bold"),fg="#4d4dff")
        b3_3.place( x = 750 , y = 350 , width = 180 , height = 40 )
        #Helpdesk Button
        img5=Image.open(r"C:\Users\paivi\Desktop\Face_Attendence_system\Images\help.jpg")
        img5=img5.resize((180,180),Image.LANCZOS)  
        self.photoimg5=ImageTk.PhotoImage(img5)

        b4 = Button(bgimage,image=self.photoimg5,borderwidth=0,cursor = " hand2 ")
        b4.place(x=1050,y=180,width=180,height=180)
        b4_4 =Button( bgimage ,text="Helpdesk", cursor = " hand2 ",font=("Cambria",15,"bold"),fg="#4d4dff")
        b4_4.place( x = 1050 , y = 350 , width = 180 , height = 40 )
# train face button
        img6=Image.open(r"C:\Users\paivi\Desktop\Face_Attendence_system\Images\train.png")
        img6=img6.resize((180,180),Image.LANCZOS)  
        self.photoimg6=ImageTk.PhotoImage(img6)

        b5 = Button(bgimage,image=self.photoimg6,borderwidth=0,cursor = " hand2 ")
        b5.place(x=150,y=400,width=180,height=180)
        b5_5 =Button( bgimage ,text="Train", cursor = " hand2 ",font=("Cambria",15,"bold"),fg="#4d4dff")
        b5_5.place( x = 150 , y = 550 , width = 180 , height = 40 )
#photo face button
        img7=Image.open(r"C:\Users\paivi\Desktop\Face_Attendence_system\Images\photo.png")
        img7=img7.resize((180,180),Image.LANCZOS)  
        self.photoimg7=ImageTk.PhotoImage(img7)

        b6 = Button(bgimage,image=self.photoimg7,borderwidth=0,cursor = " hand2 ")
        b6.place(x=450,y=400,width=180,height=180)
        b6_6 =Button( bgimage ,text="Photos", cursor = " hand2 ",font=("Cambria",15,"bold"),fg="#4d4dff")
        b6_6.place( x = 450 , y = 550 , width = 180 , height = 40 )

#Developer button
        img8=Image.open(r"C:\Users\paivi\Desktop\Face_Attendence_system\Images\dev.png")
        img8=img8.resize((180,180),Image.LANCZOS)  
        self.photoimg8=ImageTk.PhotoImage(img8)

        b7 = Button(bgimage,image=self.photoimg8,borderwidth=0,cursor = " hand2 ")
        b7.place(x=750,y=400,width=180,height=180)
        b7_7 =Button( bgimage ,text="Developer", cursor = " hand2 ",font=("Cambria",15,"bold"),fg="#4d4dff")
        b7_7.place( x = 750 , y = 550 , width = 180 , height = 40 )

#exit- button
        img9=Image.open(r"C:\Users\paivi\Desktop\Face_Attendence_system\Images\exit.png")
        img9=img9.resize((180,180),Image.LANCZOS)  
        self.photoimg9=ImageTk.PhotoImage(img9)

        b8 = Button(bgimage,image=self.photoimg9,borderwidth=0,cursor = " hand2 ")
        b8.place(x=1050,y=400,width=180,height=180)
        b8_8 =Button( bgimage ,text="Exit", cursor = " hand2 ",font=("Cambria",15,"bold"),fg="#4d4dff")
        b8_8.place( x = 1050 , y = 550 , width = 180 , height = 40 )        



if __name__ =="__main__":
    root=Tk()
    obj=Face_recognition_system(root)
    root.mainloop()


        
