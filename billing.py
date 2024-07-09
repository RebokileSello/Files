from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
class BillClass:
     def __init__(self,root):
          self.root=root
          self.root.geometry("1525x780+0+0") #set to my screen dimensions
          self.root.title("Monate & Sons Scrapyard | Developed By Rebokile Sello")
          self.root.config(bg="white")
          #===title
          self.icon_image = Image.open("Logo.png")
          self.icon_photo = ImageTk.PhotoImage(self.icon_image)
          title=Label(self.root,text="Monate & Sons Scrapyard",image=self.icon_photo, compound=LEFT, font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20).place(x=0,y=0,relwidth=1, height=70)
          #===Login/out
          btn_logount=Button(self.root, text="Logout", font=("times new roman", 15, "bold"), bg="yellow", cursor="hand2").place(x=1330, y=10, height=50, width=150)
          #===clock
          self.lbl_clock=Label(self.root,text="Welcome to Monate & Sons Scrapyard\t\t Date: DD/MM/YYYY \t\t Time: HH:MM:SS", font=("times new roman", 15), bg="#4d636d", fg="white")
          self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

          #===Product Frame
          self.var_search=StringVar()
          ProductFrame1=Frame(self.root, bd=4, relief=RIDGE, background="white")
          ProductFrame1.place(x=3, y=100, width=505, height=670)

          pTitle=Label(ProductFrame1, text="All Products", font=("goudy old style", 20, "bold"), bg="#262626", fg="white"). pack(side=TOP, fill=X)

          #===Product Search
          ProductFrame2=Frame(ProductFrame1, bd=2, relief=RIDGE, background="white")
          ProductFrame2.place(x=2, y=42, width=498, height=90)

          lbl_search=Label(ProductFrame2, text="Search Product | By Name", font=("times new roman", 20, "bold"), background="white",).place(x=2, y=5)

          lbl_product_name=Label(ProductFrame2, text="Product Name:", font=("times new roman", 15), background="white",).place(x=2, y=45)
          txt_search=Entry(ProductFrame2, textvariable=self.var_search, font=("times new roman", 15), background="lightyellow",).place(x=135, y=47, width=180, height=23)
          btn_search=Button(ProductFrame2, text="Search", font=("goudy old style", 15), bg="#2196f3", fg="white", cursor="hand2").place(x=360, y=45, width=120, height=25)
          btn_show_all=Button(ProductFrame2, text="Show All", font=("goudy old style", 15), bg="#083531", fg="white", cursor="hand2").place(x=360, y=10, width=120, height=25)

          #===Product Details
          ProductFrame3 = Frame(ProductFrame1, bd=3, relief=RIDGE)
          ProductFrame3.place(x=1, y=132
          , width=498, height=480)

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
          self.ProductTable.column("product_name", width=100)
          self.ProductTable.column("sale_price", width=60)
          self.ProductTable.column("car_name", width=80)
          self.ProductTable.column("model", width=80)
          self.ProductTable.column("quantity", width=50)
          self.ProductTable.column("status", width=50) 
          #self.ProductTable.bind("<ButtonRelease-1>", self.get_data)
          self.ProductTable.pack(fill=BOTH, expand=1)

          lbl_note=Label(ProductFrame1, text="Make Quantity 0 to remove product from cart!", font=("goudy old style", 15, "bold"),anchor='w', bg="white", fg="red").pack(side=BOTTOM, fill=X)


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
          Cal_CartFrame.place(x=510, y=165, width=505, height=485)


          #===Calculator
          self.var_cal_input=StringVar()
          CalFrame=Frame(Cal_CartFrame, bd=2, relief=RIDGE, bg="white")
          CalFrame.place(x=0, y=0, width=500, height=235)

          self.txt_cal_input=Entry(CalFrame, textvariable=self.var_cal_input, font=("arial", 15, "bold"), width=21, bd=10, relief=GROOVE)
          self.txt_cal_input.grid(row=0, columnspan=4)

          #===Cart
          CartFrame = Frame(Cal_CartFrame, bd=2, relief=RIDGE)
          CartFrame.place(x=0, y=236
          , width=500, height=245)
          cartTitle=Label(CartFrame, text="Cart \t Total Products: [0]", font=("goudy old style",15), bg="lightgray"). pack(side=TOP, fill=X)

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
          self.CartTable.column("product_name", width=100)
          self.CartTable.column("sale_price", width=60)
          self.CartTable.column("car_name", width=80)
          self.CartTable.column("model", width=80)
          self.CartTable.column("quantity", width=50)
          self.CartTable.column("status", width=50) 
          #self.CartTable.bind("<ButtonRelease-1>", self.get_data)
          self.CartTable.pack(fill=BOTH, expand=1)


          #===Cart Buttons
          self.var_barcode=StringVar()
          self.var_product_name=StringVar()
          self.var_car_name=StringVar()
          self.var_model=StringVar()
          self.var_sale_price=StringVar()
          self.var_quantity=StringVar()
          self.var_stock=StringVar()
          Add_CartWidgetsFrame=Frame(self.root, bd=2, relief=RIDGE, bg="white")
          Add_CartWidgetsFrame.place(x=510, y=650, width=505, height=120)

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

          btn_add_to_cart=Button(Add_CartWidgetsFrame, text="Add", font=("times new roman", 13), bg="#75c9ef", cursor="hand2").place(x=400, y=20, width=80,height=25)
          btn_update_cart=Button(Add_CartWidgetsFrame, text="Update", font=("times new roman", 13), bg="#b7cedc", cursor="hand2").place(x=400, y=50, width=80,height=25)
          btn_clear_cart=Button(Add_CartWidgetsFrame, text="Clear", font=("times new roman", 13), bg="lightgray", cursor="hand2").place(x=400, y=80, width=80,height=25)


if __name__=="__main__":
    root=Tk()
    obj=BillClass(root)
    root.mainloop()