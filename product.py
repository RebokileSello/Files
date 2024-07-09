from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import random

class productClass:
     def __init__(self, root):
          self.root = root
          self.root.geometry("1100x600+220+150") # Set to my screen dimensions
          self.root.title("Monate & Sons Scrapyard | Developed By Rebokile Sello")
          self.root.config(bg="white")
          self.root.focus_force()
          #===
          #===Variables
          self.var_category=StringVar()
          self.var_supplier=StringVar()
          self.cat_list=[]
          self.sup_list=[]
          self.fetch_category_and_supplier()
          self.var_car_name=StringVar()
          self.var_model=StringVar()
          self.var_vin_number=StringVar()
          self.var_product_name=StringVar()
          self.var_cost_price=StringVar()
          self.var_sale_price=StringVar()
          self.var_quantity=StringVar()
          self.var_status=StringVar()
          #self.var_barcode=StringVar()
          self.var_searchby = StringVar()
          self.var_searchtxt = StringVar()

          product_Frame=Frame(self.root, bd=3, relief=RIDGE, bg="white")
          product_Frame.place(x=10, y=15, width=450, height=540)

          #===Title
          title = Label(product_Frame, text="Manage Product Details", font=("goudy old style", 20), bg="#0f4d7d", fg="white").pack(side=TOP, fill=X)

          #===column1
          lbl_category = Label(product_Frame, text="Category", font=("goudy old style", 18), bg="white").place(x=30, y=50)
          lbl_supplier = Label(product_Frame, text="Supplier", font=("goudy old style", 18), bg="white").place(x=30, y=90)
          lbl_car_name_ = Label(product_Frame, text="Car Name", font=("goudy old style", 18), bg="white").place(x=30, y=130)
          lbl_model = Label(product_Frame, text="Model", font=("goudy old style", 18), bg="white").place(x=30, y=170)
          lbl_vin_number = Label(product_Frame, text="Vin Number", font=("goudy old style", 18), bg="white").place(x=30, y=210) 
          lbl_product_name = Label(product_Frame, text="Product Name", font=("goudy old style", 18), bg="white").place(x=30, y=250)
          lbl_cost_price = Label(product_Frame, text=" Cost Price", font=("goudy old style", 18), bg="white").place(x=30, y=290)
          lbl_sale_price = Label(product_Frame, text=" Sale Price", font=("goudy old style", 18), bg="white").place(x=30, y=330)
          lbl_quantity = Label(product_Frame, text="Quantity", font=("goudy old style", 18), bg="white").place(x=30, y=370)
          lbl_status = Label(product_Frame, text="Status", font=("goudy old style", 18), bg="white").place(x=30, y=410)

          #===column2
          cmb_category = ttk.Combobox(product_Frame, textvariable=self.var_category, values=self.cat_list, state="readonly", justify=CENTER, font=("goudy old style", 15))
          cmb_category.place(x=200, y=50, width=200)
          cmb_category.current(0)

          cmb_supplier = ttk.Combobox(product_Frame, textvariable=self.var_supplier, values=self.sup_list, state="readonly", justify=CENTER, font=("goudy old style", 15))
          cmb_supplier.place(x=200, y=90, width=200)
          cmb_supplier.current(0)

          txt_car_name = Entry(product_Frame, textvariable=self.var_car_name, font=("goudy old style", 15), bg="lightyellow").place(x=200, y=130, width=200)
          txt_model = Entry(product_Frame, textvariable=self.var_model, font=("goudy old style", 15), bg="lightyellow").place(x=200, y=170, width=200)
          txt_vin_number = Entry(product_Frame, textvariable=self.var_vin_number, font=("goudy old style", 15), bg="lightyellow").place(x=200, y=210, width=200)
          txt_product_name = Entry(product_Frame, textvariable=self.var_product_name, font=("goudy old style", 15), bg="lightyellow").place(x=200, y=250, width=200)
          txt_cost_price = Entry(product_Frame, textvariable=self.var_cost_price, font=("goudy old style", 15), bg="lightyellow").place(x=200, y=290, width=200)
          txt_sale_price = Entry(product_Frame, textvariable=self.var_sale_price, font=("goudy old style", 15), bg="lightyellow").place(x=200, y=330, width=200)
          txt_quantity = Entry(product_Frame, textvariable=self.var_quantity, font=("goudy old style", 15), bg="lightyellow").place(x=200, y=370, width=200)
          cmb_status = ttk.Combobox(product_Frame, textvariable=self.var_status, values=("Select","Active", "Inactive"), state="readonly", justify=CENTER, font=("goudy old style", 15))
          cmb_status.place(x=200, y=410, width=200)
          cmb_status.current(0)

          #===Buttons
          btn_add = Button(product_Frame, text="Save",command=self.add, font=("goudy old style", 15), bg="#2196f3", fg="white", cursor="hand2").place(x=10, y=450, width=70, height=30)
          btn_update = Button(product_Frame, text="Update",command=self.update, font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2").place(x=90, y=450, width=70, height=30)
          btn_delete = Button(product_Frame, text="Delete",command=self.delete,font=("goudy old style", 15), bg="#f44336", fg="white", cursor="hand2").place(x=170, y=450, width=70, height=30)
          btn_clear = Button(product_Frame, text="Clear",command=self.clear, font=("goudy old style", 15), bg="#607d8b", fg="white", cursor="hand2").place(x=250, y=450, width=70, height=30)
          btn_show = Button(product_Frame, text="Show",command=self.show, font=("goudy old style", 15), bg="#4E47C6", fg="white", cursor="hand2").place(x=330, y=450, width=80, height=30)

           #===Search Frame
          SearchFrame = LabelFrame(self.root, text="Search Product", font=("goudy old style", 18, "bold"), bd=2, relief=RIDGE, bg="white")
          SearchFrame.place(x=480, y=10, width=600, height=80)

          #===Options
          cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, value=("Select", "Category", "Supplier", "Care Name", "Car Model", "Product Name"), state="readonly", justify=CENTER, font=("goudy old style", 15))
          cmb_search.place(x=10, y=10, width=180, height=30)
          cmb_search.current(0)

          txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("goudy old style", 15), bg="lightyellow").place(x=200, y=10, width=220, height=30)
          btn_search = Button(SearchFrame, text="Search",command=self.search, font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2").place(x=430, y=9, width=150, height=30)

          #===Product Details
          prod_frame = Frame(self.root, bd=3, relief=RIDGE)
          prod_frame.place(x=480, y=100, width=600,height=455)
          scrolly = Scrollbar(prod_frame, orient=VERTICAL)
          scrollx = Scrollbar(prod_frame, orient=HORIZONTAL)
          self.ProductTable = ttk.Treeview(prod_frame, columns=("barcode", "category", "supplier", "car_name", "model", "vin_number", "product_name", "cost_price", "sale_price", "quantity", "status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
          scrollx.pack(side=BOTTOM, fill=X)
          scrolly.pack(side=RIGHT, fill=Y)
          scrollx.config(command=self.ProductTable.xview)
          scrolly.config(command=self.ProductTable.yview)
          self.ProductTable.heading("barcode", text="Barcode")
          self.ProductTable.heading("category", text="Category")
          self.ProductTable.heading("supplier", text="Supplier")
          self.ProductTable.heading("car_name", text="Car Name")
          self.ProductTable.heading("model", text="Model")
          self.ProductTable.heading("vin_number", text="Vin Number")
          self.ProductTable.heading("product_name", text="Product Name")
          self.ProductTable.heading("cost_price", text="Cost Price")
          self.ProductTable.heading("sale_price", text="Sale Price")
          self.ProductTable.heading("quantity", text="Quantity")
          self.ProductTable.heading("status", text="Status")
          self.ProductTable["show"] = "headings"
          self.ProductTable.column("barcode", width=100)
          self.ProductTable.column("category", width=100)
          self.ProductTable.column("supplier", width=100)
          self.ProductTable.column("car_name", width=100)
          self.ProductTable.column("model", width=100)
          self.ProductTable.column("vin_number", width=100)
          self.ProductTable.column("product_name", width=100)
          self.ProductTable.column("cost_price", width=100)
          self.ProductTable.column("sale_price", width=100)
          self.ProductTable.column("quantity", width=100)
          self.ProductTable.column("status", width=100)  
          self.ProductTable.bind("<ButtonRelease-1>", self.get_data)
          self.ProductTable.pack(fill=BOTH, expand=1)
          self.show()

     def generate_barcode(self):
          return ''.join([str(random.randint(0,9)) for _ in range(10)])
          #What we want to do here is call this function self.  

     def fetch_category_and_supplier(self):
          self.cat_list.append("Empty")
          self.sup_list.append("Empty")
          con = sqlite3.connect(database=r'pos.db')
          cur = con.cursor()
          try:
               cur.execute("Select name from category")
               cat = cur.fetchall()
               if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])
               cur.execute("Select name from supplier")
               sup = cur.fetchall()
               if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])
          except Exception as ex:
               messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
          finally:
               con.close()

     def add(self):
        con = sqlite3.connect(database=r'pos.db')
        cur = con.cursor()
        barcode = self.generate_barcode()
        try:
         if self.var_category.get() == "Select" or self.var_category.get() == "Empty" or self.var_supplier.get() == "Empty" or self.var_supplier.get() == "Select" or self.var_product_name.get() == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
         else:
            cur.execute("SELECT * FROM product WHERE vin_number=? AND product_name=?", (self.var_vin_number.get(), self.var_product_name.get()))
            row = cur.fetchone()
            if row is not None:
                messagebox.showerror("Error", "This product already exists! Search and Update.", parent=self.root)
            else:
                cur.execute(
                "INSERT INTO product (barcode, category, supplier, car_name, model, vin_number, product_name, cost_price, sale_price, quantity, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                barcode,
                self.var_category.get(),
                self.var_supplier.get(),
                self.var_car_name.get(),
                self.var_model.get(),
                self.var_vin_number.get(),
                self.var_product_name.get(),
                self.var_cost_price.get(),
                self.var_sale_price.get(),
                self.var_quantity.get(),
                self.var_status.get(),
                )
                )
                con.commit()
                messagebox.showinfo("Success", "Product Added Successfully", parent=self.root)
                self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Unexpected Error: {str(ex)}", parent=self.root)
        finally:
            con.close()

     def clear(self):
          self.var_category.set("Select")
          self.var_supplier.set("Select")
          self.var_car_name.set("")
          self.var_model.set("")
          self.var_vin_number.set("")
          self.var_product_name.set("")
          self.var_cost_price.set("")
          self.var_sale_price.set("")
          self.var_quantity.set("")
          self.var_status.set("Select")
          self.var_searchtxt.set("")
          self.var_searchby.set("Select")

     def show(self):
          con = sqlite3.connect(database=r'pos.db')
          cur = con.cursor()
          try:
               cur.execute("Select * from product")
               rows=cur.fetchall()
               if len(rows)>0:
                    self.ProductTable.delete(*self.ProductTable.get_children())
                    for row in rows:
                         self.ProductTable.insert('', END, values=row)
          except Exception as ex:
               messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
          finally:
               con.close()

     def get_data(self, ev):
          f=self.ProductTable.focus()
          content=(self.ProductTable.item(f))
          row=content['values']
          self.var_category.set(row[1]),
          self.var_supplier.set(row[2]),
          self.var_car_name.set(row[3]),
          self.var_model.set(row[4]),
          self.var_vin_number.set(row[5]),
          self.var_product_name.set(row[6]),
          self.var_cost_price.set(row[7]),
          self.var_sale_price.set(row[8]),
          self.var_quantity.set(row[9]),
          self.var_status.set(row[10]),
               
     def update(self):
        con = sqlite3.connect(database=r'pos.db')
        cur = con.cursor()
        try:
            if self.var_product_name.get() == "":
                messagebox.showerror("Error", "Please Select a Product from the list!", parent=self.root)
            else:
                 cur.execute("SELECT barcode FROM product WHERE product_name=? AND car_name=? AND model=?", 
                    (self.var_product_name.get(), self.var_car_name.get(), self.var_model.get()))
                 barcode = cur.fetchone()
                 if barcode is None:
                     messagebox.showerror("Error", "Invalid Product", parent=self.root)
                 else:
                    cur.execute("""
                    UPDATE product 
                    SET category=?, supplier=?, car_name=?, model=?, vin_number=?, product_name=?, 
                    cost_price=?, sale_price=?, quantity=?, status=? 
                     WHERE barcode=?""",
                    (
                     self.var_category.get(),
                     self.var_supplier.get(),
                     self.var_car_name.get(),
                     self.var_model.get(),
                     self.var_vin_number.get(),
                     self.var_product_name.get(),
                     self.var_cost_price.get(),
                     self.var_sale_price.get(),
                     self.var_quantity.get(),
                     self.var_status.get(),
                     barcode[0], 
                    )
                     )
                    con.commit()
                    messagebox.showinfo("Success", "Product Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
             messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

     def delete(self) : 
          con = sqlite3.connect(database=r'pos.db')
          cur= con.cursor()
          try:
               if self.var_product_name.get() == "":
                 messagebox.showerror("Error", "Please Select a Product from the list!", parent=self.root)
               else:
                    cur.execute("Select * from product where vin_number=? AND product_name=?", (self.var_vin_number.get(), self.var_product_name.get()))
                    row = cur.fetchone()
                    if row == None:
                         messagebox.showerror("Error", "This Product Does not Exist", parent=self.root)
                    else:
                         op=messagebox.askyesno("Confirm", "Do You Really Want to Delete?", parent=self.root)
                         if op==True:
                              cur.execute("Delete from product WHERE product_name=? AND car_name=? AND model=?", 
                              (self.var_product_name.get(), self.var_car_name.get(), self.var_model.get()))
                              con.commit()
                              messagebox.showinfo("Delete", "Product Deleted Successfully", parent=self.root)
                              self.show()
          except Exception as ex:
               messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
          finally:
               con.close()
     def search(self):
          con=sqlite3.connect(database=r'pos.db')
          cur=con.cursor()
          try:
               if self.var_searchby.get()=="Select":
                    messagebox.showerror("Error", "Select Search Key", parent=self.root)
               elif self.var_searchtxt.get()=="":
                    messagebox.showerror("Error", "Search Value is Required", parent=self.root)
               else:
                    cur.execute("select * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                    rows=cur.fetchall()
                    if len(rows)!=0:
                         self.ProductTable.delete(*self.ProductTable.get_children())
                         for row in rows:
                              self.ProductTable.insert('',END, values=row)
                    else:
                         messagebox.showerror("Error", "No Records Found!", parent=self.root)
          except Exception as ex:
               messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
          finally:
               con.close()
          
if __name__ == "__main__":
    root = Tk()
    obj = productClass(root)
    root.mainloop()
