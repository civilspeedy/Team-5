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


def create_tables():
    """This function will exicute SQL queries to create the required tables."""
    conn = sqlite3.connect("databases/data.db")
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
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
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


if __name__ == "__main__":
    store_user("Charlie", "test")