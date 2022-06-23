from tkinter import *
from turtle import bgcolor 
from PIL import Image,ImageTk
from cv2 import COLOR_BAYER_BG2GRAY, FONT_HERSHEY_COMPLEX
from numpy import column_stack
from tkinter import messagebox
import cv2
import os
import numpy as np
import mysql.connector
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
        facerecognition_button=Button(self.root,text="Click Here Recognition",width=10,font =( " Cambria" , 13 , " bold " ) , bg ="green" , fg ="white",command=self.face_recog)
        facerecognition_button.place(x=575,y=325,height=80,width=190)

        # face recognition
    def face_recog(self):
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

                my_cusrsor.execute("select Rollno from student where Sid="+str(id))
                r=my_cusrsor.fetchone()
                r="+".join(r)

                # my_cusrsor.execute("select Sem from student where Sid="+str(id))
                # s=my_cusrsor.fetchone()
                # s="+".join(s)
                
                if confidence>77:
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{i}",(x,y-38),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Course:{c}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    # cv2.putText(img,f"Semester:{s}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),4)
                else:
                    cv2.rectangle(img,(x,y),(x+w+y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,y]
            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
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

#last 42:43














           



if __name__ =="__main__":
    root=Tk()
    obj=FaceRecognition(root)
    root.mainloop()

