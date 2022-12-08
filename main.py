from flask import *
import sqlite3 
import hashlib 


app = Flask(__name__)


def hash_string(string):
    """Will hash input string and return it"""
    return hashlib.sha256(string.encode()).hexdigest()


def compare(item_1, item_2):
    """Compares two items and returns True or False depending on if they match"""
    if item_1 == item_2:
        return True
    return False


@app.route('/')
def main_page():
    """Renders the main template."""
    return render_template("index.html")


@app.route("/settings")
def render_settings():
    """Renders settings template"""
    return render_template("Settings.html")


@app.route("/login")
def render_login():
    """Renders login template"""
    return render_template("login.html")


@app.route("/account")
def render_account():
    return render_template("account.html")

def create_tables():
    """This function will exicute SQL queries to create the required tables."""
    conn = sqlite3.connect("databases/data.db")#Connection to DB is made
    c = conn.cursor()

    #Users table is created
    c.execute("""
    CREATE TABLE Users(
        User_ID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        Username VARCHAR(20) UNIQUE,
        Password VARCHAR(20))""")

    #User_Orders table is created
    c.execute("""
    CREATE TABLE User_Orders(
        Order_ID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        User_ID INTEGER,
        Arrival_Time DATE,
        Status VARCHAR(10));""")

    #Delivery_Address table is created
    c.execute("""
    CREATE TABLE Delivery_Address(
        User_ID INTEGER,
        Order_ID INTEGER UNIQUE,
        House_Number VARCHAR(20),
        Road VARCHAR(20),
        County VARCHAR(20),
        Postcode VARCHAR(6),
        UNIQUE(Order_ID),
        PRIMARY KEY(User_ID, Order_ID));""")

    #Order_Products table is created
    c.execute("""
    CREATE TABLE Ordered_Products(
        Order_ID INTEGER PRIMARY KEY,
        User_ID INTEGER,
        Product_Name VARCHAR(20),
        Price DOUBLE,
        Quantity INTEGER);""")

    #Prodcuts table is created
    c.execute("""
    CREATE TABLE Products(
        Product_Name VARCHAR(20) PRIMARY KEY UNIQUE,
        Price DOUBLE,
        Quantity INTEGER,
        Img_address VARCHAR(20));""")

    conn.commit()#Changes are commited
    conn.close()#Connection to DB is closed


def store_user(username, password):
    conn = sqlite3.connect("databases/data.db")
    c = conn.cursor()

    #Username and A hashed password are inserted into database via SQL
    c.execute("""
    INSERT INTO Users(Username, Password) VALUES (?, ?)""", (username, hash_string(password)))
    
    conn.commit()#Changes are commited
    conn.close()#Connection to DB is closed
    print("Query Successful")


def store_delivery_address(user_id, order_id, house_number, road, county, postcode):
    """Inserts passed address data to delivery address table"""
    conn = sqlite3.connect("databases/data.db")#Connection to DB is made
    c = conn.cursor()

    c.execute("""
    INSERT INTO Delivery_Address(User_Id, Order_ID, House_Number, Road, County, Postcode) 
    VALUES(?, ?, ?, ?, ?, ?)""", (user_id, order_id, house_number, road, county, postcode))

    conn.commit()#Changes are commited
    conn.close()#Connection to DB is closed
    print("Query Successful")


def store_ordered_products(order_id, user_id, product_name, price, quantity):
    """Inserts order data into Ordered_Products table"""
    conn = sqlite3.connect("databases/data.db")#Connection to DB is made
    c = conn.cursor()

    c.execute("""
    INSERT INTO Ordered_Products(Order_ID, User_ID, Product_Name, Price, Quantity)
    VALUES(?, ?, ?, ?, ?)""", (order_id, user_id, product_name, price, quantity))

    conn.commit()#Changes are commited
    conn.close()#Connection to DB is closed
    print("Query Successful")


def store_products(product_name, price, quantity, img_address):
    """Inserts product data into Products table"""
    conn = sqlite3.connect("databases/data.db")#Connection to DB is made
    c = conn.cursor()

    c.execute("""
    INSERT INTO Products(Product_Name, Price, Quantity, Img_address)
    VALUES(?, ?, ?, ?)""", (product_name, price, quantity, img_address))

    conn.commit()#Changes are commited
    conn.close()#Connection to DB is closed
    print("Query Successful")


def store_user_orders(user_id, arrival_time, status):
    """Inserts order data into User_Orders table"""
    conn = sqlite3.connect("databases/data.db")#Connection to DB is made
    c = conn.cursor()

    c.execute("""
    INSERT INTO User_Orders(User_ID, Arrival_Time, Status)
    VALUES (?, ?, ?)""", (user_id, arrival_time, status))

    conn.commit()#Changes are commited
    conn.close()#Connection to DB is closed
    print("Query Successful")


if __name__ == "__main__":
    app.run()
    print("Done!")