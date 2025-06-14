from tkinter import *  # Fixed typo
from tkinter import ttk
from PIL import Image, ImageTk
import os
import mysql.connector
from tkinter import messagebox
import cv2
from tkinter import Label
from time import strftime



class Student:
    


    def __init__(self, root):
        self.root = root
        self.root.geometry("1400x700+0+0")  
        self.root.title("Face Recognition System")
        
        
        
        self.var_Student_Department=StringVar()
        self.var_Course=StringVar()
        self.var_year=StringVar()
        self.var_Semester=StringVar()
        self.var_Class_Student=StringVar()
        self.var_Class_Name=StringVar()
        self.var_Class_DOB=StringVar()
        self.var_Gender_Combo=StringVar()
        self.var_Student_Devision=StringVar()
        self.var_Roll_No=StringVar()
        self.var_Email=StringVar()
        self.var_Phone_No=StringVar()
        self.var_Address=StringVar()
        self.var_Teacher=StringVar()
        self.var_button_photo_sample=StringVar()
        
        
    
        
        
        self.title_lbl = Label(self.root, text="STUDENT MANAGEMENT SYSTEM", 
        font=("Arial", 20, "bold"), bg="grey", fg="black")
        self.title_lbl.place(x=0, y=131, width=1380, height=45)
        
        
        
        def time():
            string=strftime('%H:%M:%S:%p')
            lbl.config(text=string)
            lbl.after(1000,time)
        
        lbl = Label(self.title_lbl, font=('times', 20, 'bold'), background='black', foreground='Red')
        lbl.pack(anchor='w')
        time()    
        
        

        # Load and display images (same as before)
        img_biometric = Image.open(r"d:\Images\biometrics_mono-logo-1.png")
        img_biometric = img_biometric.resize((1380, 130), Image.Resampling.LANCZOS) 
        self.photoimg_biometric = ImageTk.PhotoImage(img_biometric)
        First_label = Label(self.root, image=self.photoimg_biometric)
        First_label.place(x=0, y=0, width=1380, height=130)

        img_student = Image.open(r"d:\Images\Student.webp")
        img_student = img_student.resize((1430, 600), Image.LANCZOS)  
        self.photoimg_student = ImageTk.PhotoImage(img_student)
        First_label = Label(self.root, image=self.photoimg_student)
        First_label.place(x=0, y=181, width=1430, height=600)

        # Label frame styles
        style = ttk.Style()
        style.configure("My.TLabelframe", background="silver") 
        style.configure("My.TLabelframe.Label", background="white", font=("Arial"))

        # Main Frame
        Student_frame = ttk.LabelFrame(self.root, padding=3, relief="ridge", text="STUDENT FORM",style="My.TLabelframe")
        Student_frame.place(x=0, y=178, width=1360, height=610)
        
        
        # Left Frame
        self.LEFT_frame = ttk.LabelFrame(Student_frame, padding=10, relief="ridge",text="Student Detail")
        self.LEFT_frame.place(x=5, y=0, width=650, height=600)
        
        
        img_left = Image.open(r"d:\Images\Attendence system.jpg")
        img_left = img_left.resize((620, 60),Image.LANCZOS)  
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        First_label = Label(self.LEFT_frame, image=self.photoimg_left)
        First_label.place(x=0, y=0, width=620, height=60)
        
        
    # current course frame
        
        Current_course = ttk.LabelFrame(self.LEFT_frame, padding=10, relief="ridge",text="Current Course")
        Current_course.place(x=0, y=63, width=680, height=126)  
        
        
        
    #Department
    
        
        Student_Department=Label(Current_course,text='Department:',font=("times new roman", '8'),background="white")
        Student_Department.grid(row=0,column=0)
        
        self.Student_Department=ttk.Combobox(Current_course,textvariable=self.var_Student_Department,font=("times new roman", '8'),state="readonly")
        self.Student_Department.grid(row=0,column=1,padx=10,pady=7,sticky='w')
        self.Student_Department["values"]=("Select Department","B-tech","BA","MA","BSC","Diploma")
        self.Student_Department.current(0)
        
        
        
    #Course Detail
    
        
        Course=Label(Current_course, text='Course',font=("times new roman", '8'), background="white")
        Course.grid(row=0,column=11)
        self.Course_Combo=ttk.Combobox(Current_course,font=("times new roman", '8'), textvariable=self.var_Course,state="readonly")
        self.Course_Combo.grid(row=0,column=12,padx=10,pady=7,sticky='w')
        self.Course_Combo["values"]=("Select Course","Computer science & Engeneeing","Civil","Mechanical","Biotecnology","Artificial Intelligence & machine Learning","Artificial Intellingence & Data Science"
        "Hindi","Sanskrit","History","Geography","Electrical Engeneering","Paint Technology","Hotel Management")
        self.Course_Combo.current(0)
        
        
        
        #Year
        
        
        
        Year=Label(Current_course, text='Year',font=("times new roman", '8'), background="white")
        Year.grid(row=5,column=0)
        self.Year_Combo=ttk.Combobox(Current_course,textvariable=self.var_year,font=("times new roman", '8'),state="readonly")
        self.Year_Combo.grid(row=5,column=1,padx=10,pady=7,sticky='w')
        self.Year_Combo["values"]=("Select Year","1","2","3","4","5") 
        self.Year_Combo.current(0)
        
        
        
        
        #Semester
        
        
        
        Semester=Label(Current_course, text='Semester',font=("times new roman", '8'), background="white")
        Semester.grid(row=5,column=11)
        self.Semester_Combo=ttk.Combobox(Current_course,textvariable=self.var_Semester,font=("times new roman", '8'),state="readonly")
        self.Semester_Combo.grid(row=5,column=12,padx=10,pady=7,sticky='w')
        self.Semester_Combo["values"]=("Select Semester","1","2","3","4","5","6","7","8",)
        self.Semester_Combo.current(0)
        
        
        
        
        #Class_Student_Information
        
        #Class student Frame 
        self.Class_Student_Frame = ttk.LabelFrame(self.LEFT_frame, padding=10, relief="ridge", text="Class Student Information")
        self.Class_Student_Frame.place(x=0, y=200, width=680, height=270)
        
        
        #Student ID

        Class_Student = Label(self.Class_Student_Frame, text="Student ID", font=("times new roman", '8'))
        Class_Student.grid(row=0, column=0, sticky="w")

        self.Class_Student = Entry(self.Class_Student_Frame,textvariable=self.var_Class_Student,font=("times new roman", '8'))
        self.Class_Student.grid(row=0, column=1, sticky='w',padx=5,pady=2.5)
        
        #student Name

        
        Class_Name = Label(self.Class_Student_Frame, text="Name",font=("times new roman", '8'))
        Class_Name.grid(row=1, column=0, sticky="w")

        self.Class_Name_Entry = Entry(self.Class_Student_Frame, textvariable=self.var_Class_Name,font=("times new roman", '8'))
        self.Class_Name_Entry.grid(row=1, column=1, sticky='w', padx=5,pady=2.5)
        
        
        #Date of Birth
        
        Class_DOB = Label(self.Class_Student_Frame, text="DOB", font=("times new roman", '8'))
        Class_DOB.grid(row=3, column=0, sticky="w")
        

        self.Class_DOB = Entry(self.Class_Student_Frame, textvariable=self.var_Class_DOB,font=("times new roman", '8'))
        self.Class_DOB.grid(row=3, column=1, sticky='w',padx=5,pady=2.5)
        
        
        
        
        #Gender
        
        
        Gender_Combo = Label(self.Class_Student_Frame, text="Gender", font=("times new roman", '8'))
        Gender_Combo.grid(row=2, column=0, sticky="w")


        self.Gender_Combo=ttk.Combobox(self.Class_Student_Frame,textvariable=self.var_Gender_Combo,font=("times new roman", '8'),state="readonly")
        self.Gender_Combo.grid(row=2,column=1,padx=5,pady=2.5,sticky='w')
        self.Gender_Combo["values"] = ("Select Gender", "Male", "Female", "Others")
        self.Gender_Combo.current(0)
    

        
        
        
        #student devision 

        
        Student_Devision = Label(self.Class_Student_Frame, text="Devision", font=("times new roman", '8'))
        Student_Devision.grid(row=4, column=0, sticky="w")
        

        self.Student_Devision = Entry(self.Class_Student_Frame, textvariable=self.var_Student_Devision, font=("times new roman", '8'))
        self.Student_Devision.grid(row=4, column=1, sticky='w',padx=5,pady=4)
        
        
        #Roll No
        

        Roll_No = Label(self.Class_Student_Frame, text="Roll No", font=("times new roman", '8'))
        Roll_No.grid(row=0, column=4, sticky="w")
        

        self.Roll_No = Entry(self.Class_Student_Frame,textvariable=self.var_Roll_No,font=("times new roman", '8'))
        self.Roll_No.grid(row=0, column=5, sticky='w',padx=5,pady=4)
        
        
        #Email ID
        
        Email = Label(self.Class_Student_Frame, text="Email_ID", font=("times new roman", '8'))
        Email.grid(row=1, column=4, sticky="w")
        

        self.Email = Entry(self.Class_Student_Frame,textvariable=self.var_Email ,font=("times new roman", '8'))
        self.Email.grid(row=1, column=5, sticky='w',padx=5,pady=4)
        
        
        #Phone
        
        Phone_No = Label(self.Class_Student_Frame, text="phone No", font=("times new roman", '8'))
        Phone_No.grid(row=2, column=4, sticky="w")
        

        self.Phone_No = Entry(self.Class_Student_Frame,textvariable=self.var_Phone_No,font=("times new roman", '8'))
        self.Phone_No.grid(row=2, column=5, sticky='w',padx=5,pady=4)
        
        #Address
        
        Address = Label(self.Class_Student_Frame, text="Address", font=("times new roman", '8'))
        Address.grid(row=3, column=4 ,sticky="w")
        

        self.Address = Entry(self.Class_Student_Frame,textvariable=self.var_Address,font=("times new roman", '8'))
        self.Address.grid(row=3, column=5, sticky='w',padx=5,pady=4)
    
        
        #Teacher
        
        Teacher = Label(self.Class_Student_Frame, text="Teacher", font=("times new roman", '8'))
        Teacher.grid(row=4, column=4 ,sticky="w")
        

        self.Teacher = Entry(self.Class_Student_Frame,textvariable=self.var_Teacher,font=("times new roman", '8'))
        self.Teacher.grid(row=4, column=5, sticky='w',padx=5,pady=4)
        
        
        #**************************************   Radio    Button   **************************************************
        
        
    

        button_Photo_Sample = ttk.Radiobutton( self.Class_Student_Frame,variable=self.var_button_photo_sample, text="Photo Sample",value="Yes",)
        button_Photo_Sample.place(x=445, y=0)

        
    
        button_No_Photo_Sample=ttk.Radiobutton(self.Class_Student_Frame,text="No Photo Sample",value="No")
        button_No_Photo_Sample.place(x=445,y=50)
        
        
        
        
        

        
        
        
        #------------------------------------------------------------------------Button Frame-------------------------------------------------------------------------------#
        
        
        Button_frame = ttk.LabelFrame(self.Class_Student_Frame, padding=5, relief="ridge")
        Button_frame.place(x=0 , y=130, width=500, height=60)
        
        

        
    
        
        button_Update=ttk.Button(Button_frame,command=self.update_data,text="Update",width=15,)
        button_Update.place(x=125,y=1)
        
        
        
        button_Delete=ttk.Button(Button_frame,command=self.delete_data,text="Delete",width=15, )
        button_Delete.place(x=245,y=1)
        
        
        
        button_Reset=ttk.Button(Button_frame,command=self.reset_data,text="Reset",width=15)
        button_Reset.place(x=365,y=1)
        
        
        button_Save=ttk.Button(Button_frame,command=self.add_data,text="SAVE",width=15,)
        button_Save.place(x=5,y=1)
        
        
        
        #Photo Take & Update Button
        
        
        
        
        
        
        button_Take_Photo = ttk.LabelFrame(self.Class_Student_Frame, padding=1, relief="ridge")
        button_Take_Photo.place(x=0 , y=191, width=500, height=50)
        
        
        
        Take_Photo=ttk.Button(button_Take_Photo,command=self.generate_dataset,text="Take Photo",width=20)
        Take_Photo.place(x=45,y=0)
        
        
        Update_photo=ttk.Button(button_Take_Photo,text="Update Photo",width=20)
        Update_photo.place(x=275,y=0)
        
        
        
        #Right Frame
        
        RIGHT_frame = ttk.LabelFrame(Student_frame, padding=10, relief="ridge",text="Student Detail")
        RIGHT_frame.place(x=682, y=1, width=650, height=600)
        
        
        img_right = Image.open(r"d:\Images\network-attacks-small.jpg")
        img_right = img_right.resize((620, 60), Image.LANCZOS)  
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        First_label = Label(RIGHT_frame, image=self.photoimg_right)
        First_label.place(x=0, y=0, width=620, height=60)
        
        
        Search_DATA = ttk.LabelFrame(RIGHT_frame, padding=10, relief="ridge",text="Search System ")
        Search_DATA.place(x=0, y=63, width=680, height=60)  
        
        Search_Level = Label(Search_DATA, text="Search By :", font=("times new roman", '8'))
        Search_Level.grid(row=0, column=0 ,sticky="w")
        
        Search_Combo=ttk.Combobox(Search_DATA,font=("times new roman", '8'),state="readonly")
        Search_Combo.grid(row=0,column=1,padx=10,pady=7,sticky='w')
        
        
        Search_Combo["values"]=("Search","Roll_No","Phone_No")
        Search_Combo.current(0)
        Search_Combo.grid(row=0,column=1,padx=10,pady=5)
        
        
        Student_Data = Entry(Search_DATA, font=("times new roman", '8'))
        Student_Data.grid(row=0, column=9, sticky='w',padx=10)
        
        
        Search_Combo=ttk.Combobox(Search_DATA,font=("times new roman", '8'))
        Search_Combo.grid(row=0,column=9,padx=10,sticky='w')
        
        
        Search_Combo["values"]=("Type")
        Search_Combo.current(0)
        Search_Combo.grid(row=0,column=9,padx=10,)
        
        
        
        Search_Button=ttk.Button(Search_DATA, text=" Click to search ",width=15)
        Search_Button.grid(row=0,column=15,padx=10)
        
        
        Show_All_Button=ttk.Button(Search_DATA, text=" Show All ",width=15)
        Show_All_Button.grid(row=0,column=20,padx=10)
        
        
        
        
        
        
        
        #################################################     Table     #############################################################
        
        
        
        
        Table_frame = Frame(Student_frame,relief=RIDGE,bd=3)
        Table_frame.place(x=685, y=200, width=635, height=300)
        
        
        
