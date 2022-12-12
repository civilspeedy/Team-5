from flask import *
import sqlite3 
import hashlib 


app = Flask(__name__)

#For populating Database
list_of_items = (["Lamp", 50.00, 10, "lamp.jpg"], 
["Desk", 120.00, 5, "desk.jpg"], 
["Hammer", 10.00, 50, "hammer.jpg"], 
["Pencils", 2.00, 132, "pencil.jpg"], 
["Towel", 15.00, 52, "towel.jpg"], 
["Computer Monitor", 120.00, 15, "monitor.jpg"], 
["Computer", 300.00, 10, "computer.jpg"], 
["Smart Phone", 200.00, 11, "phone.jpg"], 
["Digit Clock", 50.00, 28, "clock.jpg"], 
["Keyboard", 25.00, 30, "keyboard.jpg"], 
["Map of Talbot Campus", 50.00, 10, "map.jpg"],
["Sea Monkeys", 8.00, 700, "seamonkeys.jpg"], 
["Bird feeder", 10.00, 50, "tweet.jpg"], 
["Lorax DVD", 29.99, 100, "Lorax.jpg"], 
["Model Coconut",70.00, 5, "tropical.jpg"], 
["fish tank", 300.00, 12, "fish.jpg"], 
["Dog Toy", 12.00, 35, "dogToy.jpg"], 
["JavaScript for Dummies", 32.99, 100, "book.jpg"], 
["Laptop",250.00, 12, "laptop.jpg"], 
["Camera", 200.00, 10, "camera.jpg"])


def populate_db():
    """For filling database with items"""
    print(list_of_items)
    for product in list_of_items:
        store_products(product[0], product[1], product[2], product[3])
        print(product[0], "added")


def hash_string(string):
    """Will hash input string and return it"""
    return hashlib.sha256(string.encode()).hexdigest()


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

@app.route("/onSale")
def render_on_sale():
    return render_template("on sale.html")

@app.route("/browse")
def render_browse():
    return render_template("browse.html")

@app.route("/search")
def render_search():
    return render_template("Search.html")

@app.route('/createAccount')
def render_create_account():
    return render_template("CreateAccount.html")

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


app.route('/api/signUp', methods=['GET'])
def sign_up():
    """Gets user login info and stores it"""
    store_user(request.args.get("username"), request.args.get("password"))
    return make_response(jsonify({"result": "ok"}, 200))


@app.route('/api/login', methods=['GET'])
def login():
    """Authenticates user login info"""
    conn = sqlite3.connect("databases/data.db")#Connection to DB is made
    c = conn.cursor()

    c.execute("""
    SELECT Password FROM Users WHERE Username = ?""", request.args.get("username"))
    password = c.fetchone()
    conn.close()

    if hash_string(request.args.get("password")) == password:
        return make_response(jsonify({"result": "authenticated"}, 200))
    else:
        return make_response(jsonify({"result": "failure"}, 400))


@app.route('/api/getSearchTerm', methods=['GET'])
def get_search_term():
    search_term = request.args.get("term")
    print(search_term)
    neutralised_term = f"{search_term[0].upper()}{search_term[1:].lower()}"
    print(f"neutral>>{neutralised_term}")
    conn = sqlite3.connect("databases/data.db")#Connection to DB is made
    c = conn.cursor()

    c.execute("""SELECT * FROM Products WHERE Product_Name = ?""", (neutralised_term,))
    items = c.fetchall()
    print(items)
    conn.close()
    if items == []:
        return make_response(jsonify({"result": "failure"}, 400))
    else:
        return make_response(jsonify({"result": "ok"}, 200, items))


@app.route('/api/getAllProducts')
def get_all_products():
    """Returns all elements in products table to API"""
    conn = sqlite3.connect("databases/data.db")#Connection to DB is made
    c = conn.cursor()

    c.execute("""SELECT * FROM Products""")
    items = c.fetchall()
    conn.close()
    return make_response(jsonify({"result": "ok"}, 200, items))


@app.route("/api/getFeatured")
def get_featured():
    """This will return five random products to be used as the featured items"""
    conn = sqlite3.connect("databases/data.db")#Connection to DB is made
    c = conn.cursor()

    c.execute("""
    SELECT * FROM Products ORDER BY RANDOM() LIMIT 5""") #fetches 5 random rows
    items = c.fetchall()
    conn.close()
    print(items)
    return make_response(jsonify({"result": "ok"}, 200, items))
    

if __name__ == "__main__":
    app.run()