from flask import Flask, jsonify, url_for
from flask_cors import CORS, cross_origin 

app = Flask(__name__)

# Mock Data
banner_data = [
    {"id": "banner3", "image_url": "https://backend.babybowl.life/static/Image/Banner3.png", "banner_type": "Home"}
]

# category_data = [
#     {
#         "id": "1",
#         "name": "Foods",
#         "image_url": "https://backend.babybowl.life/static/Image/food4.jpg",
#         "is_active": True
#     },
#     {
#         "id": "2",
#         "name": "Toys",
#         "image_url": "https://backend.babybowl.life/static/Image/Toys1.png",
#         "is_active": True
#     },
#     {
#         "id": "3",
#         "name": "Oil",
#         "image_url": "https://backend.babybowl.life/static/Image/oil1.png",
#         "is_active": True
#     },
#     {
#         "id": "4",
#         "name": "Dress",
#         "image_url": "https://backend.babybowl.life/static/Image/dress1.png",
#         "is_active": True
#     },
#     {
#         "id": "5",
#         "name": "Soap",
#         "image_url": "https://backend.babybowl.life/static/Image/soap1.png",
#         "is_active": True
#     }
# ]

category_data = [
    {"id": "1", "name": "Baby Foods", "image_url": "https://backend.babybowl.life/static/Image/food4.jpg", "is_active": True},
    {"id": "2", "name": "Baby Toys", "image_url": "https://backend.babybowl.life/static/Image/food4.jpg", "is_active": True},
    {"id": "3", "name": "Baby Oils", "image_url": "https://backend.babybowl.life/static/Image/food4.jpg", "is_active": True},
    {"id": "4", "name": "Baby Clothes", "image_url": "https://backend.babybowl.life/static/Image/food4.jpg", "is_active": True},
    {"id": "5", "name": "Baby Soaps", "image_url": "https://backend.babybowl.life/static/Image/food4.jpg", "is_active": True},
    {"id": "6", "name": "Diapers", "image_url": "https://backend.babybowl.life/static/Image/food4.jpg", "is_active": True},
    {"id": "7", "name": "Bath Essentials", "image_url": "https://backend.babybowl.life/static/Image/food4.jpg", "is_active": True},
    {"id": "8", "name": "Storybooks", "image_url": "https://backend.babybowl.life/static/Image/food4.jpg", "is_active": True},
    {"id": "9", "name": "Feeding Bottles", "image_url": "https://backend.babybowl.life/static/Image/food4.jpg", "is_active": True},
    {"id": "10", "name": "Baby Skincare", "image_url": "https://backend.babybowl.life/static/Image/food4.jpg", "is_active": True},
    {"id": "11", "name": "Baby Blankets", "image_url": "https://backend.babybowl.life/static/Image/food4.jpg", "is_active": True},
    {"id": "12", "name": "Strollers", "image_url": "https://backend.babybowl.life/static/Image/food4.jpg", "is_active": True},
    {"id": "13", "name": "Car Seats", "image_url": "https://backend.babybowl.life/static/Image/food4.jpg", "is_active": True},
    {"id": "14", "name": "Baby Cribs", "image_url": "https://backend.babybowl.life/static/Image/food4.jpg", "is_active": True},
    {"id": "15", "name": "Swaddles", "image_url": "https://backend.babybowl.life/static/Image/food4.jpg", "is_active": True},
    {"id": "16", "name": "Pillows for Babies", "image_url": "https://backend.babybowl.life/static/Image/food4.jpg", "is_active": True},
    {"id": "17", "name": "Pacifiers", "image_url": "https://backend.babybowl.life/static/Image/food4.jpg", "is_active": True},
    {"id": "18", "name": "Teethers", "image_url": "https://backend.babybowl.life/static/Image/food4.jpg", "is_active": True},
    {"id": "19", "name": "Health Supplements", "image_url": "https://backend.babybowl.life/static/Image/food4.jpg", "is_active": True},
    {"id": "20", "name": "Baby Cleaning Supplies", "image_url": "https://backend.babybowl.life/static/Image/food4.jpg", "is_active": True}
]



