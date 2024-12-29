from flask import Flask, jsonify, url_for
from flask_cors import CORS, cross_origin 

app = Flask(__name__)

# Mock Data
banner_data = [
    {"id": "banner3", "image_url": "https://backend.babybowl.life/static/Image/Banner3.png", "banner_type": "Home"}
]

category_data = [
    {
        "id": "1",
        "name": "Foods",
        "image_url": "https://backend.babybowl.life/static/Image/food4.jpg",
        "is_active": True
    },
    {
        "id": "1",
        "name": "Toys",
        "image_url": "https://backend.babybowl.life/static/Image/Toys1.png",
        "is_active": True
    },
    {
        "id": "1",
        "name": "Oil",
        "image_url": "https://backend.babybowl.life/static/Image/oil1.png",
        "is_active": True
    }
]

product_data = [
    {
        "id": "product_sathu_maavu",
        "name": "Sathu Maavu",
        "image_url": "https://backend.babybowl.life/static/Image/food4.jpg",
        "price": 150.00,
        "currency": "INR",
        "rating": 4.7,
        "is_available": True,
        "categories": ["Food", "Health Mix"],
        "description": "Nutritious multigrain health mix made with natural ingredients",
        "brand": "Health Foods",
        "shipping_info": {
            "weight": "500 g",
            "shipping_cost": 50
        },
        "tags": ["multigrain", "organic", "health mix"]
    },
    {
        "id": "Toys",
        "name": "Toys",
        "image_url": "https://backend.babybowl.life/static/Image/Toys1.jpg",
        "price": 150.00,
        "currency": "INR",
        "rating": 4.7,
        "is_available": True,
        "categories": ["Toys"],
        "description": "Nutritious multigrain health mix made with natural ingredients",
        "brand": "Health Foods",
        "shipping_info": {
            "weight": "500 g",
            "shipping_cost": 50
        },
        "tags": ["toys"]
    },
    {
        "id": "Hair oil",
        "name": "Hair oil",
        "image_url": "https://backend.babybowl.life/static/Image/oil11.png",
        "price": 150.00,
        "currency": "INR",
        "rating": 4.7,
        "is_available": True,
        "categories": ["Toys"],
        "description": "Nutritious multigrain health mix made with natural ingredients",
        "brand": "Health Foods",
        "shipping_info": {
            "weight": "500 g",
            "shipping_cost": 50
        },
        "tags": ["toys"]
    }
]

# Routes

@app.route('/dashboard/banner', methods=['GET'])
@cross_origin('*')
def get_banners():
    return jsonify({"data": banner_data})

@app.route('/dashboard/categories', methods=['GET'])
@cross_origin('*')
def get_categories():
    return jsonify({"data": category_data})

@app.route('/dashboard/products', methods=['GET'])
@cross_origin('*')
def get_products():
    return jsonify({"data": product_data})

@app.route('/api', methods=['GET'])
@cross_origin('*')
def get_api():
    return "Welcome to BabyBowl API"

@app.route('/', methods=['GET'])
@cross_origin('*')
def home():
    return "Welcome to Babybowl Backend"

if __name__ == '__main__':
    app.run(debug=True)
