from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x720+0+0")
        self.root.title("train")
        
        
        title_lbl=Label(self.root,text="Train Data Set",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1400,height=35)
        
        img_top=Image.open("data/smart-attendance.jpg")
        img_top=img_top.resize((1400,260),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        train_lbl=Label(self.root,image=self.photoimg_top)
        train_lbl.place(x=0,y=40,width=1400,height=260)
        
        #button
        b1_5=Button(self.root,text="Train data",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="darkblue",fg="white")
        b1_5.place(x=0,y=310,width=1400,height=80)
        
        img_bottom=Image.open("data/student.jpg")
        img_bottom=img_bottom.resize((1400,260),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        
        train1_lbl=Label(self.root,image=self.photoimg_bottom)
        train1_lbl.place(x=0,y=400,width=1400,height=260)
    
    def train_classifier(self):
        data_dir="samp"
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        
        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L')  # l= gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])        
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        #*********train classifier
        
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","training datasets completed")
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()