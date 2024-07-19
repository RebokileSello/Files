from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
class BillClass:
     def __init__(self,root):
          self.root=root
          self.root.geometry("1525x780+0+0") #set to my screen dimensions
          self.root.title("Inventory Management System | Developed By Rebokile Sello")
          self.root.config(bg="white")
          self.cart_list=[]
          self.var_bill_amount=0
          self.var_net_pay=0
          self.var_bill_amount=float(self.var_bill_amount)
          self.var_net_pay=float(self.var_net_pay)
         
          #===title
          self.icon_image = Image.open("Logo.png")
          self.icon_photo = ImageTk.PhotoImage(self.icon_image)
          title=Label(self.root,text="Inventory Management System",image=self.icon_photo, compound=LEFT, font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20).place(x=0,y=0,relwidth=1, height=70)
          #===Login/out
          btn_logount=Button(self.root, text="Logout", font=("times new roman", 15, "bold"), bg="yellow", cursor="hand2").place(x=1330, y=10, height=50, width=150)
          #===clock
          self.lbl_clock=Label(self.root,text="Welcome to Inventory Management System\t\t Date: DD/MM/YYYY \t\t Time: HH:MM:SS", font=("times new roman", 15), bg="#4d636d", fg="white")
          self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

          #===Product Frame
          ProductFrame1=Frame(self.root, bd=4, relief=RIDGE, background="white")
          ProductFrame1.place(x=3, y=100, width=505, height=614)

          pTitle=Label(ProductFrame1, text="All Products", font=("goudy old style", 20, "bold"), bg="#262626", fg="white"). pack(side=TOP, fill=X)

          #===Product Search
          self.var_search=StringVar()
          ProductFrame2=Frame(ProductFrame1, bd=2, relief=RIDGE, background="white")
          ProductFrame2.place(x=2, y=42, width=496, height=90)

          lbl_search=Label(ProductFrame2, text="Search Product | By Name", font=("times new roman", 20, "bold"), background="white",).place(x=2, y=5)

          lbl_product_name=Label(ProductFrame2, text="Product Name:", font=("times new roman", 15), background="white",).place(x=2, y=45)
          txt_search=Entry(ProductFrame2, textvariable=self.var_search, font=("times new roman", 15), background="lightyellow",).place(x=135, y=47, width=180, height=23)
          btn_search=Button(ProductFrame2, text="Search",command=self.search, font=("goudy old style", 15), bg="#2196f3", fg="white", cursor="hand2").place(x=360, y=45, width=120, height=25)
          btn_show_all=Button(ProductFrame2, text="Show All",command=self.show, font=("goudy old style", 15), bg="#083531", fg="white", cursor="hand2").place(x=360, y=10, width=120, height=25)

          #===Product Details
          ProductFrame3 = Frame(ProductFrame1, bd=3, relief=RIDGE)
          ProductFrame3.place(x=1, y=132
          , width=498, height=357)

          scrolly = Scrollbar(ProductFrame3, orient=VERTICAL)
          scrollx = Scrollbar(ProductFrame3, orient=HORIZONTAL)

          self.ProductTable = ttk.Treeview(ProductFrame3, columns=("barcode", "product_name", "sale_price", "car_name", "model", "quantity", "status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
          
          scrollx.pack(side=BOTTOM, fill=X)
          scrolly.pack(side=RIGHT, fill=Y)
          scrollx.config(command=self.ProductTable.xview)
          scrolly.config(command=self.ProductTable.yview)
          self.ProductTable.heading("barcode", text="Barcode")
          self.ProductTable.heading("product_name", text="Product Name")
          self.ProductTable.heading("sale_price", text="Price")
          self.ProductTable.heading("car_name", text="Car Name")
          self.ProductTable.heading("model", text="Model")
          self.ProductTable.heading("quantity", text="Quantity")
          self.ProductTable.heading("status", text="Status")

          self.ProductTable["show"] = "headings"
          self.ProductTable.column("barcode", width=80)
          self.ProductTable.column("product_name", width=120)
          self.ProductTable.column("sale_price", width=70)
          self.ProductTable.column("car_name", width=120)
          self.ProductTable.column("model", width=120)
          self.ProductTable.column("quantity", width=60)
          self.ProductTable.column("status", width=50) 
          self.ProductTable.pack(fill=BOTH, expand=1)
          self.ProductTable.bind("<ButtonRelease-1>", self.get_data)


          #===Customer Frame
          self.var_name=StringVar()
          self.var_contact=StringVar()
          CustomerFrame=Frame(self.root, bd=4, relief=RIDGE, bg="white")
          CustomerFrame.place(x=510, y=100, width=505, height=65)

          cTitle=Label(CustomerFrame, text="Customer Details", font=("goudy old style",13, "bold"), bg="lightgray"). pack(side=TOP, fill=X)
          lbl_customer_name=Label(CustomerFrame, text="Name:", font=("times new roman", 13, "bold"), background="white",).place(x=2, y=30)
          txt_customer_name=Entry(CustomerFrame, textvariable=self.var_name, font=("times new roman", 13), background="lightyellow",).place(x=80, y=32, width=170, height=23)

          lbl_contact=Label(CustomerFrame, text="Contact:", font=("times new roman", 13), background="white",).place(x=260, y=30)
          txt_contact=Entry(CustomerFrame, textvariable=self.var_contact, font=("times new roman", 13), background="lightyellow",).place(x=340, y=32, width=150, height=23)


          #===Calculator and Cart Frame
          Cal_CartFrame=Frame(self.root, bd=2, relief=RIDGE, bg="white")
          Cal_CartFrame.place(x=510, y=165, width=505, height=549)

          lbl_note=Label(Cal_CartFrame, text="Make Quantity 0 to remove product from cart!", font=("goudy old style", 15, "bold"),anchor='w', bg="white", fg="red").pack(side=BOTTOM, fill=X)


          #===Calculator
          self.var_cal_input=StringVar()
          CalFrame=Frame(Cal_CartFrame, bd=2, relief=RIDGE, bg="white")
          CalFrame.place(x=0, y=0, width=290, height=250)

          txt_cal_input=Entry(CalFrame, textvariable=self.var_cal_input, font=("arial", 15, "bold"), width=24, bd=10, relief=GROOVE, state="readonly", justify=RIGHT)
          txt_cal_input.grid(row=0, columnspan=4)

          btn_7=Button(CalFrame,text="7", font=("arial", 15, "bold"),command=lambda:self.get_input(7), bd=2, width=5, pady=5, cursor="hand2").grid(row=1, column=0)
          btn_8=Button(CalFrame,text="8", font=("arial", 15, "bold"),command=lambda:self.get_input(8), bd=2, width=5, pady=5, cursor="hand2").grid(row=1, column=1)
          btn_9=Button(CalFrame,text="9", font=("arial", 15, "bold"),command=lambda:self.get_input(9), bd=2, width=5, pady=5, cursor="hand2").grid(row=1, column=2)
          btn_sum=Button(CalFrame,text="+", font=("arial", 15, "bold"),command=lambda:self.get_input("+"), bd=2, width=5, pady=5, cursor="hand2").grid(row=1, column=3)

          btn_4=Button(CalFrame,text="4", font=("arial", 15, "bold"),command=lambda:self.get_input(4), bd=2, width=5, pady=5, cursor="hand2").grid(row=2, column=0)
          btn_5=Button(CalFrame,text="5", font=("arial", 15, "bold"),command=lambda:self.get_input(5), bd=2, width=5, pady=5, cursor="hand2").grid(row=2, column=1)
          btn_6=Button(CalFrame,text="6", font=("arial", 15, "bold"),command=lambda:self.get_input(6), bd=2, width=5, pady=5, cursor="hand2").grid(row=2, column=2)
          btn_subtract=Button(CalFrame,text="-", font=("arial", 15, "bold"),command=lambda:self.get_input("-"), bd=2, width=5, pady=5, cursor="hand2").grid(row=2, column=3)

          btn_1=Button(CalFrame,text="1", font=("arial", 15, "bold"),command=lambda:self.get_input(1), bd=2, width=5, pady=5, cursor="hand2").grid(row=3, column=0)
          btn_2=Button(CalFrame,text="2", font=("arial", 15, "bold"),command=lambda:self.get_input(2), bd=2, width=5, pady=5, cursor="hand2").grid(row=3, column=1)
          btn_3=Button(CalFrame,text="3", font=("arial", 15, "bold"),command=lambda:self.get_input(3), bd=2, width=5, pady=5, cursor="hand2").grid(row=3, column=2)
          btn_multiply=Button(CalFrame,text="*", font=("arial", 15, "bold"),command=lambda:self.get_input("*"), bd=2, width=5, pady=5, cursor="hand2").grid(row=3, column=3)

          btn_0=Button(CalFrame,text="0", font=("arial", 15, "bold"),command=lambda:self.get_input(0), bd=2, width=5, pady=5, cursor="hand2").grid(row=4, column=0)
          btn_clear=Button(CalFrame,text="C", font=("arial", 15, "bold"), command=self.clear_cal, bd=2, width=5, pady=5, cursor="hand2").grid(row=4, column=1)
          btn_divide=Button(CalFrame,text="/", font=("arial", 15, "bold"),command=lambda:self.get_input("/"), bd=2, width=5, pady=5, cursor="hand2").grid(row=4, column=2)
          btn_equal=Button(CalFrame,text="=", font=("arial", 15, "bold"),command=self.perform_cal, bd=2, width=5, pady=5, cursor="hand2").grid(row=4, column=3)

          #===Cart
          CartFrame = Frame(Cal_CartFrame, bd=2, relief=RIDGE)
          CartFrame.place(x=0, y=251, width=500, height=265)
          self.cartTitle=Label(CartFrame, text="Cart \t Total Products: [0]", font=("goudy old style",15), bg="lightgray")
          self.cartTitle.pack(side=TOP, fill=X)

          scrolly = Scrollbar(CartFrame, orient=VERTICAL)
          scrollx = Scrollbar(CartFrame, orient=HORIZONTAL)

          self.CartTable = ttk.Treeview(CartFrame, columns=("barcode", "product_name", "sale_price", "car_name", "model", "quantity", "status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
          
          scrollx.pack(side=BOTTOM, fill=X)
          scrolly.pack(side=RIGHT, fill=Y)
          scrollx.config(command=self.CartTable.xview)
          scrolly.config(command=self.CartTable.yview)
          self.CartTable.heading("barcode", text="Barcode")
          self.CartTable.heading("product_name", text="Product Name")
          self.CartTable.heading("sale_price", text="Price")
          self.CartTable.heading("car_name", text="Car Name")
          self.CartTable.heading("model", text="Model")
          self.CartTable.heading("quantity", text="Quantity")
          self.CartTable.heading("status", text="Status")

          self.CartTable["show"] = "headings"
          self.CartTable.column("barcode", width=80)
          self.CartTable.column("product_name", width=120)
          self.CartTable.column("sale_price", width=60)
          self.CartTable.column("car_name", width=110)
          self.CartTable.column("model", width=100)
          self.CartTable.column("quantity", width=60) 
          self.CartTable.column("status", width=50)
          self.CartTable.pack(fill=BOTH, expand=1)
          #self.CartTable.bind("<ButtonRelease-1>", self.get_data)


          #===Cart Buttons
          self.var_barcode=StringVar()
          self.var_product_name=StringVar()
          self.var_car_name=StringVar()
          self.var_model=StringVar()
          self.var_sale_price=StringVar()
          self.var_quantity=StringVar()
          self.var_stock=StringVar()
          self.var_status=StringVar()
          Add_CartWidgetsFrame=Frame(ProductFrame1, bd=2, relief=RIDGE, bg="white")
          Add_CartWidgetsFrame.place(x=1, y=490, width=497, height=116)

          lbl_p_name=Label(Add_CartWidgetsFrame, text="Product Name", font=("times new roman", 12), bg="white").place(x=2,y=2)
          txt_p_name=Entry(Add_CartWidgetsFrame, textvariable=self.var_product_name, font=("times new roman", 12), background="lightyellow", state="readonly").place(x=2,y=25, width=150, height=20)

          lbl_c_name=Label(Add_CartWidgetsFrame, text="Car Name", font=("times new roman", 12), bg="white").place(x=157,y=2)
          txt_c_name=Entry(Add_CartWidgetsFrame, textvariable=self.var_car_name, font=("times new roman", 12), background="lightyellow", state="readonly").place(x=160,y=25, width=150, height=20)

          lbl_quantity=Label(Add_CartWidgetsFrame, text="Quantity", font=("times new roman", 12), bg="white").place(x=320,y=2)
          txt_quantity=Entry(Add_CartWidgetsFrame, textvariable=self.var_quantity, font=("times new roman", 12), background="lightyellow").place(x=320,y=25, width=70, height=20)

          lbl_model=Label(Add_CartWidgetsFrame, text="Model", font=("times new roman", 12), bg="white").place(x=2,y=45)
          txt_model=Entry(Add_CartWidgetsFrame, textvariable=self.var_model, font=("times new roman", 12), background="lightyellow", state="readonly").place(x=2,y=68, width=150, height=20)

          lbl_price=Label(Add_CartWidgetsFrame, text="Unit Price", font=("times new roman", 12), bg="white").place(x=157,y=45)
          txt_Price=Entry(Add_CartWidgetsFrame, textvariable=self.var_sale_price, font=("times new roman", 12), background="lightyellow", state="readonly").place(x=160,y=68, width=150, height=20)

          lbl_available_quantity=Label(Add_CartWidgetsFrame, text="Available", font=("times new roman", 12), bg="white").place(x=320,y=45)
          txt_available_quantity=Entry(Add_CartWidgetsFrame, textvariable=self.var_stock, font=("times new roman", 12), background="lightyellow", state="readonly").place(x=320,y=68, width=70, height=20)

          btn_add_to_cart=Button(Add_CartWidgetsFrame, text="Add", command=self.addto_update_cart, font=("times new roman", 13), bg="#75c9ef", cursor="hand2").place(x=400, y=20, width=80,height=25)
          btn_update_cart=Button(Add_CartWidgetsFrame, text="Update", command=self.addto_update_cart, font=("times new roman", 13), bg="#b7cedc", cursor="hand2").place(x=400, y=50, width=80,height=25)
          btn_clear_cart=Button(Add_CartWidgetsFrame, text="Clear", font=("times new roman", 13), bg="lightgray", cursor="hand2").place(x=400, y=80, width=80,height=25)


     #===Billing Area
          billFrame=Frame(self.root, bd=2, relief=RIDGE, bg="white")
          billFrame.place(x=1017, y=100, width=505, height=500)

          BTitle=Label(billFrame, text="Customer Bill Area", font=("goudy old style", 20, "bold"), bg="#1D56C2", fg="white"). pack(side=TOP, fill=X)
          scrolly=Scrollbar(billFrame, orient=VERTICAL)
          scrolly.pack(side=RIGHT, fill=Y)

          self.txt_bill_area=Text(billFrame, yscrollcommand=scrolly.set)
          self.txt_bill_area.pack(fill=BOTH, expand=1)
          scrolly.config(command=self.txt_bill_area.yview)


     #===Billing Buttons
          billMenuFrame=Frame(self.root, bd=2, relief=RIDGE, bg="white")
          billMenuFrame.place(x=1017, y=600, width=505, height=114)

          self.lbl_amount=Label(billMenuFrame, text="Gross. M\n[0]", font=("goudy old style", 15, "bold"), bg="#3f51b5", fg="white")
          self.lbl_amount.place(x=2, y=2, width=120, height=50)

          btn_discount=Button(billMenuFrame, text="Discount\n[5%]", command=self.discount, font=("goudy old style", 15, "bold"), bg="#8bc34a", fg="white", cursor="hand2")
          btn_discount.place(x=123, y=2, width=120, height=50)

          self.lbl_net_pay=Label(billMenuFrame, text="Total. M\n[0]", font=("goudy old style", 15, "bold"), bg="#607d8b", fg="white")
          self.lbl_net_pay.place(x=244, y=2, width=120, height=50)

          btn_print=Button(billMenuFrame, text="Print", font=("goudy old style", 15, "bold"), bg="lightgreen", fg="white", cursor="hand2")
          btn_print.place(x=2, y=53, width=120, height=57)

          btn_clear_all=Button(billMenuFrame, text="Clear All", font=("goudy old style", 15, "bold"), bg="gray", fg="white", cursor="hand2")
          btn_clear_all.place(x=123, y=53, width=120, height=57)

          btn_generate=Button(billMenuFrame, text="Generate & \nSave Bill", font=("goudy old style", 15, "bold"), bg="#009688", fg="white", cursor="hand2")
          btn_generate.place(x=244, y=53, width=120, height=57)

           #===footer
          lbl_footer=Label(self.root,text="Inventory Management System | Developed By Rebokile Sello\nAvailable @ +26657415133 & rebokiles35@gmail.com", font=("times new roman", 12), bg="#4d636d", fg="white").pack(side=BOTTOM, fill=X)

          self.show()
     



     #===All Functions
     def get_input(self, num):
          xnum=self.var_cal_input.get()+str(num)
          self.var_cal_input.set(xnum)

     def clear_cal(self):
          self.var_cal_input.set("")

     def perform_cal(self):
          result=self.var_cal_input.get()
          self.var_cal_input.set(eval(result))

     def show(self):
          con = sqlite3.connect(database=r'pos.db')
          cur = con.cursor()
          try:
               cur.execute("Select barcode, product_name, sale_price, car_name, model, quantity, status from product where status='Active'")
               rows=cur.fetchall()
               if len(rows)>0:
                    self.ProductTable.delete(*self.ProductTable.get_children())
                    for row in rows:
                         self.ProductTable.insert('', END, values=row)
          except Exception as ex:
               messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
          finally:
               con.close()

     def search(self):
          con=sqlite3.connect(database=r'pos.db')
          cur=con.cursor()
          try:
               if self.var_search.get()=="":
                    messagebox.showerror("Error", "Search Value is Required", parent=self.root)
               else:
                    cur.execute("select barcode, product_name, sale_price, car_name, model, quantity, status from product where product_name LIKE '%"+self.var_search.get()+"%'")
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

     def get_data(self, ev):
          f=self.ProductTable.focus()
          content=(self.ProductTable.item(f))
          row=content['values']
          self.var_barcode.set(row[0])
          self.var_product_name.set(row[1])
          self.var_sale_price.set(row[2])
          self.var_car_name.set(row[3])
          self.var_model.set(row[4])
          self.var_stock.set(row[5])
          self.var_status.set(row[6])

     def addto_update_cart(self):
          if self.var_barcode.get()=='':
               messagebox.showerror("Error", "Please Select A Product from the list", parent=self.root)
          elif self.var_quantity.get()=='':
               messagebox.showerror("Error", "A Quantity is Required", parent=self.root)
          else:
               price_cal=int(self.var_quantity.get())*float(self.var_sale_price.get())
               price_cal=float(price_cal)
               cart_data=[self.var_barcode.get(), self.var_product_name.get(), price_cal, self.var_car_name.get(), self.var_model.get(), self.var_quantity.get(), self.var_status.get()]
               #===Update Cart
               present="no"
               index_=0
               for row in self.cart_list:
                    if self.var_barcode.get()==row[0]:
                         present="yes"
                         break
                    index_+=1
               if present=="yes":
                    op=messagebox.askyesno("Confirm", "Product Already Present.\nDo you want to Update or Remove it?", parent=self.root)
                    if op==True:
                         if self.var_quantity.get()=="0":
                              self.cart_list.pop(index_)
                         else:
                              oldq=int(self.cart_list[index_][5])
                              oldp=int(self.cart_list[index_][2])
                              self.cart_list[index_][2]=oldp+price_cal
                              self.cart_list[index_][5]=oldq+int(self.var_quantity.get())
               else:
                    self.cart_list.append(cart_data)

               self.show_cart()
               self.bill_update()

     def bill_update(self):
          
          bill_amount=0
          
          net_pay=0
          for row in self.cart_list:
               bill_amount=bill_amount+float(row[2])
               self.var_bill_amount=bill_amount
          
          net_pay=bill_amount
          self.var_net_pay=net_pay

          self.lbl_amount.config(text=f"Gross. M\n{str(self.var_bill_amount)}")
          self.lbl_net_pay.config(text=f"Total. M\n{str(self.var_net_pay)}")
          self.cartTitle.config(text=f"Cart \t Total Products: {str(len(self.cart_list))}")

     def discount(self):
          self.var_net_pay=self.var_net_pay-(self.var_bill_amount*0.05)
          self.lbl_net_pay.config(text=f"Total. M\n{str(self.var_net_pay)}")


     def show_cart(self):
          try:
               self.CartTable.delete(*self.CartTable.get_children())
               for row in self.cart_list:
                    self.CartTable.insert("", END, values=row)
          except Exception as ex:
               messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj=BillClass(root)
    root.mainloop()