import sqlite3
def create_db():
    con=sqlite3.connect(database=r'pos.db')
    cur=con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS employee(empID INTEGER PRIMARY KEY AUTOINCREMENT, name text, email text, gender text, contact text, dob text, doj text, password text, utype text, address text, salary text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT, name text, contact text, desc text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT, name text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS product(barcode INTEGER PRIMARY KEY, category text, supplier text, car_name text, model text, vin_number text, product_name text, cost_price text, sale_price text, quantity text, status text)")
    con.commit()
    

create_db()