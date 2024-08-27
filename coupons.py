class CouponManager:
    def __init__(self):
        # Sample coupon data
        self.coupons = [
            {"code": "SAVE10", "discount": 10},
            {"code": "SAVE20", "discount": 20},
        ]

    def save_coupon(self, coupon_data):
        # Save new coupon
        self.coupons.append(coupon_data)

    def get_all_coupons(self):
        # Retrieve all coupons
        return self.coupons

    def search_coupon_by_code(self, code):
        # Find coupon by code
        return next((c for c in self.coupons if c['code'].lower() == code.lower()), None)
