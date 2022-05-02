from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x720+0+0")
        self.root.title("face recogination system")
        
        #variables********
        self.var_dep=StringVar()
        self.var_year=StringVar()
        self.var_name=StringVar()
        self.var_cource=StringVar()
        self.var_sem=StringVar()
        self.var_studentid=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_phoneno=StringVar()
        
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
        
        title_lbl=Label(bg_img,text="Student Management system",font=("times new roman",30,"bold"),bg="white",fg="dark green")
        title_lbl.place(x=0,y=0,width=1400,height=35)
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=40,width=1330,height=550)
        
        
        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Detail",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=2,width=640,height=520)
        
        sl_img=Image.open("data/1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        sl_img=sl_img.resize((620,130),Image.ANTIALIAS)
        self.photosl_img=ImageTk.PhotoImage(sl_img)
        
        left_lbl=Label(left_frame,image=self.photosl_img)
        left_lbl.place(x=7,y=0,width=620,height=110)
        
        #current cource
        cc_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Cource Information",font=("times new roman",12,"bold"))
        cc_frame.place(x=5,y=110,width=620,height=110)
        
        #department combo box
        dep_label=Label(cc_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0)
        
        dep_combo=ttk.Combobox(cc_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("select Department","CSE","IT","ECE","ME")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=5,pady=10,sticky=W)
        
        #cource
        dep_label=Label(cc_frame,text="Cource",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=2)
        
        dep_combo=ttk.Combobox(cc_frame,textvariable=self.var_cource,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("select Cource","Btech","BSc","BBA","Barch")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=5,pady=10,sticky=W)
        
        #Year
        dep_label=Label(cc_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=1,column=0)
        
        dep_combo=ttk.Combobox(cc_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("select year","1st","2nd","3rd","4th")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=1,padx=5,pady=10,sticky=W)
        
        #semester
        dep_label=Label(cc_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=1,column=2)
        
        dep_combo=ttk.Combobox(cc_frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("select Semester","1st","2nd")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=3,padx=5,pady=10,sticky=W)
        
        #Class student info
        sinfo_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information ",font=("times new roman",12,"bold"))
        sinfo_frame.place(x=5,y=220,width=620,height=275)
        
        #Student Id
        sinfo_label=Label(sinfo_frame,text="Student ID",font=("times new roman",12,"bold"),bg="white")
        sinfo_label.grid(row=0,column=0)
        
        sinfo_entry=ttk.Entry(sinfo_frame,textvariable=self.var_studentid,width=20,font=("times new roman",12,"bold"))
        sinfo_entry.grid(row=0,column=1,padx=5,pady=10,sticky=W)
        
        #Student Name
        sinfo_label=Label(sinfo_frame,text="Student Name",font=("times new roman",12,"bold"),bg="white")
        sinfo_label.grid(row=0,column=2)
        
        sinfo_entry=ttk.Entry(sinfo_frame,textvariable=self.var_name,width=20,font=("times new roman",12,"bold"))
        sinfo_entry.grid(row=0,column=3,padx=5,pady=10,sticky=W)
        
        #Gender
        sinfo_label=Label(sinfo_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        sinfo_label.grid(row=1,column=0)
        
        sinfo_combo=ttk.Combobox(sinfo_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=17,state="readonly")
        sinfo_combo["values"]=("select Gender","Male","Female")
        sinfo_combo.current(0)
        sinfo_combo.grid(row=1,column=1,padx=5,pady=10,sticky=W)
        
        #Email
        sinfo_label=Label(sinfo_frame,text="Email",font=("times new roman",12,"bold"),bg="white")
        sinfo_label.grid(row=1,column=2)
        
        sinfo_entry=ttk.Entry(sinfo_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        sinfo_entry.grid(row=1,column=3,padx=5,pady=10,sticky=W)
        
        
        #Phone no
        sinfo_label=Label(sinfo_frame,text="Phone no",font=("times new roman",12,"bold"),bg="white")
        sinfo_label.grid(row=2,column=0)
        
        sinfo_entry=ttk.Entry(sinfo_frame,textvariable=self.var_phoneno,width=20,font=("times new roman",12,"bold"))
        sinfo_entry.grid(row=2,column=1,padx=5,pady=10,sticky=W)
        
        #Address
        sinfo_label=Label(sinfo_frame,text="Address",font=("times new roman",12,"bold"),bg="white")
        sinfo_label.grid(row=2,column=2)
        
        sinfo_entry=ttk.Entry(sinfo_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        sinfo_entry.grid(row=2,column=3,padx=5,pady=10,sticky=W)
        
        
        #Radio buttons
        self.var_radio1=StringVar()
        radiobutton1=ttk.Radiobutton(sinfo_frame,variable=self.var_radio1,text="Take Photo Sample",value="yes")
        radiobutton1.grid(row=3,column=1)
        
        #Radio buttons2
        self.var_radio1=StringVar()
        radiobutton2=ttk.Radiobutton(sinfo_frame,variable=self.var_radio1,text="NO Photo Sample",value="no")
        radiobutton2.grid(row=3,column=3)
        
        #button frame
        b_frame=Frame(sinfo_frame,bd=2,relief=RIDGE)
        b_frame.place(x=0,y=160,width=610,height=35)
         
        #buttons
        save_btn=Button(b_frame,text="Save",command=self.add_data,width=16,font=("times new roman",12,"bold"),bg="red",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(b_frame,text="Update",command=self.update_data,width=16,font=("times new roman",12,"bold"),bg="red",fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(b_frame,text="Delete",command=self.delete_data,width=16,font=("times new roman",12,"bold"),bg="red",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(b_frame,text="Reset",command=self.reset_data,width=16,font=("times new roman",12,"bold"),bg="red",fg="white")
        reset_btn.grid(row=0,column=3)
        
        btn_frame1=Frame(sinfo_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=200,width=610,height=35)
        
        #take photo button
        tp_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=33,font=("times new roman",12,"bold"),bg="red",fg="white")
        tp_btn.grid(row=1,column=0)
        
        #update photo button
        up_btn=Button(btn_frame1,text="Update Photo Sample",width=33,font=("times new roman",12,"bold"),bg="red",fg="white")
        up_btn.grid(row=1,column=1)

        
        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Detail",font=("times new roman",12,"bold"))
        right_frame.place(x=670,y=2,width=640,height=520)
        
        rl_img=Image.open("data/girl.jpeg")
        rl_img=rl_img.resize((620,130),Image.ANTIALIAS)
        self.photorl_img=ImageTk.PhotoImage(rl_img)
        
        right_lbl=Label(right_frame,image=self.photorl_img)
        right_lbl.place(x=7,y=0,width=620,height=110)
        
        
        # ********Search system**************
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="search system",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=110,width=620,height=110)
        
        search_lbl=Label(search_frame,bd=2,relief=RIDGE,text="Search",font=("times new roman",15,"bold"),bg="red",fg="white")
        search_lbl.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=15,state="readonly")
        search_combo["values"]=("select","Student Id","Phone No","Name",)
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=10,sticky=W)
        
        search_btn=Button(search_frame,text="search",width=14,font=("times new roman",12,"bold"),bg="red",fg="white")
        search_btn.grid(row=1,column=1)
        
        showall_btn=Button(search_frame,text="showall",width=14,font=("times new roman",12,"bold"),bg="red",fg="white")
        showall_btn.grid(row=1,column=2)
        
        search_entry=ttk.Entry(search_frame,width=20,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=10,sticky=W)
        
        #table frame
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=220,width=620,height=280)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","cource","year","sem","studentid","name","gender","email","phoneno","address","photosample"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("cource",text="Cource")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("studentid",text="Student ID")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("phoneno",text="Phone No")
        self.student_table.heading("photosample",text="Photo Sample")
        self.student_table.column("dep",width=100)
        self.student_table.column("cource",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("studentid",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("phoneno",width=100)
        self.student_table.column("photosample",width=100)
        self.student_table["show"]="headings"
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
        
    #***************Function declaration***********
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()==""or self.var_studentid.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recogination_system")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.var_dep.get(),
                                                                                                self.var_cource.get(),
                                                                                                self.var_year.get(),
                                                                                                self.var_sem.get(),
                                                                                                self.var_studentid.get(),
                                                                                                self.var_name.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_phoneno.get(),
                                                                                                self.var_address.get(), 
                                                                                                self.var_radio1.get()
                                                                                               ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Sucess","Student details has been added sucessfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
                
    #*********fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recogination_system")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
            
    #******get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0])
        self.var_cource.set(data[1])
        self.var_year.set(data[2])
        self.var_sem.set(data[3])
        self.var_studentid.set(data[4])
        self.var_name.set(data[5])
        self.var_gender.set(data[6])
        self.var_email.set(data[7])
        self.var_phoneno.set(data[8])
        self.var_address.set(data[9])
        self.var_radio1.set(data[10])
        
    #Update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()==""or self.var_studentid.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Upadate=messagebox.askyesno("upadate","Do you want to update student details?",parent=self.root)
                if Upadate>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recogination_system")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set dep=%s,cource=%s,year=%s,sem=%s,name=%s,gender=%s,email=%s,phoneno=%s,address=%s,photo_sample=%s where studentid=%s",(self.var_dep.get(),
                                                                                                                                                                               self.var_cource.get(),
                                                                                                                                                                               self.var_year.get(),
                                                                                                                                                                               self.var_sem.get(),
                                                                                                                                                                               self.var_name.get(),
                                                                                                                                                                               self.var_gender.get(),
                                                                                                                                                                               self.var_email.get(),
                                                                                                                                                                               self.var_phoneno.get(),
                                                                                                                                                                               self.var_address.get(), 
                                                                                                                                                                               self.var_radio1.get(),
                                                                                                                                                                               self.var_studentid.get()
                                                                                                                                                                            ))
                else:
                    if not Upadate:
                        return
                messagebox.showinfo("sucess","student details updated sucessfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    #delete function
    def delete_data(self):
        if self.var_studentid.get()=="":
            messagebox.error("Error","studentid must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recogination_system")
                    my_cursor=conn.cursor()
                    sql="delete from student where studentid=%s"
                    val=(self.var_studentid.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Student details sucessfully deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
    #reset
    def reset_data(self):
        self.var_dep.set("select Department")
        self.var_cource.set("select Cource")
        self.var_year.set("select Year")
        self.var_sem.set("select sememster")
        self.var_studentid.set("")
        self.var_name.set("")
        self.var_gender.set("select")
        self.var_email.set("")
        self.var_phoneno.set("")
        self.var_address.set("")
        self.var_radio1.set("")
    
    #data set and photo samples
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()==""or self.var_studentid.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recogination_system")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set dep=%s,cource=%s,year=%s,sem=%s,name=%s,gender=%s,email=%s,phoneno=%s,address=%s,photo_sample=%s where studentid=%s",(self.var_dep.get(),
                                                                                                                                                                               self.var_cource.get(),
                                                                                                                                                                               self.var_year.get(),
                                                                                                                                                                               self.var_sem.get(),
                                                                                                                                                                               self.var_name.get(),
                                                                                                                                                                               self.var_gender.get(),
                                                                                                                                                                               self.var_email.get(),
                                                                                                                                                                               self.var_phoneno.get(),
                                                                                                                                                                               self.var_address.get(), 
                                                                                                                                                                               self.var_radio1.get(),
                                                                                                                                                                               self.var_studentid.get()==id+1
                                                                                                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                #333 load predefined data on face frontal from open cv
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)#1.3=scaling factor,minimum neighbour=5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="samp/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Crooped Face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generation data set compleated!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
        
                    
        
                    
                    
            
                          

if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()