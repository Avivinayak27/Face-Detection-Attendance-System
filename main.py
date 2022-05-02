from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import tkinter
from train import Train
from face import Face_Recognition
from attendance import Attendance
import os





class Face_Recogination_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x720+0+0")
        self.root.title("Face Recognisation system")
        
        #1st image
        img=Image.open("data/clg.jpg")
        img=img.resize((450,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f1_lbl=Label(self.root,image=self.photoimg)
        f1_lbl.place(x=0,y=0,width=450,height=130)
        
        #2nd image
        img1=Image.open("data/facialrecognition.png")
        img1=img1.resize((450,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f1_lbl=Label(self.root,image=self.photoimg1)
        f1_lbl.place(x=450,y=0,width=450,height=130)
        
        #3rd image
        img2=Image.open("data/university.jpg")
        img2=img2.resize((450,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f1_lbl=Label(self.root,image=self.photoimg2)
        f1_lbl.place(x=900,y=0,width=450,height=130)
        
        #backgroung image
        img3=Image.open("data/di.jpg")
        img3=img3.resize((1400,720),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1400,height=720)
        
        title_lbl=Label(bg_img,text="FACE RECOGINATION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1400,height=45)
        
        #student button
        img4=Image.open("data/student.jpg")
        img4=img4.resize((330,200),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,cursor="hand2",command=self.student_details)
        b1.place(x=110,y=60,width=330,height=200)
        
        b1_1=Button(bg_img,text="Student details",cursor="hand2",command=self.student_details,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=110,y=260,width=330,height=30)
        
        #detect face
        img5=Image.open("data/BestFacialRecognition.jpg")
        img5=img5.resize((330,200),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b2=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b2.place(x=540,y=60,width=330,height=200)
        
        b1_2=Button(bg_img,text="face detector",cursor="hand2",command=self.face_data,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        b1_2.place(x=540,y=260,width=330,height=30)
        
        #attendance
        img6=Image.open("data/facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img6=img6.resize((330,200),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b3=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_detail)
        b3.place(x=970,y=60,width=330,height=200)
        
        b1_3=Button(bg_img,text="attendance",cursor="hand2",command=self.attendance_detail,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        b1_3.place(x=970,y=260,width=330,height=30)
        
       
        
        #Train face buttton
        img8=Image.open("data/img1.jpeg")
        img8=img8.resize((330,200),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b5=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b5.place(x=110,y=310,width=330,height=200)
        
        b1_5=Button(bg_img,text="Train data",cursor="hand2",command=self.train_data,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        b1_5.place(x=110,y=510,width=330,height=30)
        
        #photos
        img9=Image.open("data/smart-attendance.jpg")
        img9=img9.resize((330,200),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b6=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b6.place(x=540,y=310,width=330,height=200)
        
        b1_6=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        b1_6.place(x=540,y=510,width=330,height=30)
        
        
        
        #Exit
        img11=Image.open("data/exit.jpg")
        img11=img11.resize((330,200),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b8=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iexit)
        b8.place(x=970,y=310,width=330,height=200)
        
        b1_8=Button(bg_img,text="Exit",cursor="hand2",command=self.iexit,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        b1_8.place(x=970,y=510,width=330,height=30)
        
        
    #***************Function button********************
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
            
    def open_img(self):
        os.startfile("samp")
            
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
            
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
    def attendance_detail(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def iexit(self):
        self.iexit=tkinter.messagebox.askyesno("Face Recognition","Are you Sure exit the project",parent=self.root)
        if self.iexit>0:
            self.root.destroy()
        else:
            return
           
        
        
if __name__=="__main__":
    root=Tk()
    obj=Face_Recogination_System(root)
    root.mainloop()
    
    
