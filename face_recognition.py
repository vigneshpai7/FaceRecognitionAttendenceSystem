from tkinter import *
from turtle import bgcolor 
from PIL import Image,ImageTk
from cv2 import COLOR_BAYER_BG2GRAY, FONT_HERSHEY_COMPLEX
from matplotlib import animation
from numpy import column_stack
from tkinter import messagebox
import cv2
import os
import numpy as np
import mysql.connector
from time import strftime
from datetime import datetime
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

        #button
        facerecognition_button=Button(self.root,text="Click Here Mark Attendence",width=10,font =( " Cambria" , 13 , " bold " ) , bg ="green" , fg ="white",command=self.face_recog)
        facerecognition_button.place(x=575,y=325,height=80,width=290)

        #adding note that click enter to exit
        note=Label(self.root,text="Click Enter to close the Attendence marking window",font=("cambria",12,"bold"),bg="white",fg="navyblue",bd=2,relief="solid")
        note.place(x=475,y=410,height=80,width=490)


    #=========mark_attendence======
    def attend(self,i,r,n):
        with open("attendence.csv","r+",newline="") as f:
            mydatalist=f.readlines()
            name_list=[]
            for line in mydatalist:
                entry=line.split(",")
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"{r},{i},{n},{dtString},{d1},Present\n")




    

        # face recognition
    def face_recog(self):
        try:    
            def draw_boundary(img,classifier,scaleFactor,minNeighbour,color,text,clf):
                #converting img to gray scale
                gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbour)
                coord=[]

                for (x,y,w,h) in features:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                    id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                    confidence=int((100*(1-predict/300)))

                    conn= mysql.connector.connect(host="localhost",username="root",password="root",database="facerecogniser")
                    my_cusrsor=conn.cursor()

                    my_cusrsor.execute("select Name from student where Sid="+str(id))
                    i=my_cusrsor.fetchone()
                    i="+".join(i)

                    my_cusrsor.execute("select Course from student where Sid="+str(id))
                    c=my_cusrsor.fetchone()
                    c="+".join(c)

                    my_cusrsor.execute("select Sid from student where Sid="+str(id))
                    r=my_cusrsor.fetchone()
                    r=" ".join(r)

                    # my_cusrsor.execute("select Sem from student where Sid="+str(id))
                    # s=my_cusrsor.fetchone()
                    # s="+".join(s)
                    
                    if confidence>80:
                        cv2.putText(img,f"Student ID :{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                        cv2.putText(img,f"Name:{i}",(x,y-38),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                        cv2.putText(img,f"Course:{c}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                        # cv2.putText(img,f"Semester:{s}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),4)
                        self.attend(i,r,c)
                    

                    else:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                        cv2.putText(img,"Unknown face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                    coord=[x,y,w,y]
                return coord

            def recognize(img,clf,faceCascade):
                coord=draw_boundary(img,faceCascade,1.1,20,(255,25,255),"Face",clf)
                return img
            faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")    
            clf=cv2.face.LBPHFaceRecognizer_create()
            clf.read("classifier.xml")
            video_cap=cv2.VideoCapture(0)

            while True:
                ret,img =video_cap.read()
                img=recognize(img,clf,faceCascade)
                cv2.imshow("Welcome to Face Recognition",img)

                if cv2.waitKey(1)==13:
                    break

            video_cap.release()
            cv2.destroyAllWindows()
        except Exception as e:
            messagebox.showerror("Error","No data in prsent in database please add data")
            print(e)
            self.root.destroy()
            os.system("python facerecognition.py")
            return
            pass    

#last 42:43














           



if __name__ =="__main__":
    root=Tk()
    obj=FaceRecognition(root)
    root.mainloop()

