from tkinter import*
from PIL import Image, ImageTk
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
class IMS:
     def __init__(self,root):
          self.root=root
          self.root.geometry("1350x700+0+0") #set to my screen dimensions
          self.root.title("Inventory Management System | Developed By Rebokile Sello")
          self.root.config(bg="white")
          #===title
          self.icon_image = Image.open("Logo.png")
          self.icon_photo = ImageTk.PhotoImage(self.icon_image)
          title=Label(self.root,text="Inventory Management System",image=self.icon_photo, compound=LEFT, font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20).place(x=0,y=0,relwidth=1, height=70)
          #===Login/out
          btn_logount=Button(self.root, text="Logout", font=("times new roman", 15, "bold"), bg="yellow", cursor="hand2").place(x=1150, y=10, height=50, width=150)
          #===clock
          self.lbl_clock=Label(self.root,text="Welcome to Inventory Management System\t\t Date: DD/MM/YYYY \t\t Time: HH:MM:SS", font=("times new roman", 15), bg="#4d636d", fg="white")
          self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)
          #====Left Menu
          self.MenuLogo=Image.open("Menu.jpeg")
          self.MenuLogo=self.MenuLogo.resize((290,200))
          self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

          LeftMenu=Frame(self.root, bd=2, relief=RIDGE, bg="white")
          LeftMenu.place(x=0, y=102, width=290, height=565)

          lbl_menuLogo=Label(LeftMenu, image=self.MenuLogo)
          lbl_menuLogo.pack(side=TOP, fill=X)
          
          self.icon_side=Image.open("arrow.png")
          self.icon_side=self.icon_side.resize((30,30))
          self.icon_side=ImageTk.PhotoImage(self.icon_side)

          lb_menu=Label(LeftMenu, text="Menu", font=("times new roman", 20), bg="#009688", cursor="hand2").pack(side=TOP, fill=X)
          btn_employee=Button(LeftMenu, text="Employee",command=self.employee, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white",bd=3,  cursor="hand2").pack(side=TOP, fill=X)
          btn_supplier=Button(LeftMenu, text="Supplier",command=self.supplier, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white",bd=3,  cursor="hand2").pack(side=TOP, fill=X)
          btn_category=Button(LeftMenu, text="Category",command=self.category,image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white",bd=3,  cursor="hand2").pack(side=TOP, fill=X)
          btn_product=Button(LeftMenu, text="Product",command=self.product,image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white",bd=3,  cursor="hand2").pack(side=TOP, fill=X)
          btn_sales=Button(LeftMenu, text="Sales",command=self.sales,image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white",bd=3,  cursor="hand2").pack(side=TOP, fill=X)
          btn_exit=Button(LeftMenu, text="Exit",image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white",bd=3,  cursor="hand2").pack(side=TOP, fill=X)
          #====content
          self.lbl_employee=Label(self.root, text="Total Employee\n[ 0 ]",bd=5, relief=RIDGE,  bg="#33bbf9", fg="white", font=("goudy old style", 20, "bold"))
          self.lbl_employee.place(x=300, y=120, height=150, width=300)

          self.lbl_supplier=Label(self.root, text="Total Supplier\n[ 0 ]",bd=5, relief=RIDGE,  bg="#33bbf9", fg="white", font=("goudy old style", 20, "bold"))
          self.lbl_supplier.place(x=650, y=120, height=150, width=300)
          
          self.lbl_category=Label(self.root, text="Total Category\n[ 0 ]",bd=5, relief=RIDGE,  bg="#33bbf9", fg="white", font=("goudy old style", 20, "bold"))
          self.lbl_category.place(x=1000, y=120, height=150, width=300)

          self.lbl_product=Label(self.root, text="Total Products\n[ 0 ]",bd=5, relief=RIDGE,  bg="#33bbf9", fg="white", font=("goudy old style", 20, "bold"))
          self.lbl_product.place(x=300, y=300, height=150, width=300)

          self.lbl_sales=Label(self.root, text="Total Sales\n[ 0 ]",bd=5, relief=RIDGE,  bg="#33bbf9", fg="white", font=("goudy old style", 20, "bold"))
          self.lbl_sales.place(x=650, y=300, height=150, width=300) 


          #===footer
          lbl_footer=Label(self.root,text="Inventory Management System | Developed By Rebokile Sello\nAvailable @ +26657415133 & rebokiles35@gmail.com", font=("times new roman", 12), bg="#4d636d", fg="white").pack(side=BOTTOM, fill=X)


#==============================
     def employee(self):
          self.new_win=Toplevel(self.root)
          self.new_obj=employeeClass(self.new_win)

     def supplier(self):
          self.new_win=Toplevel(self.root)
          self.new_obj=supplierClass(self.new_win)
     
     def category(self):
          self.new_win=Toplevel(self.root)
          self.new_obj=categoryClass(self.new_win)

     def product(self):
          self.new_win=Toplevel(self.root)
          self.new_obj=productClass(self.new_win)

     def sales(self):
          self.new_win=Toplevel(self.root)
          self.new_obj=salesClass(self.new_win)
          
if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()