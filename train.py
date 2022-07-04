from tkinter import *
from turtle import bgcolor 
from PIL import Image,ImageTk
from numpy import column_stack
from tkinter import messagebox
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x750+0+0")
        self.root.title('Face recognition System')
        trainbgimage=Image.open(r"Images\timg.jpg")
        trainbgimage=trainbgimage.resize((1350,750),Image.LANCZOS)  #LANCZOS is used for conversion of high level image to low level image
        self.photo_img=ImageTk.PhotoImage(trainbgimage) 
        bgimage = Label(self.root,image=self.photo_img)
        bgimage.place(width=1350,height=750)

        #button
        train_button=Button(self.root,text="Click here to Train",width=10,font =( " Cambria" , 13 , " bold " ) , bg ="#2E8BC0" , fg ="white",command=self.train_classifier)
        train_button.place(x=825,y=325,height=80,width=190)


    def train_classifier(self):
        try:
            data_dir=("data")    
            path = [os.path.join(data_dir,file)for file in os.listdir(data_dir)]

            faces=[]
            ids=[]

            for image in path:
                img=Image.open(image).convert('L') # l is  for gre scale image converting
                #grid system conversion
                imageNp=np.array(img,'uint8')#uint* is a data type
                id=int(os.path.split(image)[1].split('.')[1])

                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training",imageNp)
                cv2.waitKey(1)==13
            ids=np.array(ids)

        # Train classifier and save
            clf=cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces,ids)
            clf.write("classifier.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("Result","Training is completed")
        except Exception as e:
            messagebox.showinfo("Error","Sorry There are No data Present")



if __name__ =="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()

