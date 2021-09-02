from flask import Flask, render_template, abort, request
import json

from pymongo import cursor, results
from data import data
from flask_cors import CORS
from config import db, parse_json

app = Flask(__name__) # create a flask app
CORS(app)

me = {
    "name": "Corey",
    "last_name": "Arnold",
    "age": 27,
    "email": "carnold9438@gmail.com",
    "address": {
        "street": "504 acorn",
        "number": 42,
    }
}



######## Home/About/ AboutEmail ########

@app.route('/')
@app.route('/home')
def home_page():
    return render_template("index.html")



@app.route("/about") 
def about_me():
    return me["name"] + " " + me["last_name"]



@app.route("/about/email")
def my_email():
    return me["email"]  # get data out of dictionary



############ Catalog ##################

@app.route("/api/catalog")
def get_catalog():
    cursor = db.products.find({})
    prods = [ prod for prod in cursor ]

    return parse_json(prods)



@app.route("/api/catalog", methods=['POST'])
def save_product():
    product = request.get_json() # returns dictionary

    # validations
    if not "title" in product:
        return parse_json({"error": "title is required", "success": False})

    if not "price" in product or not product["price"]:
        return parse_json({"error": "price is required, and shouldn't be zero", "success": False})    

    db.products.insert_one(product)
    return parse_json(product)



############ Coupons #################
@app.route("/api/couponCodes/<code>")
def get_coupon(code):
    code = db.couponCodes.find_one({"code": code})
    return parse_json(code)



@app.route("/api/couponCodes")
def get_coupons():
    cursor = db.couponCodes.find({})
    codes=[code for code in cursor]
    return parse_json(codes)

@app.route("/api/couponCodes", methods=['POST'])
def save_coupon():
    coupon = request.get_json()

    # validations
    if not "code" in coupon:
        return parse_json({"error": "code is required", "success": False})

    if not "discount" in coupon or not coupon["discount"]:
        return parse_json({"error": "discount is required, and shouldnt be zero", "success": False})

    db.couponCodes.insert_one(coupon)
    return parse_json(coupon)



############# Categories #############

@app.route("/api/categories")
def get_categories():
    """
        Get the unique categories from the catalog(data var)
        and return them as a list of string
    """

    cursor = db.products.find({})
    categories = []
    for item in cursor:
        cat = item["category"] 

        if cat not in categories:
            categories.append(cat)
    
    return parse_json(categories)



########### Catalog Id ###########
@app.route("/api/catalog/id/<id>")
def get_product_by_id(id):
    
    product = db.products.find_one({"_id": id})
    if not product:
        abort(404)

    return parse_json(product)
       

@app.route("/api/catalog/category/<category>")
def get_product_by_category(category):
    cursor = db.products.find({"category": category })
    results = [prod for prod in cursor]
    return parse_json(results)



######### Cheapest ###############

@app.route("/api/catalog/cheapest")
def get_cheapest_product():
    cheapest = data[0]
    for item in data:
        if(item["price"] < cheapest["price"]):
            cheapest = item

    return parse_json(cheapest)



############ Test DB Populate ###########

@app.route("/api/test/populatedb")
def populate_db():
    for prod in data:
        db.products.insert_one(prod)
    
    return "Data loaded"



############ Orders ##################

@app.route("/api/orders", methods=["post"])
def save_order():
    order = request.get_json()

    # validate 
    prods = order["products"]
    count = len(prods)
    if(count < 1):
        abort(400, "Error: Orders without products are not allowed!")

    # get the prices for the items included
    #console log the id of each product
    total = 0
    for item in prods:
        id = item["_id"]
        print(id)
    
        db_item = db.products.find_one({"_id": id})
        item["price"] = db_item["price"]

        total += db_item["price"]
          
    print("the total is: ", total)
    order["total"] = total

    # verify and apply the coupon code
    if "couponCode" in order and order["couponCode"]:
        #validate
        code = order["couponCode"]
        coupon = db.couponCodes.find_one({"code": code})
        if coupon:
            discount= coupon["discount"]
            total = total - (total * discount) / 100
            order["total"] = total
        else:
            order["couponCode"] = "INVALID"    


    db.orders.insert_one(order)
    return parse_json(order)

@app.route("/api/orders")
def get_orders():
    cursor = db.orders.find({})
    orders = [order for order in cursor]
    return parse_json(orders)



@app.route("/api/orders/<userId>")
def get_order_for_user(userId):
    cursor = db.orders.find({"userId": userId })
    order = [order for order in cursor]
    return parse_json(order)

3

       
            
if __name__ == '__main__':

    app.run(debug=True)


