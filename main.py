from tkinter import *  
from tkinter import ttk
from PIL import Image, ImageTk
from studentData import Student
from train import Train
from face_recogniser import Face_Recognition
from developer import Developer
from about import About
import os
from attendence import Attendence
from tkinter import messagebox
from time import strftime
from datetime import datetime
from tkinter import Label



class Face_recognition_System:
    
    def __init__(self, root):
        
        self.root = root
        self.root.geometry("1400x670+0+0")  # Correct format for geometry
        self.root.title("Face Recognition System")
        
        self.title_lbl = Label(self.root, text="Face Recognition Software System", 
        font=("Arial", 20, "bold"), bg="grey", fg="black")
        self.title_lbl.place(x=0, y=130, width=1480, height=40)
        
        def time():
            string=strftime('%H:%M:%S:%p')
            lbl.config(text=string)
            lbl.after(1000,time)
        
        lbl = Label(self.title_lbl, font=('times', 20, 'bold'), background='black', foreground='Red')
        lbl.pack(anchor='w')
        time()     

        # Load Image
        img = Image.open(r"c:\Users\darsh\OneDrive\Pictures\LTSSaddleback-Attendance.jpg")
        img = img.resize((1380, 130), Image.LANCZOS)  # Use Image.LANCZOS instead of Image.ANTIALIAS
        self.photoimg = ImageTk.PhotoImage(img)

        # Display Image
        First_label = Label(self.root, image=self.photoimg)
        First_label.place(x=0, y=0, width=1380, height=130)
        
        
        # Load Image
        imgC = Image.open(r"d:\Images\OIP (1).jpg")
        imgC = imgC.resize((1430, 600), Image.LANCZOS) 
        self.photoimgC = ImageTk.PhotoImage(imgC)

        # Display Image
        First_0 = Label(self.root, image=self.photoimgC)
        First_0.place(x=0, y=170, width=1400, height=600)
        
        
        ######################################################    BUTTON   #########################################################
        
        
        
        # Load  Image  Student Detail
        
        
        
        button1 = Image.open(r"d:\Images\vector-male-student-icon.jpg")
        button1 = button1.resize((60, 60), Image.LANCZOS) 
        self.photobutton1 = ImageTk.PhotoImage(button1)

        # Display Image
        First_1 = Label(self.root, image=self.photobutton1)
        First_1.place(x=50, y=200, width=60, height=60)
        
        B1 = ttk.Button(self.root, image=self.photobutton1,command=self.Student_Detail ,cursor= "hand2")
        B1.place(x=50, y=200, width=80, height=80)
        
        B1_1 = Button(text="STUDENTS", compound="center", font=("Arial", 10, "bold"), fg="black",command=self.Student_Detail,cursor="hand2")
        B1_1.place(x=50, y=260, width=81, height=20)
        
        
        
        # Load Image  Data
        
        
        
        button2 = Image.open(r"d:\Images\th.jpg")
        button2 = button2.resize((60, 60), Image.LANCZOS)  
        self.photobutton2 = ImageTk.PhotoImage(button2)

        # Display Image
        First_2 = Label(self.root, image=self.photobutton2)
        First_2.place(x=50, y=320, width=80, height=80)
        
        B2 = ttk.Button(self.root, image=self.photobutton2 , cursor= "hand2",command=self.open_img)
        B2.place(x=50, y=320, width=80, height=80)
        
        B1_2 = Button(text="Photos", compound="center",command=self.open_img ,font=("Arial", 10, "bold"), fg="black", cursor="hand2")
        B1_2.place(x=50, y=380, width=81, height=20)
        
        
        
        
        # Load Image
        button3 = Image.open(r"c:\Users\darsh\OneDrive\Pictures\Train Dataset.jpg")
        button3 = button3.resize((80, 80), Image.LANCZOS)  
        self.photobutton3 = ImageTk.PhotoImage(button3)

        # Display Image
        First_3 = Label(self.root, image=self.photobutton3)
        First_3.place(x=46, y=437, width=80, height=80)
        
        B3 = ttk.Button(self.root, image=self.photobutton3 ,command=self.train_data,cursor= "hand2")
        B3.place(x=48, y=440, width=80, height=80)
        
        B1_3 = Button(text="Train Data", compound="center" ,command=self.train_data,font=("Arial", 10, "bold"), fg="black", cursor="hand2")
        B1_3.place(x=48, y=499, width=81, height=20)  
        
        
        
        
        # Load Image
        button4 = Image.open(r"c:\Users\darsh\OneDrive\Pictures\App dev.jpg")
        button4 = button4.resize((78, 78), Image.LANCZOS) 
        self.photobutton4 = ImageTk.PhotoImage(button4)

        # Display Image
        First_4 = Label(self.root, image=self.photobutton4)
        First_4.place(x=50, y=557, width=78, height=78)
        
        B4 = ttk.Button(self.root, image=self.photobutton4, cursor= "hand2",command=self.Developer_button)
        B4.place(x=46, y=557, width=78, height=78)
        
        B1_4 = Button(text="DEVELOPER", compound="center", font=("Arial", 10, "bold"), command=self.Developer_button,fg="black", cursor="hand2")
        B1_4.place(x=46, y=628, width=81, height=20)
        
        
        
        
        # Load Image
        button5 = Image.open(r"d:\Images\detector.jpg")
        button5 = button5.resize((80, 80), Image.LANCZOS) 
        self.photobutton5 = ImageTk.PhotoImage(button5)

        # Display Image
        First_5 = Label(self.root, image=self.photobutton5)
        First_5.place(x=1200, y=200, width=80, height=80)
        
        B5 = ttk.Button(self.root, image=self.photobutton5,command=self.face_data,cursor= "hand2")
        B5.place(x=1200, y=200, width=80, height=80)
        
        B1_5 = Button(text="DETECTOR", compound="center",command=self.face_data,font=("Arial", 10, "bold"), fg="black", cursor="hand2")
        B1_5.place(x=1200, y=260, width=81, height=20)


        # Load Image
        button6 = Image.open(r"c:\Users\darsh\OneDrive\Pictures\attendance-icon-design-free-vector.jpg")
        button6 = button6.resize((80, 80), Image.LANCZOS) 
        self.photobutton6 = ImageTk.PhotoImage(button6)

        # Display Image
        First_6 = Label(self.root, image=self.photobutton6)
        First_6.place(x=1200, y=320, width=80, height=80)
        
        button6 = ttk.Button(self.root, image=self.photobutton6,command=self.Attendence,cursor="hand2")
        button6.place(x=1200, y=320, width=80, height=80)
        
        B1_6 = Button(text="ATTENDENCE", compound="center",command=self.Attendence,font=("Arial", 8, "bold"), fg="black", cursor="hand2")
        B1_6.place(x=1200, y=380, width=81, height=20)
        
        
        
        
        # Load Image
        button7 = Image.open(r"c:\Users\darsh\OneDrive\Pictures\help.jpg")
        button7 = button7.resize((80, 80), Image.LANCZOS)  
        self.photobutton7 = ImageTk.PhotoImage(button7)

        # Display Image
        First_label = Label(self.root, image=self.photobutton7)
        First_label.place(x=1200, y=440, width=80, height=80)
        
        B7 = ttk.Button(self.root, image=self.photobutton7, command=self.About,cursor= "hand2")
        B7.place(x=1200, y=440, width=80, height=80)
        
        B1_7 = Button(text="About", compound="center", command=self.About,font=("Arial", 10, "bold"), fg="black", cursor="hand2")
        B1_7.place(x=1200, y=500, width=81, height=20)
        
        
        
        
        button8 = Image.open(r"d:\Images\EXIT.jpg")
        button8 = button8.resize((80, 80), Image.LANCZOS)  
        self.photobutton8 = ImageTk.PhotoImage(button8)
        
        
        First_label = Label(self.root, image=self.photobutton8)
        First_label.place(x=1200, y=560, width=80, height=80)
        
        B4 = ttk.Button(self.root, image=self.photobutton8,  command=self.iExit,cursor= "hand2")
        B4.place(x=1200, y=560, width=80, height=80)
        
        B1_4 = Button(text="Exit", compound="center", command=self.iExit,font=("Arial", 10, "bold"), fg="black", cursor="hand2")
        B1_4.place(x=1200, y=630, width=81, height=20)
        
        
    def open_img(self):
        os.startfile("User")
        
        
        
        
    def iExit(self):
        exit_confirm = messagebox.askyesno("Face Recognition", "Are you sure you want to exit?")
        if exit_confirm:
            self.root.destroy()
            
            

#***********************************************    Function Button    ***************************************************


    def Student_Detail(self):
        self.new_window=Toplevel(self.root)
        self.App= Student(self.new_window)
        
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.App = Train(self.new_window)
        
        
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.App = Face_Recognition(self.new_window)
        
    def Attendence(self):
        self.new_window = Toplevel(self.root)
        self.App = Attendence(self.new_window)
        
    def Developer_button(self):
        self.new_window = Toplevel(self.root)
        self.App = Developer(self.new_window)
        
        
    def About(self):
        self.new_window = Toplevel(self.root)
        self.App = About(self.new_window)
        
        
        
    
        
    
        
    




if __name__ == "__main__" :
    root = Tk()
    obj = Face_recognition_System(root) 
    root.mainloop()

