class ProductManager:
    def __init__(self):
        # Sample product data
        self.products = [
            {"id": 1, "title": "Product 1", "category": "Electronics", "price": 199.99},
            {"id": 2, "title": "Product 2", "category": "Books", "price": 15.99},
            {"id": 3, "title": "Product 3", "category": "Electronics", "price": 299.99},
        ]

    def get_products_by_category_and_price(self, category, max_price):
        # Filter products based on category and price
        filtered_products = [
            p for p in self.products
            if (category is None or p['category'] == category) and (max_price is None or p['price'] <= max_price)
        ]
        return filtered_products

    def search_product_by_title(self, title):
        # Find product by title
        return next((p for p in self.products if p['title'].lower() == title.lower()), None)