# Treeview


        
        Scroll_X = Scrollbar(Table_frame, orient=HORIZONTAL)
        Scroll_Y = Scrollbar(Table_frame, orient=VERTICAL)

        self.student_information = ttk.Treeview(Table_frame,columns=(
        "Student_Department", "Course", "year", "Semester", 
        "Class_Student", "Class_Name", "Class_DOB", "Gender_Combo", "Student_Devision", 
        "Roll_No", "Email", "Phone_No", "Address", "Teacher", "button_photo_sample"
            ),
        xscrollcommand=Scroll_X.set,
        yscrollcommand=Scroll_Y.set
        )
        
        

        Scroll_X.pack(side=BOTTOM,fill=X)
        Scroll_Y.pack(side=RIGHT,fill=Y)
        
        Scroll_X.config(command=self.student_information.xview)
        Scroll_Y.config(command=self.student_information.yview)
        
        self.student_information.heading('Student_Department',text="Department")
        self.student_information.heading('Course',text='Course')
        self.student_information.heading('year',text='year')
        self.student_information.heading('Semester',text='Semester')
        self.student_information.heading('Class_Student',text='Student_Id') 
        self.student_information.heading('Class_Name',text='Name') 
        self.student_information.heading('Class_DOB',text='DOB') 
        self.student_information.heading('Gender_Combo',text='Gender') 
        self.student_information.heading('Student_Devision',text='Devision') 
        self.student_information.heading('Roll_No',text='Roll_No') 
        self.student_information.heading('Email',text='Email')
        self.student_information.heading('Phone_No',text=' Contact')
        self.student_information.heading('Address',text='Address') 
        self.student_information.heading('Teacher',text='Teacher')  
        self.student_information.heading('button_photo_sample',text='Picture') 
        
        
        self.student_information.column('Student_Department',width=100)
        self.student_information.column('Course',width=100)
        self.student_information.column('year',width=100)
        self.student_information.column('Semester',width=100)
        self.student_information.column('Class_Student',width=100) 
        self.student_information.column('Class_Name',width=100) 
        self.student_information.column('Class_DOB',width=100)  
        self.student_information.column('Gender_Combo',width=100) 
        self.student_information.column('Student_Devision',width=100) 
        self.student_information.column('Roll_No',width=100) 
        self.student_information.column('Email',width=100)
        self.student_information.column('Phone_No',width=100) 
        self.student_information.column('Address',width=100) 
        self.student_information.column('Teacher',width=100)
        self.student_information.column('button_photo_sample',width=100)
        
        self.student_information["show"]='headings'
        
        self.student_information.pack(fill=BOTH,expand=1)
        self.student_information.bind("<ButtonRelease>"),self.get_cursor
        self.fetch_data
    
        
        
        
    def add_data(self):
        if self.var_Student_Department.get() == "Select Department" or self.var_Class_DOB.get() == "" or self.var_Roll_No.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            messagebox.showinfo("Successful",'Welcome To Biometric', parent=self.root)
            try:
                conn=mysql.connector.connect(host='127.0.0.1', user="root", password="Darshan2004@", database="biometric_software",port=3306)
                my_cursor = conn.cursor()
                my_cursor.execute("""insert into student_Info  values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (
                    self.var_Student_Department.get(),
                    self.var_Course.get(),
                    self.var_year.get(),           
                    self.var_Semester.get(),
                    self.var_Class_Student.get(),
                    self.var_Class_Name.get(),
                    self.var_Class_DOB.get(),
                    self.var_Gender_Combo.get(),
                    self.var_Student_Devision.get(),
                    self.var_Roll_No.get(),
                    self.var_Email.get(),
                    self.var_Phone_No.get(),
                    self.var_Address.get(),
                    self.var_Teacher.get(),
                    self.var_button_photo_sample.get()
                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student data has been added", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
                
                
                
                
                #__________________________________   FETCH DATA _________________________________________________________________#
        
    def  fetch_data(self):
        conn=mysql.connector.connect(host='127.0.0.1', user="root", password="Darshan004@", database="biometric_software",port=3306)
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM Student_Info")
        Data=my_cursor.fetchall()
        
        if  len(Data) !=0:
            self.student_information.delete(*self.student_information.get_children())
            for i in  Data:  
                self.student_information.insert("",END,values=i)
                conn.commit()
        conn.close()
        
        
 #-------------------------------------GET  CURSOR -----------------------------------------#      
        
    def get_cursor(self):
        cursor_focus=self.student_information.focus()
        content=self.student_information.item(cursor_focus)
        data=content["values"]
        
        
        self.var_Student_Department.set(data[0]),
        self.var_Course.set(data[1])
        self.var_year.set(data[2])
        self.var_Semester.set(data[3])
        self.var_Class_Student.set(data[4])
        self.var_Class_Name.set(data[5])
        self.var_Class_DOB.set(data[6])
        self.var_Gender_Combo.set(data[7])
        self.var_Student_Devision.set(data[8])
        self.var_Roll_No.set(data[9])
        self.var_Email.set(data[10])
        self.var_Phone_No.set(data[11])
        self.var_Address.set(data[12])
        self.var_Teacher.set(data[13])
        self.var_button_photo_sample.set(data[14])
        
    def update_data(self):
        if self.var_Student_Department.get() == "Select Department" or self.var_Class_DOB.get() == "" or self.var_Roll_No.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                Update=messagebox.askyesno('Update',"Do you want to Update this Student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host='127.0.0.1', user="root", password="Darshan2004@", database="biometric_software",port=3306)
                    my_cursor = conn.cursor()
                    my_cursor.execute("""UPDATE student.info SET Student_Department=%s, Course=%s, year=%s, Semester=%s,  Class_Name=%s, Class_DOB=%s, Gender_Combo=%s, Student_Devision=%s, Roll_No=%s, Email=%s, Phone_No=%s, Address=%s, Teacher=%s, button_photo_sample=%s WHERE Class_Student=%s
                    """, (
                    self.var_Student_Department.get(),
                    self.var_Course.get(),
                    self.var_year.get(),
                    self.var_Semester.get(),
                    self.var_Class_Name.get(),
                    self.var_Class_DOB.get(),
                    self.var_Gender_Combo.get(),
                    self.var_Student_Devision.get(),
                    self.var_Roll_No.get(),
                    self.var_Email.get(),
                    self.var_Phone_No.get(),
                    self.var_Address.get(),
                    self.var_Teacher.get(),
                    self.var_button_photo_sample.get(),
                    self.var_Class_Student.get()
                ))
                                            
                                        
                    
                
                else:
                    if  not Update:
                        return
                messagebox.showinfo("Successfull","Student Detail Updated Successfull",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
                
                
#--------------------------------------------------------------------------DELETE----------------------------------------------------------------------------------------#

    def  delete_data(self):
        if self.var_Class_Student.get()=="":
            messagebox.showerror("Error", "Student id Must be Required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student DeletePage", "Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host='127.0.0.1', user="root", password="Darshan2004@", database="biometric_software",port=3306)
                    my_cursor = conn.cursor()
                    sql="delete from student info where Class_Student=%s"
                    val=(self.var_Class_Student.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Reset", 'Successfully Reset student details',parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
                
                    


    def reset_data(self):
        self.var_Student_Department.set("Select Department")
        self.var_Course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_Semester.set("Select Semester")
        self.var_Class_Student.set("")
        self.var_Class_Name.set("")
        self.var_Class_DOB.set("")
        self.var_Gender_Combo.set("Select Gender")
        self.var_Student_Devision.set("")
        self.var_Roll_No.set("")
        self.var_Email.set("")
        self.var_Phone_No.set("")
        self.var_Address.set("")
        self.var_Teacher.set("")
        self.var_button_photo_sample.set("")
        
        
#-----------------------------------------------Genearate datasetor take photo----------------------------------#







    def generate_dataset(self):
        if self.var_Student_Department.get() == "Select Department" or self.var_Class_DOB.get() == "" or self.var_Roll_No.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
            return
        else:
            messagebox.showinfo("Successful", 'Welcome To Biometric system', parent=self.root)
        
            face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            def face_cropped(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    return img[y:y+h, x:x+w]
                return None

            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                messagebox.showerror("Camera Error", "Failed to open webcam.", parent=self.root)
                return

            img_id = 0
            while True:
                ret, my_frame = cap.read()
                if not ret:
                    break

                cropped = face_cropped(my_frame)
                if cropped is not None:
                    img_id += 1
                    face = cv2.resize(cropped, (450, 450))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                    file_name_path=r"C:\Users\darsh\OneDrive\Documents\ATTENDENCE SYSTEM\data"+str(self.Class_Student)+"."+str(img_id)+".jpg"
                    cv2.imwrite(file_name_path, face)

                    cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
                    cv2.imshow("Cropped Face", face)

                if cv2.waitKey(1) == 13 or img_id == 100:
                    break

            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Generated dataset completed!", parent=self.root)

        try:
            conn = mysql.connector.connect(host='127.0.0.1', user="root", password="Darshan2004@", database="biometric_software", port=3306)
            my_cursor = conn.cursor()
            my_cursor.execute('select * from student')
            myresult = my_cursor.fetchall()
            self.Class_Student = len(myresult) + 1  # auto-incrementing id

        # Update student info
            my_cursor.execute("""
                UPDATE student info SET Student_Department=%s, Course=%s, year=%s, Semester=%s, 
                Class_Name=%s, Class_DOB=%s, Gender_Combo=%s, Student_Devision=%s, 
                Roll_No=%s, Email=%s, Phone_No=%s, Address=%s, Teacher=%s, 
                button_photo_sample=%s WHERE Class_Student=%s
                """, (
                self.var_Student_Department.get(),
                self.var_Course.get(),
                self.var_year.get(),
                self.var_Semester.get(),
                self.var_Class_Name.get(),
                self.var_Class_DOB.get(),
                self.var_Gender_Combo.get(),
                self.var_Student_Devision.get(),
                self.var_Roll_No.get(),
                self.var_Email.get(),
                self.var_Phone_No.get(),
                self.var_Address.get(),
                self.var_Teacher.get(),
                self.var_button_photo_sample.get(),
                self.var_Class_Student.get()
                ))

            conn.commit()
            conn.close()
            self.fetch_data()
            self.reset_data()
            
        except Exception as es:
            messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
                
                                                                                                                                                                                                                                                                
if __name__ == "__main__":
    root = Tk()
    app = Student(root)
    root.mainloop()
    