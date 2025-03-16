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
    {"id": "1", "name": "Yum Bites", "image_url": "https://backend.babybowl.life/static/Image/food4.jpg", "is_active": True},
    {"id": "1", "name": "Soft Wash", "image_url": "https://backend.babybowl.life/static/Image/bathcategory.png", "is_active": True}
   ]

product_data = [
    # foods
    {"id": "1", "name": "Sathu Maavu", "image_url": "https://backend.babybowl.life/static/Image/sathumaavu.png", "price": 200.00, "currency": "INR", "rating": 4.7, "is_available": True, "categories": ["Yum Bites"], "description": "Yum Bites Sathu Maavu is a nutritious blend of cashew nuts, almonds, pistachios, walnuts, ragi, karuppu kavuni, mappillai samba, wheat, barley rice, sorghum, pearl millet, green gram, sago, groundnuts, roasted gram, and palm candy — perfect for a healthy start!", "brand": "BabyBowl", "ProductInfo": {"measurementsName": "Weight", "measuremtnsList": ["500g","200g", "1kg"]}, "tags": ["multigrain", "health mix"]},
    {"id": "2", "name": "Thiraviya Kuliyal Podi", "image_url": "https://backend.babybowl.life/static/Image/thiraviyakuliyalpodi.png", "price": 200.00, "currency": "INR", "rating": 4.9, "is_available": True, "categories": ["Soft Wash"], "description": "Soft Wash - Thiraviya Podi is a gentle herbal mix made with thiraviya podi, vettiver, pulangkilangu, rose petals, hibiscus petals, aavarampoo petals, thiruneetrupattru fibers, orange peel, green gram, chana dal, and almond dal — perfect for soft and healthy skin!", "brand": "BabyBowl", "ProductInfo": {"measurementsName": "Weight", "measuremtnsList": ["500g","200g", "1kg"]}, "tags": ["SoftWash"]},

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
