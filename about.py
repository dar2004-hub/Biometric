from tkinter import *  # Fixed typo
from tkinter import ttk
from PIL import Image, ImageTk
import os
import mysql.connector
from tkinter import messagebox
import cv2
from tkinter import Label
from time import strftime
from tkinter import Text, Scrollbar, RIGHT, Y, LEFT, BOTH



class About:
    


    def __init__(self, root):
        self.root = root
        self.root.geometry("1400x6800+0+0")  
        self.root.title("Face Recognition System")
        
        

        # Load and display images (same as before)
        img_biometric = Image.open(r"c:\Users\darsh\OneDrive\Pictures\LTSSaddleback-Attendance.jpg")
        img_biometric = img_biometric.resize((1380, 128), Image.Resampling.LANCZOS) 
        self.photoimg_biometric = ImageTk.PhotoImage(img_biometric)
        First_label = Label(self.root, image=self.photoimg_biometric)
        First_label.place(x=0, y=0, width=1380, height=128)
        
        
        self.title_lbl = Label(self.root, text="ABOUT & HELP DESK ", 
        font=("Arial", 20, "bold"), bg="grey", fg="black")
        self.title_lbl.place(x=0, y=129, width=1380, height=70)
        
        
        def time():
            string=strftime('%H:%M:%S:%p')
            lbl.config(text=string)
            lbl.after(1000,time)
        
        lbl = Label(self.title_lbl, font=('times', 20, 'bold'), background='black', foreground='Red')
        lbl.pack(anchor='w')
        time()   

        img_student = Image.open(r"c:\Users\darsh\OneDrive\Pictures\About.jpg")
        img_student = img_student.resize((1430, 600), Image.LANCZOS)  
        self.photoimg_student = ImageTk.PhotoImage(img_student)
        First_label = Label(self.root, image=self.photoimg_student)
        First_label.place(x=0, y=200, width=1430, height=600)
        
        

# ---------------- ABOUT FRAME ----------------
        about_frame = ttk.LabelFrame(First_label, padding=3, relief="ridge", text="ABOUT", style="My.TLabelframe")
        about_frame.place(x=700, y=0, width=650, height=480)

# Scrollbar for About
        about_scroll = Scrollbar(about_frame)
        about_scroll.pack(side=RIGHT, fill=Y)

# Text widget for About
        about_text_widget = Text(about_frame, yscrollcommand=about_scroll.set, wrap="word", font=("times new roman", 12), bg="white")
        about_text_widget.pack(side=LEFT, fill=BOTH, expand=True)
        about_scroll.config(command=about_text_widget.yview)

# Insert about text
        about_text_widget.insert("1.0", 
            "Face Recognition Attendance System\n\n"
            "Developed by:\n"
            "• Darshan Chaubey (Team Leader)\n"
            "• Vandana Yadav\n"
            "• Shivam Shankar Pandey\n\n"
            "Description:\n"
            "This Face Recognition Attendance System is an intelligent software solution designed to automate the process "
            "of marking attendance using facial recognition technology. It eliminates the need for manual attendance, "
            "improves accuracy, and enhances security.\n\n"
            "Key Features:\n"
            "• Real-time face detection and recognition using OpenCV and Haar Cascade classifiers.\n"
            "• Automatic attendance marking and timestamp logging.\n"
            "• Secure database storage using MySQL.\n"
            "• User-friendly graphical interface built with Tkinter.\n"
            "• Easy to use for both teachers and administrators.\n\n"
            "Technologies Used:\n"
            "• Python\n"
            "• OpenCV (Computer Vision)\n"
            "• Tkinter (GUI)\n"
            "• MySQL (Database)\n\n"
            "Use Cases:\n"
            "• Schools, colleges, and universities\n"
            "• Offices and companies\n"
            "• Training centers and coaching institutes\n\n"
            "This system ensures that attendance is taken accurately and quickly with minimal human intervention, "
            "making the entire process more efficient and reliable."
            )

# Make text read-only
        about_text_widget.config(state="disabled")

# ---------------- SUPPORT FRAME ----------------
        support_frame = ttk.LabelFrame(First_label, padding=3, relief="ridge", text="Support", style="My.TLabelframe")
        support_frame.place(x=5, y=0, width=650, height=480)

# Scrollbar for Support
        support_scroll = Scrollbar(support_frame)
        support_scroll.pack(side=RIGHT, fill=Y)

# Text widget for Support
        support_text_widget = Text(support_frame, yscrollcommand=support_scroll.set, wrap="word", font=("times new roman", 12), bg="white")
        support_text_widget.pack(side=LEFT, fill=BOTH, expand=True)
        support_scroll.config(command=support_text_widget.yview)

# Insert support text
        support_text_widget.insert("1.0", 
            "Support Information:\n\n"
            "If you face any issues with the Face Recognition Attendance System, feel free to contact us.\n\n"
            "Contact Details:\n"
            "• Darshan Chaubey: darshan@example.com\n"
            "• Phone: +91-XXXXXXXXXX\n\n"
            "Available support includes:\n"
            "• Installation assistance\n"
            "• Troubleshooting errors\n"
            "• Training or demo sessions\n"
            "• Custom feature requests\n\n"
            "We are committed to providing quick and effective solutions to all users of this system.\n\n"
            "Thank you for using our software!"
            )        

# Make text read-only
        support_text_widget.config(state="disabled")

        
        
        
        
if __name__ == "__main__":
    root = Tk()
    app = About(root)
    root.mainloop()
    