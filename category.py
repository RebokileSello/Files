from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class categoryClass:
     def __init__(self, root):
          self.root = root
          self.root.geometry("1100x550+220+230") # Set to my screen dimensions
          self.root.title("Monate & Sons Scrapyard | Developed By Rebokile Sello")
          self.root.config(bg="white")
          self.root.focus_force()

          #===Variables
          self.var_cat_id=StringVar()
          self.var_name=StringVar()

          #===title
          lbl_title=Label(self.root, text="Manage Product Category", font=("goudy old style", 30), bg="#33bbf9", fg="white", bd=3, relief=RIDGE).pack(side=TOP, fill=X, padx=10, pady=20)

          lbl_name=Label(self.root, text="Enter Product Name", font=("goudy old style", 30), bg="white",).place(x=50, y=100)
          txt_name=Entry(self.root, textvariable=self.var_name, font=("goudy old style", 18), bg="lightyellow",).place(x=50, y=170, width=300)

          btn_add=Button(self.root, text="Add", command=self.add, font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2").place(x=360, y=170, width=150, height=30)
          btn_delete=Button(self.root, text="Delete",command=self.delete, font=("goudy old style", 15), bg="red", fg="white", cursor="hand2").place(x=520, y=170, width=150, height=30)

          #===Catergory Details
          category_frame = Frame(self.root, bd=3, relief=RIDGE)
          category_frame.place(x=700, y=100, width=380, height=100)

          scrolly = Scrollbar(category_frame, orient=VERTICAL)
          scrollx = Scrollbar(category_frame, orient=HORIZONTAL)

          self.categoryTable = ttk.Treeview(category_frame, columns=("cid", "name"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
          scrollx.pack(side=BOTTOM, fill=X)
          scrolly.pack(side=RIGHT, fill=Y)
          scrollx.config(command=self.categoryTable.xview)
          scrolly.config(command=self.categoryTable.yview)
          
          self.categoryTable.heading("cid", text="Category ID")
          self.categoryTable.heading("name", text="Product name")
          self.categoryTable["show"] = "headings"

          self.categoryTable.column("cid", width=100)
          self.categoryTable.column("name", width=100)
          self.categoryTable.pack(fill=BOTH, expand=1)
          self.categoryTable.bind("<ButtonRelease-1>", self.get_data)

          #===Images
          self.im1=Image.open("Avengers 1.jpg")
          self.im1=self.im1.resize((500,300))
          self.im1=ImageTk.PhotoImage(self.im1)
          self.lbl_im1=Label(self.root, image=self.im1, relief=RAISED)
          self.lbl_im1.place(x=50, y=220)

          self.im2=Image.open("Avengers 2.jpg")
          self.im2=self.im2.resize((500,300))
          self.im2=ImageTk.PhotoImage(self.im2)
          self.lbl_im2=Label(self.root, image=self.im2, relief=RAISED)
          self.lbl_im2.place(x=580, y=220)

          self.show()

    #===Functions      

     def add(self):
          con = sqlite3.connect(database=r'pos.db')
          cur = con.cursor()
          try:
               if self.var_name.get() == "":
                    messagebox.showerror("Error", "Category Name Is Required", parent=self.root)
               else:
                    cur.execute("SELECT * FROM category WHERE name=?", (self.var_name.get(),))
                    row = cur.fetchone()
                    if row is not None:
                         messagebox.showerror("Error", "This Category Name is alredy present; try a different one", parent=self.root)
                    else:
                         cur.execute("INSERT INTO category (name) VALUES (?)", (self.var_name.get(),))
                         con.commit()
                         messagebox.showinfo("Success", "Category Added Successfully", parent=self.root)
                         self.show()
          except Exception as ex:
               messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
          finally:
               con.close()

     def show(self):
          con = sqlite3.connect(database=r'pos.db')
          cur = con.cursor()
          try:
               cur.execute("Select * from category")
               rows=cur.fetchall()
               if len(rows)>0:
                    self.categoryTable.delete(*self.categoryTable.get_children())
                    for row in rows:
                         self.categoryTable.insert('', END, values=row)
          except Exception as ex:
               messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
          finally:
               con.close()

     def get_data(self, ev):
          f=self.categoryTable.focus()
          content=(self.categoryTable.item(f))
          row=content['values']
          self.var_cat_id.set(row[0]),
          self.var_name.set(row[1]),


     def delete(self) : 
          con = sqlite3.connect(database=r'pos.db')
          cur= con.cursor()
          try:
               if self.var_name.get() == "":
                    messagebox.showerror("Error", "Category Name Is Required", parent=self.root)
               else:
                    cur.execute("SELECT * FROM category WHERE name=?", (self.var_name.get(),))
                    row = cur.fetchone()
                    if row == None:
                         messagebox.showerror("Error", "Category Name", parent=self.root)
                    else:
                         op=messagebox.askyesno("Confirm", "Do You Really Want to Delete?", parent=self.root)
                         if op==True:
                              cur.execute("Delete from category where name=?",(self.var_name.get(),))
                              con.commit()
                              messagebox.showinfo("Delete", "Category Deleted Successful", parent=self.root)
                              self.show()
                              self.var_cat_id.set("")
                              self.var_name.set("")
          except Exception as ex:
               messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
          finally:
               con.close()

if __name__ == "__main__":
    root = Tk()
    obj = categoryClass(root)
    root.mainloop()
