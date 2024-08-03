from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import os
import email_pass
import smtplib
import time
class Login_System:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1350x700+0+0") #set to my screen dimensions
        self.root.title("Login System | Developed By Rebokile Sello")
        self.root.config(bg="white")

        self.otp=""

        #===images
        self.im1=Image.open("Login3.jpg")
        self.im1=self.im1.resize((400,460))
        self.im1=ImageTk.PhotoImage(self.im1)
        self.lbl_im1=Label(self.root, image=self.im1, relief=RAISED)
        self.lbl_im1.place(x=200, y=90)

        #===Login Frame
        self.employeeID=StringVar()
        self.password=StringVar()

        login_frame=Frame(self.root, bd=2, relief=RIDGE, bg="white")
        login_frame.place(x=650, y=90, width=350, height=390)

        title=Label(login_frame, text="Login System", font=("Elephant", 30, "bold"), background="white").place(x=0, y=0, relwidth=1)

        lbl_user=Label(login_frame, text="Employee ID", font=("Andalus", 15), bg="white", fg="#767171").place(x=50, y=70)
        txt_employeeID=Entry(login_frame,textvariable=self.employeeID, font=("times new roman", 15), bg="#ECECEC").place(x=50, y=110, width=250)

        lbl_pass=Label(login_frame, text="Password", font=("Andalus", 15), bg="white", fg="#767171").place(x=50, y=160)
        txt_pass=Entry(login_frame,textvariable=self.password, font=("times new roman", 15), bg="#ECECEC").place(x=50, y=200, width=250)

        btn_login=Button(login_frame,command=self.login, text="Log in", font=("Arial Rounded MT Bold", 15), bg="#00B0F0", activebackground="#00B0F0", activeforeground="white", fg="white", cursor="hand2").place(x=50, y=250, width=250, height=35)

        hr=Label(login_frame, bg="lightgray"). place(x=50, y=315, width=250, height=2)
        or_=Label(login_frame,text="OR", fg="lightgray",background="white", font=("times new roman", 15, "bold")). place(x=150, y=300)

        btn_forget=Button(login_frame, text="Forgot Password?",command=self.forget_window, font=("times new roman", 13), bg="white", fg="#00759E", bd=0, activebackground="white", activeforeground="#00759E").place(x=100, y=330)

        #===Create Account Frame
        register_frame=Frame(self.root, bd=2, relief=RIDGE, bg="white")
        register_frame.place(x=650, y=495, width=350, height=60)

        lbl_reg=Label(register_frame, text="Don't Have An Account?", font=("times new roman", 12), bg="white").place(x=40, y=15)
        btn_signup=Button(register_frame, text="Sign Up", font=("times new roman", 13, "bold"), bg="white", fg="#00759E", bd=0, activebackground="white", activeforeground="#00759E").place(x=200, y=15)

    def login(self):
        con = sqlite3.connect(database=r'pos.db')
        cur = con.cursor()
        try:
            if self.employeeID.get()=="" or self.password.get()=="":
                messagebox.showerror("Error", "All Fields are Required!", parent=self.root)
            else:
                cur.execute("select utype from employee where empID=? AND password=?", (self.employeeID.get(), self.password.get()))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror("Error", "Invalid Employee ID or Password or Both!", parent=self.root)
                else:
                    if user[0]=="Admin":
                        self.root.destroy()
                        os.system("python dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("python billing.py")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def forget_window(self):
        con = sqlite3.connect(database=r'pos.db')
        cur = con.cursor()
        try:
            if self.employeeID.get()=="":
                messagebox.showerror("Error", "Employee ID is Required", parent=self.root)
            else:
                cur.execute("select email from employee where empID=?", (self.employeeID.get(),))
                email=cur.fetchone()
                if email==None:
                    messagebox.showerror("Error", "Invalid Employee ID!", parent=self.root)
                else:
                    #Call send_email function
                    #===Forget Window
                    self.var_otp=StringVar()
                    self.var_new_password=StringVar()
                    self.var_con_password=StringVar()
                    chk=self.send_email(email[0])
                    if chk=='f':
                        messagebox.showerror("Error", "Connection Error! \nTry Again!", parent=self.root)
                    else:
                        self.forget_win=Toplevel(self.root)
                        self.forget_win.title("Reset Password")
                        self.forget_win.geometry("400x350+500+100")
                        self.forget_win.focus_force()
                        self.forget_win.config(bg="white")

                        title=Label(self.forget_win, text="Reset Password", font=("goudy old style", 15, "bold"), bg="#3f51b5", fg="white").pack(side=TOP, fill=X)
                        lbl_reset=Label(self.forget_win, text="Enter OTP sent to your email!", font=("times new roman ", 15), background="white").place(x=20, y=60)
                        txt_reset=Entry(self.forget_win, textvariable=self.var_otp, font=("times new roman ", 15), bg="lightgray").place(x=20, y=100, width=250, height=30)
                        self.btn_reset=Button(self.forget_win, text="Submit",command=self.validate_otp, font=("times new roman ", 13), bg="lightblue", cursor="hand2")
                        self.btn_reset.place(x=280, y=100, width=100, height=30)

                        lbl_new_password=Label(self.forget_win, text="Enter New Password", font=("times new roman ", 15), background="white").place(x=20, y=160)
                        txt_new_password=Entry(self.forget_win, textvariable=self.var_new_password, font=("times new roman ", 15), bg="lightgray").place(x=20, y=190, width=250, height=30)

                        lbl_confirm=Label(self.forget_win, text="Confirm New Password", font=("times new roman ", 15), background="white").place(x=20, y=225)
                        txt_confirm=Entry(self.forget_win, textvariable=self.var_con_password, font=("times new roman ", 15), bg="lightgray").place(x=20, y=255, width=250, height=30)

                        self.btn_update=Button(self.forget_win, text="Update",command=self.update_password, font=("times new roman ", 13), bg="lightblue",cursor="hand2", state=DISABLED)
                        self.btn_update.place(x=150, y=300, width=100, height=30)
        except Exception as ex:
            messagebox.showerror("Error!", f"Error due to: {str(ex)}", parent=self.root)

    def validate_otp(self):
        if int(self.otp)==int(self.var_otp.get()):
            self.btn_update.config(state=NORMAL)
            self.btn_reset.config(state=DISABLED)
        else:
            messagebox.showerror("Error", "Invalid OTP!\nTry Again!", parent=self.forget_win)

    def send_email(self, to_):
        s=smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        email_=email_pass.email_
        pass_=email_pass.pass_

        s.login(email_, pass_)

        self.otp=str(time.strftime("%H%S%M"))+str(time.strftime("%S"))
        
        subj="IMS Reset Password OTP"
        msg=f"Dear Sir/Madam,\n\nYour Reset OTP is {str(self.otp)}.\n\nRegards, \nRebokile Sello"
        msg="Subject:{}\n\n{}".format(subj,msg)
        s.sendmail(email_,to_,msg)
        chk=s.ehlo()
        if chk[0]==250:
            return 's'
        else:
            return 'f'
        
    def update_password(self):
        if self.var_new_password.get()=="" or self.var_con_password.get()=="":
            messagebox.showerror("Error!", "Password is Required!", parent=self.forget_win)
        elif self.var_new_password.get()!=self.var_con_password.get():
            messagebox.showerror("Error!", "The Two Passwords Must Match!", parent=self.forget_win)
        else:
            con = sqlite3.connect(database=r'pos.db')
        cur = con.cursor()
        try:
            cur.execute("Update employee password=? where empID=?", (self.var_new_password.get(), self.employeeID.get()))
            con.commit()
        except Exception as ex:
            messagebox.showerror("Error!", f"Error due to: {str(ex)}", parent=self.root)



root=Tk()
obj=Login_System(root)
root.mainloop()