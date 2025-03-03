# from flask import Flask, jsonify, url_for
# from flask_cors import CORS, cross_origin 

from flask import Flask, jsonify, url_for, request
from flask_cors import CORS, cross_origin


app = Flask(__name__)

# Mock Data
banner_data = [
    {"id": "banner3", "image_url": "https://backend.babybowl.life/static/Image/Banner3.png", "banner_type": "Home"}
]

category_data = [
    {"id": "1", "name": "Foods", "image_url": "https://backend.babybowl.life/static/Image/food4.jpg", "is_active": True},
   ]

product_data = [
    # foods
    {"id": "1", "name": "Sathu Maavu", "image_url": "https://backend.babybowl.life/static/Image/Toys1.png", "price": 200.00, "currency": "INR", "rating": 4.7, "is_available": True, "categories": ["Foods"], "description": "Boost your health with our premium Sathu Maavu, a nutritious multigrain health mix packed with the goodness of whole grains, nuts, and pulses. Carefully crafted to provide essential vitamins, minerals, and fiber, this wholesome mix supports digestion, energy, and overall well-being. Ideal for all ages, it’s a perfect choice for a hearty breakfast or a nourishing meal. No preservatives, no artificial flavors—just pure, natural goodness in every scoop!", "brand": "BabyBowl", "ProductInfo": {"measurementsName": "Weight", "measuremtnsList": ["500g","200g","1Kg"]}, "tags": ["multigrain", "health mix"]}
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

@app.route('/dashboard/products/all', methods=['GET'])
@cross_origin('*')
def get_all_products():
    return jsonify({"data": product_data})

@app.route('/dashboard/products/', methods=['GET'])
@cross_origin('*')
def get_products():
    category = request.args.get('category', '').strip()
    
    # If category is empty or not found, return all products
    if not category:
        return jsonify({"data": product_data})
    
    # Filter products by category
    filtered_products = [product for product in product_data if category.lower() in map(str.lower, product['categories'])]
    
    # If no products match the category, return all products
    if not filtered_products:
        return jsonify({"data": product_data})
    
    return jsonify({"data": filtered_products})

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
