from flask import Flask, request, jsonify
from products import ProductManager
from coupons import CouponManager

app = Flask(__name__)

product_manager = ProductManager()
coupon_manager = CouponManager()

# Endpoint to retrieve products by category and price
@app.route('/products', methods=['GET'])
def get_products():
    category = request.args.get('category')
    max_price = request.args.get('max_price', type=float)
    products = product_manager.get_products_by_category_and_price(category, max_price)
    return jsonify(products)

# Endpoint to search product by title
@app.route('/products/search', methods=['GET'])
def search_product():
    title = request.args.get('title')
    product = product_manager.search_product_by_title(title)
    return jsonify(product or {})

# Endpoint to save a new coupon code
@app.route('/coupons', methods=['POST'])
def save_coupon():
    coupon_data = request.get_json()
    coupon_manager.save_coupon(coupon_data)
    return jsonify({"message": "Coupon saved successfully."}), 201

# Endpoint to retrieve all coupon codes
@app.route('/coupons', methods=['GET'])
def get_coupons():
    coupons = coupon_manager.get_all_coupons()
    return jsonify(coupons)

# Endpoint to search for a specific coupon code
@app.route('/coupons/search', methods=['GET'])
def search_coupon():
    code = request.args.get('code')
    coupon = coupon_manager.search_coupon_by_code(code)
    return jsonify(coupon or {})

if __name__ == '__main__':
    app.run(debug=True)
