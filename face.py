from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x720+0+0")
        self.root.title("face recognize")
        
        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",30,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1400,height=35)
        
        img_left=Image.open("data/face_detector1.jpg")
        img_left=img_left.resize((550,670),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        train_lbl=Label(self.root,image=self.photoimg_left)
        train_lbl.place(x=0,y=40,width=550,height=670)
        
        img_right=Image.open("data/facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_right=img_right.resize((800,670),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        train_lbl=Label(self.root,image=self.photoimg_right)
        train_lbl.place(x=550,y=40,width=800,height=670)
        
        
        b1_1=Button(train_lbl,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("times new roman",18,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=320,y=600,width=200,height=30)
    ########attendance
    def mark_attendance(self,n,p,d,i):
        with open("avi.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
                
            if((n not in name_list)) and (p not in name_list) and (d not in name_list) and (i not in name_list):
                now=datetime.now()
                d1=now.strftime("%d/%m/%y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{n},{p},{d},{i},{dtString},{d1},Present")
            

    ##################Face recognition
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            
            
            coord=[]
            
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recogination_system")
                my_cursor=conn.cursor()
                
                my_cursor.execute("select name from student where studentid="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)
                
                my_cursor.execute("select studentid from student where studentid="+str(id))
                p=my_cursor.fetchone()
                p="+".join(p)
                
                my_cursor.execute("select dep from student where studentid="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)
                
                my_cursor.execute("select year from student where studentid="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)
                                
                
                if confidence>77:
                    cv2.putText(img,f"Name:{n}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Studentid:{p}",(x,y-50),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Dep:{d}",(x,y-27),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Year:{i}",(x,y-2),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(n,p,d,i)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
                coord=[x,y,w,h]
                
                
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face Recognition",img)
            
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
            
        
        
if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()