# product_data = [
#     {
#         "id": "1",
#         "name": "Sathu Maavu",
#         "image_url": "https://backend.babybowl.life/static/Image/food4.jpg",
#         "price": 150.00,
#         "currency": "INR",
#         "rating": 4.7,
#         "is_available": True,
#         "categories": ["Food"],
#         "description": "Nutritious multigrain health mix made with natural ingredients",
#         "brand": "Health Foods",
#         "ProductInfo": {
#             "measurementsName": "500 g",
#             "measuremtnsList": 50
#         },
#         "tags": ["multigrain", "organic", "health mix"]
#     },
#     {
#         "id": "2",
#         "name": "Toys",
#         "image_url": "https://backend.babybowl.life/static/Image/Toys1.png",
#         "price": 150.00,
#         "currency": "INR",
#         "rating": 4.7,
#         "is_available": True,
#         "categories": ["Toys"],
#         "description": "Nutritious multigrain health mix made with natural ingredients",
#         "brand": "Health Foods",
#         "ProductInfo": {
#             "measurementsName": "",
#             "measuremtnsList": []
#         },
#         "tags": ["toys"]
#     },
#     {
#         "id": "Hair oil",
#         "name": "Hair oil",
#         "image_url": "https://backend.babybowl.life/static/Image/oil1.png",
#         "price": 150.00,
#         "currency": "INR",
#         "rating": 4.7,
#         "is_available": True,
#         "categories": ["oil"],
#         "description": "Nutritious multigrain health mix made with natural ingredients",
#         "brand": "Health Foods",
#         "ProductInfo": {
#             "measurementsName": "liter",
#             "measuremtnsList": ["1ltr","500 ML","'200 ML"]
#         },
#         "tags": ["oil"]
#     },
#     {
#         "id": "Dress",
#         "name": "Dress",
#         "image_url": "https://backend.babybowl.life/static/Image/dress1.png",
#         "price": 150.00,
#         "currency": "INR",
#         "rating": 4.7,
#         "is_available": True,
#         "categories": ["Dress"],
#         "description": "Nutritious multigrain health mix made with natural ingredients",
#         "brand": "Health Foods",
#         "ProductInfo": {
#             "measurementsName": "Size",
#             "measuremtnsList": ["xl","M","S"]
#         },
#         "tags": ["Dress"]
#     },
#     {
#         "id": "Soap",
#         "name": "Soap",
#         "image_url": "https://backend.babybowl.life/static/Image/soap1.png",
#         "price": 150.00,
#         "currency": "INR",
#         "rating": 4.7,
#         "is_available": True,
#         "categories": ["Soap"],
#         "description": "Nutritious multigrain health mix made with natural ingredients",
#         "brand": "Health Foods",
#         "ProductInfo": {
#             "measurementsName": "Weight",
#             "measuremtnsList": ["200g","100g"]
#         },
#         "tags": ["Soap"]
#     }
# ]


