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
import csv
from tkinter import filedialog

mydata=[]

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x720+0+0")
        self.root.title("face recognize")
        
        self.var_name=StringVar()
        self.var_studentid=StringVar()
        self.var_dep=StringVar()
        self.var_year=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attendance=StringVar()
        
        #1st image
        img=Image.open("data/clg.jpg")
        img=img.resize((720,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f1_lbl=Label(self.root,image=self.photoimg)
        f1_lbl.place(x=0,y=0,width=720,height=200)
        
        #2nd image
        img1=Image.open("data/facialrecognition.png")
        img1=img1.resize((720,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f1_lbl=Label(self.root,image=self.photoimg1)
        f1_lbl.place(x=720,y=0,width=720,height=200)
        
         #backgroung image
        img3=Image.open("data/di.jpg")
        img3=img3.resize((1400,720),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1400,height=720)
        
        title_lbl=Label(bg_img,text="ATTENDANCE",font=("times new roman",30,"bold"),bg="white",fg="dark Red")
        title_lbl.place(x=0,y=0,width=1400,height=35)
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=40,width=1330,height=550)
        
        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Detail",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=2,width=640,height=440)
        
        sl_img=Image.open("data/1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        sl_img=sl_img.resize((620,130),Image.ANTIALIAS)
        self.photosl_img=ImageTk.PhotoImage(sl_img)
        
        left_lbl=Label(left_frame,image=self.photosl_img)
        left_lbl.place(x=7,y=0,width=620,height=110)
        
        #Details frame
        cc_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Cource Information",font=("times new roman",12,"bold"))
        cc_frame.place(x=5,y=110,width=620,height=300)
        
        #Student Id
        sinfo_label=Label(cc_frame,text="Student ID",font=("times new roman",12,"bold"),bg="white")
        sinfo_label.grid(row=0,column=0)
        
        sinfo_entry=ttk.Entry(cc_frame,textvariable=self.var_studentid,width=20,font=("times new roman",12,"bold"))
        sinfo_entry.grid(row=0,column=1,padx=5,pady=10,sticky=W)
        
        #Student Name
        sinfo_label=Label(cc_frame,text="Student Name",font=("times new roman",12,"bold"),bg="white")
        sinfo_label.grid(row=0,column=2)
        
        sinfo_entry=ttk.Entry(cc_frame,textvariable=self.var_name,width=20,font=("times new roman",12,"bold"))
        sinfo_entry.grid(row=0,column=3,padx=5,pady=10,sticky=W)
        
        #Dept
        sinfo_label=Label(cc_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        sinfo_label.grid(row=1,column=0)
        
        sinfo_entry=ttk.Entry(cc_frame,textvariable=self.var_dep,width=20,font=("times new roman",12,"bold"))
        sinfo_entry.grid(row=1,column=1,padx=5,pady=10,sticky=W)
        
        #Year
        sinfo_label=Label(cc_frame,text="year",font=("times new roman",12,"bold"),bg="white")
        sinfo_label.grid(row=1,column=2)
        
        sinfo_entry=ttk.Entry(cc_frame,textvariable=self.var_year,width=20,font=("times new roman",12,"bold"))
        sinfo_entry.grid(row=1,column=3,padx=5,pady=10,sticky=W)
        
        #time
        sinfo_label=Label(cc_frame,text="Time",font=("times new roman",12,"bold"),bg="white")
        sinfo_label.grid(row=2,column=0)
        
        sinfo_entry=ttk.Entry(cc_frame,textvariable=self.var_time,width=20,font=("times new roman",12,"bold"))
        sinfo_entry.grid(row=2,column=1,padx=5,pady=10,sticky=W)
        
        
        #Date
        sinfo_label=Label(cc_frame,text="Date",font=("times new roman",12,"bold"),bg="white")
        sinfo_label.grid(row=2,column=2)
        
        sinfo_entry=ttk.Entry(cc_frame,textvariable=self.var_date,width=20,font=("times new roman",12,"bold"))
        sinfo_entry.grid(row=2,column=3,padx=5,pady=10,sticky=W)
        
        #Status
        sinfo_label=Label(cc_frame,text="Status",font=("times new roman",12,"bold"),bg="white")
        sinfo_label.grid(row=3,column=0)
        
        sinfo_combo=ttk.Combobox(cc_frame,textvariable=self.var_attendance,font=("times new roman",12,"bold"),width=17,state="readonly")
        sinfo_combo["values"]=("Select Status","Present","Absent")
        sinfo_combo.current(0)
        sinfo_combo.grid(row=3,column=1,padx=5,pady=10,sticky=W)
        
        #button frame
        b_frame=Frame(cc_frame,bd=2,relief=RIDGE)
        b_frame.place(x=0,y=230,width=610,height=35)
         
        #buttons
        save_btn=Button(b_frame,text="Import CSV",command=self.import_Csv,width=16,font=("times new roman",12,"bold"),bg="red",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(b_frame,text="Export CSV",command=self.export_Csv,width=16,font=("times new roman",12,"bold"),bg="red",fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(b_frame,text="Update",width=16,font=("times new roman",12,"bold"),bg="red",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(b_frame,text="Reset",command=self.reset_data,width=16,font=("times new roman",12,"bold"),bg="red",fg="white")
        reset_btn.grid(row=0,column=3)
        
        
        
        
        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance",font=("times new roman",12,"bold"))
        right_frame.place(x=670,y=2,width=640,height=440)
        
        right_lbl=Label(right_frame,relief=RIDGE,bg="white")
        right_lbl.place(x=7,y=0,width=620,height=410)
        
        
        #scroll bar table
        scroll_x=ttk.Scrollbar(right_lbl,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(right_lbl,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(right_lbl,column=("name","studentid","dep","year","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("studentid",text="Student Id")
        self.AttendanceReportTable.heading("dep",text="Dep")
        self.AttendanceReportTable.heading("year",text="Year")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("studentid",width=100)
        self.AttendanceReportTable.column("dep",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("year",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
        
        
        
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
                
    def import_Csv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
            
    def export_Csv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Fount to Export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data is Exported to"+os.path.basename(fln)+"Successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
                
                
    def get_cursor(self,event=""):
        cursor_row= self.AttendanceReportTable.focus()
        content= self.AttendanceReportTable.item(cursor_row)
        data=content['values']
        self.var_name.set(data[0])
        self.var_studentid.set(data[1])
        self.var_dep.set(data[2])
        self.var_year.set(data[3])
        self.var_time.set(data[4])
        self.var_date.set(data[5])
        self.var_attendance.set(data[6])
    def reset_data(self):
        self.var_name.set("")
        self.var_studentid.set("")
        self.var_dep.set("")
        self.var_year.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance.set("")
        
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()