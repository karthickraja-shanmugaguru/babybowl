from flask import Flask, jsonify, url_for

app = Flask(__name__)

# Mock Data
banner_data = [
    {"id": "banner1", "image_url": "Banner1.png", "banner_type": "Home"},
    {"id": "banner2", "image_url": "Banner2.png", "banner_type": "Home"},
    {"id": "banner3", "image_url": "Banner3.png", "banner_type": "Home"}
]

category_data = [
    {
        "id": "1",
        "name": "Foods",
        "image_url": "https://example.com/images/electronics.jpg",
        "is_active": True
    }
]

product_data = [
    {
        "id": "product_sathu_maavu",
        "name": "Sathu Maavu",
        "image_url": "https://example.com/images/sathu_maavu.jpg",
        "price": 150.00,
        "currency": "INR",
        "rating": 4.7,
        "is_available": True,
        "categories": ["Food", "Health Mix"],
        "description": "Nutritious multigrain health mix made with natural ingredients",
        "brand": "Health Foods",
        "shipping_info": {
            "weight": "500 g",
            "shipping_cost": 40
        },
        "tags": ["multigrain", "organic", "health mix"]
    }
]

# Routes

@app.route('/dashboard/banner', methods=['GET'])
def get_banners():
    # Update image URLs to point to the static folder
    for banner in banner_data:
        banner['image_url'] = url_for('static', filename=f"Image/{banner['image_url']}")
    return jsonify({"data": banner_data})

@app.route('/dashboard/categories', methods=['GET'])
def get_categories():
    return jsonify({"data": category_data})

@app.route('/dashboard/products', methods=['GET'])
def get_products():
    return jsonify({"data": product_data})

@app.route('/api', methods=['GET'])
def get_api():
    return "Welcome to BabyBowl API"

@app.route('/', methods=['GET'])
def home():
    return "Welcome to Babybowl Backend"

if __name__ == '__main__':
    app.run(debug=True)
