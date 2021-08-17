from flask import Flask, render_template, abort, request
import json
from data import data

app = Flask(__name__) # create a flask app

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



@app.route("/api/catalog")
def get_catalog():
    return json.dumps(data) 


@app.route("/api/catalog", methods=['POST'])
def save_product():
    product = request.get_json() # returns dictionary
    data.append(product)

    return "OK"


@app.route("/api/categories")
def get_categories():
    """
        Get the unique categories from the catalog(data var)
        and return them as a list of string
    """

    categories = []
    for item in data:
        cat = item["category"] 

        if cat not in categories:
            categories.append(cat)
    
    return json.dumps(categories)


@app.route("/api/catalog/id/<id>")
def get_product_by_id(id):
    
    for item in data:
        if(str(item["_id"]) == id):
            return json.dumps(item)

    abort(404)    

@app.route("/api/catalog/category/<category>")
def get_product_by_category(category):
    results = []
    for item in data:
        if(item["category"].lower() == category.lower()):
            results.append(item)
        
    return json.dumps(results)


@app.route("/api/catalog/cheapest")
def get_cheapest_product():
    cheapest = data[0]
    for item in data:
        if(item["price"] < cheapest["price"]):
            cheapest = item

    return json.dumps(cheapest)



       
            
if __name__ == '__main__':
    app.run(debug=True)