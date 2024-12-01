from flask import Flask, jsonify

app = Flask(__name__)

# Mock Data

# Banners
banner_data = [
    {
        "id": "banner1",
        "image_url": "https://example.com/images/banner1.jpg",
        "link": "test",
        "start_date": "01-01-2024",
        "end_date": "01-01-2025",
        "banner_type": "Home",
        "priority": 1
    },
    {
        "id": "banner2",
        "image_url": "https://example.com/images/banner2.jpg",
        "link": "https://example.com/new-arrivals",
        "start_date": "01-02-2024",
        "end_date": "01-02-2025",
        "banner_type": "Home",
        "priority": 2
    }
]

# Categories
category_data = [
    {
        "id": "1",
        "name": "Foods",
        "image_url": "https://example.com/images/electronics.jpg",
        "is_active": True,
        "url": "test"
    }
]

# Products
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
    return jsonify({"data": banner_data})

@app.route('/dashboard/categories', methods=['GET'])
def get_categories():
    return jsonify({"data": category_data})

@app.route('/dashboard/products', methods=['GET'])
def get_products():
    return jsonify({"data": product_data})

@app.route('/api',methods = ['GET'])
def get_api():
    return ("Welcome to BabyBowl API")

if __name__ == '__main__':
    app.run(debug=True)