product_data = [
    # Baby Foods
    {"id": "1", "name": "Sathu Maavu", "image_url": "https://backend.babybowl.life/static/Image/Toys1.png", "price": 150.00, "currency": "INR", "rating": 4.7, "is_available": True, "categories": ["Baby Foods"], "description": "Nutritious multigrain health mix.", "brand": "Health Foods", "ProductInfo": {"measurementsName": "Weight", "measuremtnsList": ["500g"]}, "tags": ["multigrain", "health mix"]},
    {"id": "2", "name": "Baby Cereal", "image_url": "https://backend.babybowl.life/static/Image/Toys1.png", "price": 200.00, "currency": "INR", "rating": 4.6, "is_available": True, "categories": ["Baby Foods"], "description": "Healthy cereal for babies.", "brand": "Baby Care", "ProductInfo": {"measurementsName": "Weight", "measuremtnsList": ["250g"]}, "tags": ["cereal", "baby food"]},

    # Baby Toys
    {"id": "3", "name": "Soft Plush Toy", "image_url": "https://backend.babybowl.life/static/Image/Toys1.png", "price": 250.00, "currency": "INR", "rating": 4.8, "is_available": True, "categories": ["Baby Toys"], "description": "Soft plush toy made with safe materials.", "brand": "Toy World", "ProductInfo": {"measurementsName": "Dimensions", "measuremtnsList": ["30 cm"]}, "tags": ["plush", "toys"]},
    {"id": "4", "name": "Stacking Rings", "image_url": "https://backend.babybowl.life/static/Image/Toys1.png", "price": 300.00, "currency": "INR", "rating": 4.5, "is_available": True, "categories": ["Baby Toys"], "description": "Colorful stacking rings for coordination.", "brand": "Fun Toys", "ProductInfo": {"measurementsName": "", "measuremtnsList": []}, "tags": ["stacking", "educational"]},

    # Baby Oils
    {"id": "5", "name": "Hair Oil", "image_url": "https://backend.babybowl.life/static/Image/Toys1.png", "price": 350.00, "currency": "INR", "rating": 4.9, "is_available": True, "categories": ["Baby Oils"], "description": "Nourishing baby hair oil.", "brand": "Baby Naturals", "ProductInfo": {"measurementsName": "Volume", "measuremtnsList": ["500 ml"]}, "tags": ["hair oil", "herbal"]},
    {"id": "6", "name": "Massage Oil", "image_url": "https://backend.babybowl.life/static/Image/Toys1.png", "price": 400.00, "currency": "INR", "rating": 4.7, "is_available": True, "categories": ["Baby Oils"], "description": "Gentle massage oil for babies.", "brand": "Care Oil", "ProductInfo": {"measurementsName": "Volume", "measuremtnsList": ["250 ml"]}, "tags": ["massage oil", "nourishment"]},

    # Baby Clothes
    {"id": "7", "name": "Baby Onesie", "image_url": "https://backend.babybowl.life/static/Image/Toys1.png", "price": 450.00, "currency": "INR", "rating": 4.6, "is_available": True, "categories": ["Baby Clothes"], "description": "Comfortable cotton onesie.", "brand": "Baby Wear", "ProductInfo": {"measurementsName": "Size", "measuremtnsList": ["S", "M", "L"]}, "tags": ["onesie", "cotton"]},
    {"id": "8", "name": "Baby Frock", "image_url": "https://backend.babybowl.life/static/Image/Toys1.png", "price": 500.00, "currency": "INR", "rating": 4.7, "is_available": True, "categories": ["Baby Clothes"], "description": "Stylish frock for baby girls.", "brand": "Fashion Baby", "ProductInfo": {"measurementsName": "Size", "measuremtnsList": ["S", "M", "L"]}, "tags": ["frock", "stylish"]},

    # Baby Soaps
    {"id": "9", "name": "Mild Baby Soap", "image_url": "https://backend.babybowl.life/static/Image/Toys1.png", "price": 100.00, "currency": "INR", "rating": 4.9, "is_available": True, "categories": ["Baby Soaps"], "description": "Mild soap to keep baby skin soft.", "brand": "Gentle Care", "ProductInfo": {"measurementsName": "Weight", "measuremtnsList": ["200g"]}, "tags": ["soap", "gentle"]},
    {"id": "10", "name": "Organic Baby Soap", "image_url": "https://backend.babybowl.life/static/Image/Toys1.png", "price": 120.00, "currency": "INR", "rating": 4.8, "is_available": True, "categories": ["Baby Soaps"], "description": "Organic soap with natural ingredients.", "brand": "Nature's Touch", "ProductInfo": {"measurementsName": "Weight", "measuremtnsList": ["100g"]}, "tags": ["organic soap", "natural"]},

    # Diapers
    {"id": "11", "name": "Disposable Diapers", "image_url": "https://backend.babybowl.life/static/Image/Toys1.png", "price": 500.00, "currency": "INR", "rating": 4.5, "is_available": True, "categories": ["Diapers"], "description": "Super absorbent disposable diapers.", "brand": "DiaperCare", "ProductInfo": {"measurementsName": "Pack", "measuremtnsList": ["S", "M"]}, "tags": ["disposable", "diapers"]},
    {"id": "12", "name": "Reusable Cloth Diapers", "image_url": "https://backend.babybowl.life/static/Image/Toys1.png", "price": 350.00, "currency": "INR", "rating": 4.6, "is_available": True, "categories": ["Diapers"], "description": "Eco-friendly reusable cloth diapers.", "brand": "Eco Baby", "ProductInfo": {"measurementsName": "Pack Size", "measuremtnsList": ["3-Pack"]}, "tags": ["reusable", "cloth diapers"]},

    # Bath Essentials
    {"id": "13", "name": "Baby Shampoo", "image_url": "https://backend.babybowl.life/static/Image/Toys1.png", "price": 180.00, "currency": "INR", "rating": 4.8, "is_available": True, "categories": ["Bath Essentials"], "description": "Gentle shampoo for babies.", "brand": "Gentle Wash", "ProductInfo": {"measurementsName": "Volume", "measuremtnsList": ["200 ml"]}, "tags": ["shampoo", "bath"]},
    {"id": "14", "name": "Bath Sponge", "image_url": "https://backend.babybowl.life/static/Image/Toys1.png", "price": 100.00, "currency": "INR", "rating": 4.5, "is_available": True, "categories": ["Bath Essentials"], "description": "Soft bath sponge for babies.", "brand": "Soft Care", "ProductInfo": {"measurementsName": "", "measuremtnsList": []}, "tags": ["bath sponge", "soft"]},

    # Add products for remaining categories...
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
