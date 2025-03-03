from os import DirEntry
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import random #we are going to use this to generate invoice numbers
import os

class salesClass:
     def __init__(self, root):
          self.root = root
          self.root.geometry("1200x600+220+150") # Set to my screen dimensions
          self.root.title("Monate & Sons Scrapyard | Developed By Rebokile Sello")
          self.root.config(bg="white") 
          self.root.focus_force()
          #===
          self.var_invoice=StringVar()
          self.bill_list=[]

          #===title
          lbl_title=Label(self.root, text="View Customer Bills", font=("goudy old style", 30), bg="#33bbf9", fg="white", bd=3, relief=RIDGE).pack(side=TOP, fill=X, padx=10, pady=20)

          lbl_invoice=Label(self.root, text="Invoice Number", font=("times new roman", 16), bg="white").place(x=50, y=100)
          txt_invoice=Entry(self.root, textvariable=self.var_invoice, font=("times new roman", 16), bg="lightyellow").place(x=200, y=100, width=180, height=28)

          btn_search=Button(self.root, text="Search",command=self.search, font=("times new roman", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2").place(x=390, y=100, width=120, height=28)
          btn_clear=Button(self.root, text="Clear",command=self.clear, font=("times new roman", 15, "bold"), bg="lightgray", cursor="hand2").place(x=520, y=100, width=120, height=28)

          #===Bill List
          self.sales_frame = Frame(self.root, bd=3, relief=RIDGE)
          self.sales_frame.place(x=50, y=140, width=330, height=330)

          scrolly=Scrollbar(self.sales_frame, orient=VERTICAL)
          self.sales_list = Listbox(self.sales_frame, font=("goudy old style", 15), bg="white", yscrollcommand=scrolly.set)
          scrolly.pack(side=RIGHT, fill=Y)
          scrolly.config(command=self.sales_list.yview)
          self.sales_list.pack(fill=BOTH, expand=1)
          self.sales_list.bind("<ButtonRelease-1>", self.get_data)

          #===Bill Area
          self.bill_frame = Frame(self.root, bd=3, relief=RIDGE)
          self.bill_frame.place(x=400, y=140, width=507, height=330)
          scrolly2=Scrollbar(self.bill_frame, orient=VERTICAL)
          self.bill_area = Text(self.bill_frame, bg="lightyellow", yscrollcommand=scrolly2.set)

          lbl_title2=Label(self.bill_frame, text="Customer Bill Area", font=("goudy old style", 20), bg="orange").pack(side=TOP, fill=X)


          scrolly2.pack(side=RIGHT, fill=Y)
          scrolly2.config(command=self.bill_area.yview)
          self.bill_area.pack(fill=BOTH, expand=1)

          #===Image
          try:
            self.billLogo = Image.open("Blackhole.jpg")
            self.billLogo = self.billLogo.resize((280, 325))
            self.billLogo = ImageTk.PhotoImage(self.billLogo)
          except FileNotFoundError:
            messagebox.showerror("Error", "Image file 'Drogon.jpeg' not found.")

          lbl_image=Label(self.root, image=self.billLogo)
          lbl_image.place(x=910, y=140)

          
          self.show()



          #=======
     def show(self):
         del self.bill_list[:]
         self.sales_list.delete(0,END)
         #print(os.listdir('../Files'))
         for i in os.listdir('bill'):
             #print(i.split('.'),i.split('.')[-1])
             if i.split('.')[-1]=='txt':
                 self.sales_list.insert(END,i)
                 self.bill_list.append(i.split('.')[0])

     def get_data(self, ev):
         index_=self.sales_list.curselection()
         file_name=self.sales_list.get(index_)
         #0print(file_name)
         self.bill_area.delete('1.0', END)
         fp=open(f'bill/{file_name}', 'r')
         for i in fp:
             self.bill_area.insert(END,i)
         fp.close()

     def search(self):
         if self.var_invoice.get()=="":
             messagebox.showerror("Error", "Invoice number is required", parent=self.root)
         else:
             if self.var_invoice.get() in self.bill_list:
                 fp=open(f'bill/{self.var_invoice.get()}.txt', 'r')
                 self.bill_area.delete('1.0', END) 
                 for i in fp:
                    self.bill_area.insert(END,i)
                 fp.close()
             else:
                 messagebox.showerror("Error", "Invoice does not exist", parent=self.root)
            
     def clear(self):
         self.show()
         self.bill_area.delete('1.0', END)


if __name__ == "__main__":
    root = Tk()
    obj = salesClass(root)
    root.mainloop()
