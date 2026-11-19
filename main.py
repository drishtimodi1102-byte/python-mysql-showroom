import os
import mysql.connector as sq
from dotenv import load_dotenv
load_dotenv()
mycon = sq.connect(host=os.getenv("DB_HOST"), user=os.getenv("DB_USER"),
                   passwd=os.getenv("DB_PASSWORD"), database=os.getenv("DB_NAME"))
c = mycon.cursor()
print("Successfully connected")
def show(table, col):
    print("1. Model Name")
    print("2. Price")
    print("3. Show All")
    f = int(input("Select filter: "))
    if f == 1:
        n = input("Enter product number: ")
        q = "select * from " + table + " where product_no=%s"
        c.execute(q, (n,))
    elif f == 2:
        n = int(input("Enter upper limit of cost: "))
        q = "select * from " + table + " where price<=%s"
        c.execute(q, (n,))
    elif f == 3:
        c.execute("select * from " + table)
    else:
        print("Invalid choice")
        return
    d = c.fetchall()
    if len(d) == 0:
        print("No similar result found")
    else:
        for i in d:
            print(i)

# Function to place order
def order():
    nm = input("Enter your name: ")
    p = input("Enter vehicle type: ")
    m = input("Enter model name: ")
    pay = input("Enter mode of payment: ")
    y = input("Enter contact number: ")
    q = "insert into orders values(%s,%s,%s,%s,%s)"
    c.execute(q, (nm, p, m, pay, y))
    mycon.commit()
    print("Order placed successfully")

# Main program
print("WELCOME TO OUR ONLINE SHOWROOM")
x = input("Enter yes if you want to shop: ")
while x.lower() == "yes":
    print("1. CARS")
    print("2. BIKES")
    print("3. SCOOTY")
    print("4. TRUCK")
    print("5. TRACTORS")
    print("6. BUS")
    choice = int(input("Select your choice: "))
    if choice == 1:
        show("cars", "product_no")
    elif choice == 2:
        show("bike", "product_no")
    elif choice == 3:
        show("SCOOTY", "product_no")
    elif choice == 4:
        show("TRUCKS", "product_no")
    elif choice == 5:
        show("TRACTOR", "product_no")
    elif choice == 6:
        show("BUS", "product_no")
    else:
        print("Invalid choice")
    ask = input("Do you wish to explore more (y/n): ")
    if ask.lower() == "n":
        print("For placing your order")
        order()
        print("Thank you for shopping")
        break
mycon.close()
