from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
#we are going to change this to the Car file where we will store all the cars that come into the businss such that when we add the products salvaged from a car, we just select the particular car and this will help us prepare the finacial statements and check how much a partical car made
class supplierClass:
     def __init__(self, root):
          self.root = root
          self.root.geometry("1100x550+220+230") # Set to my screen dimensions
          self.root.title("Monate & Sons Scrapyard | Developed By Rebokile Sello")
          self.root.config(bg="white")
          self.root.focus_force()
          
          #===All variables
          self.var_searchby = StringVar()
          self.var_searchtxt = StringVar()

          self.var_sup_invoice = StringVar()
          self.var_name = StringVar()
          self.var_contact = StringVar()
          
          
          
          #===Search Frame

          #===Options
          lbl_search = Label(self.root, text="Search By Invoice No.", bg="white", font=("goudy old style", 15))
          lbl_search.place(x=700, y=80)

          txt_search = Entry(self.root, textvariable=self.var_searchtxt, font=("goudy old style", 15), bg="lightyellow").place(x=880, y=80)
          btn_search = Button(self.root, text="Search",command=self.search, font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2").place(x=880, y=120, width=205, height=30)

          #===Title
          title = Label(self.root, text="Supplier Details", font=("goudy old style", 20, "bold"), bg="#0f4d7d", fg="white").place(x=50, y=10, width=1000, height=40)

          #======Content
          #===Row 1
          lbl_supplier_invoice = Label(self.root, text="Invoice Number", font=("goudy old style", 15), bg="white").place(x=50, y=80)

          txt_supplier_invoice = Entry(self.root, textvariable=self.var_sup_invoice, font=("goudy old style", 15), bg="lightyellow").place(x=190, y=80, width=180)


          #===Row 2
          lbl_name = Label(self.root, text="Name", font=("goudy old style", 15), bg="white").place(x=50, y=120)

          txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15), bg="lightyellow").place(x=190, y=120, width=180)

          #===Row 3
          lbl_contact = Label(self.root, text="Contact", font=("goudy old style", 15), bg="white").place(x=50, y=160)

          txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15), bg="lightyellow").place(x=190, y=160, width=180)

          #===Row 4
          lbl_desc = Label(self.root, text="Description", font=("goudy old style", 15), bg="white").place(x=50, y=200)
          self.txt_desc = Text(self.root, font=("goudy old style", 15), bg="lightyellow")
          self.txt_desc.place(x=190, y=200, width=470, height=240)

          #===Buttons
          btn_add = Button(self.root, text="Save", command=self.add, font=("goudy old style", 15), bg="#2196f3", fg="white", cursor="hand2").place(x=190, y=460, width=110, height=30)
          btn_update = Button(self.root, text="Update",command=self.update, font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2").place(x=310, y=460, width=110, height=30)
          btn_delete = Button(self.root, text="Delete",command=self.delete,font=("goudy old style", 15), bg="#f44336", fg="white", cursor="hand2").place(x=430, y=460, width=110, height=30)
          btn_clear = Button(self.root, text="Clear",command=self.clear, font=("goudy old style", 15), bg="#607d8b", fg="white", cursor="hand2").place(x=550, y=460, width=110, height=30)

          #===Supplier Details
          supplier_frame = Frame(self.root, bd=3, relief=RIDGE)
          supplier_frame.place(x=700, y=160, width=380, height=350)

          scrolly = Scrollbar(supplier_frame, orient=VERTICAL)
          scrollx = Scrollbar(supplier_frame, orient=HORIZONTAL)

          self.supplierTable = ttk.Treeview(supplier_frame, columns=("invoice", "name", "contact", "description"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
          scrollx.pack(side=BOTTOM, fill=X)
          scrolly.pack(side=RIGHT, fill=Y)
          scrollx.config(command=self.supplierTable.xview)
          scrolly.config(command=self.supplierTable.yview)
          
          self.supplierTable.heading("invoice", text="Invoice Number")
          self.supplierTable.heading("name", text="Full name")
          self.supplierTable.heading("contact", text="Contact")
          self.supplierTable.heading("description", text="Description")
          self.supplierTable["show"] = "headings"

          self.supplierTable.column("invoice", width=100)
          self.supplierTable.column("name", width=100)
          self.supplierTable.column("contact", width=100)
          self.supplierTable.column("description", width=100)
          self.supplierTable.pack(fill=BOTH, expand=1)
          self.supplierTable.bind("<ButtonRelease-1>", self.get_data)       

          self.show()

     def add(self):
          con = sqlite3.connect(database=r'pos.db')
          cur = con.cursor()
          try:
               if self.var_sup_invoice.get() == "":
                    messagebox.showerror("Error", "Invoice Number Is Required", parent=self.root)
               else:
                    cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                    row = cur.fetchone()
                    if row is not None:
                         messagebox.showerror("Error", "This Invoice Number is already assigned; try a different one", parent=self.root)
                    else:
                         cur.execute("INSERT INTO supplier (invoice, name, contact, desc) VALUES (?, ?, ?, ?)", (
                              self.var_sup_invoice.get(),
                              self.var_name.get(),
                              self.var_contact.get(),
                              self.txt_desc.get('1.0', END),
                         ))
                         con.commit()
                         messagebox.showinfo("Success", "Supplier Added Successfully", parent=self.root)
                         self.show()
          except Exception as ex:
               messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
          finally:
               con.close()

     def clear(self):
          self.var_sup_invoice.set("")
          self.var_name.set("")
          self.var_contact.set("")
          self.txt_desc.delete('1.0', END)
          self.var_searchtxt.set("")
          self.show()

     #However, this function has to go because I want the supplierloyee details to be privileged
     def show(self):
          con = sqlite3.connect(database=r'pos.db')
          cur = con.cursor()
          try:
               cur.execute("Select * from supplier")
               rows=cur.fetchall()
               if len(rows)>0:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    for row in rows:
                         self.supplierTable.insert('', END, values=row)
          except Exception as ex:
               messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
          finally:
               con.close()

     def get_data(self, ev):
          f=self.supplierTable.focus()
          content=(self.supplierTable.item(f))
          row=content['values']
          self.var_sup_invoice.set(row[0]),
          self.var_name.set(row[1]),
          self.var_contact.set(row[2]),
          self.txt_desc.delete('1.0', END),
          self.txt_desc.insert(END, row[3]),
     
     def update(self):
          con = sqlite3.connect(database=r'pos.db')
          cur = con.cursor()
          try:
               if self.var_sup_invoice.get() == "":
                    messagebox.showerror("Error", "Supplier Number Is Required", parent=self.root)
               else:
                    cur.execute("SELECT * FROM supplier WHERE invoice=?",(self.var_sup_invoice.get(),))
                    row = cur.fetchone()
                    if row == None:
                         messagebox.showerror("Error", "Invalid Invoice Number ID", parent=self.root)
                    else:
                         cur.execute("Update supplier set name=?, contact=?, desc=? where invoice=?", (
                              self.var_name.get(),
                              self.var_contact.get(),
                              self.txt_desc.get('1.0', END),
                              self.var_sup_invoice.get(),
                         ))
                         con.commit()
                         messagebox.showinfo("Success", "Supplier Updated Successfully", parent=self.root)
                         self.show()
          except Exception as ex:
               messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
          finally:
               con.close()

     def delete(self) : 
          con = sqlite3.connect(database=r'pos.db')
          cur= con.cursor()
          try:
               if self.var_sup_invoice.get() == "":
                    messagebox.showerror("Error", "Invoice Number Is Required", parent=self.root)
               else:
                    cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                    row = cur.fetchone()
                    if row == None:
                         messagebox.showerror("Error", "Invalid Invoice Number", parent=self.root)
                    else:
                         op=messagebox.askyesno("Confirm", "Do You Really Want to Delete?", parent=self.root)
                         if op==True:
                              cur.execute("Delete from supplier where invoice=?",(self.var_sup_invoice.get(),))
                              con.commit()
                              messagebox.showinfo("Delete", "Supplier Deleted Successful", parent=self.root)
                              self.clear()
          except Exception as ex:
               messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
          finally:
               con.close()

     def search(self):
          con=sqlite3.connect(database=r'pos.db')
          cur=con.cursor()
          try:
               if self.var_searchtxt.get()=="":
                    messagebox.showerror("Error", "Search Invoice Number is Required", parent=self.root)
               else:
                    cur.execute("select * from supplier where invoice=?",(self.var_searchtxt.get(),))
                    row=cur.fetchone()
                    if row!=None:
                         self.supplierTable.delete(*self.supplierTable.get_children())
                         self.supplierTable.insert('',END, values=row)
                    else:
                         messagebox.showerror("Error", "No Records Found!", parent=self.root)
          except Exception as ex:
               messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
          finally:
               con.close()


if __name__ == "__main__":
    root = Tk()
    obj = supplierClass(root)
    root.mainloop()
